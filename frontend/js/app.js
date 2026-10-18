// Vue 应用主模块

const { createApp, ref, reactive, computed, onMounted } = Vue;

// 创建 Vue 应用
const app = createApp({
    setup() {
        // ==================== 状态管理 ====================

        // 当前页面
        const currentPage = ref('login');

        // 加载状态
        const loading = ref(false);

        // 网络错误
        const networkError = ref(false);

        // 用户相关
        const currentUser = ref(null);
        const profile = reactive({
            total_score: 0,
            today_points: 0,
            daily_goal: 10,
        });

        // 表单数据
        const loginForm = reactive({
            username: '',
            password: '',
        });

        const registerForm = reactive({
            name: '',
            username: '',
            phone: '',
            email: '',
            password: '',
            role: 'child',
        });

        const resetForm = reactive({
            username: '',
            phone: '',
            email: '',
            new_password: '',
        });

        // 页面状态
        const showRegister = ref(false);
        const showResetPassword = ref(false);

        // 今日学习数据
        const todayData = reactive({
            new_words_learned: 0,
            review_completed: 0,
            daily_goal: 10,
            remaining_new: 0,
            remaining_review: 0,
            due_today: 0,
            wrong_total: 0,
            today_points: 0,
            signed_in: false,
            continuous_signin_days: 0,
            today_tasks: [],
        });

        // 编辑每日目标
        const editingDailyGoal = ref(10);

        // 词库相关
        const systemLibraries = ref([]);
        const selectedLibraries = ref([]);

        // 学习相关
        const currentWord = ref(null);
        const currentOptions = ref([]);
        const currentWordIndex = ref(0);
        const todayTasks = ref([]);
        const showResult = ref(false);
        const selectedOption = ref(null);
        const isCorrect = ref(false);
        const isPlayingAudio = ref(false);
        const audioFailed = ref(false);

        // 错题本
        const wrongList = ref([]);
        const wrongFilter = ref('all');
        const wrongLoading = ref(false);
        const wrongStats = reactive({
            total_wrong: 0,
            reviewing: 0,
            mastered: 0,
            due_today: 0,
        });

        // Toast 提示
        const toast = reactive({
            show: false,
            message: '',
        });

        // ==================== 工具函数 ====================

        // 显示 Toast
        let toastTimer = null;
        function showToast(msg) {
            if (toastTimer) clearTimeout(toastTimer);
            toast.message = msg;
            toast.show = true;
            toastTimer = setTimeout(() => {
                toast.show = false;
            }, 2500);
        }

        // 网络错误处理
        function handleNetworkError(err) {
            console.error('Network Error:', err);
            networkError.value = true;
            showToast('网络连接失败，请检查网络');
        }

        // ==================== 数据加载 ====================

        // 加载首页数据
        async function loadHomeData() {
            loading.value = true;
            networkError.value = false;
            try {
                const profileData = await getUserProfile();
                Object.assign(profile, profileData);
                editingDailyGoal.value = profileData.daily_goal || 10;

                const todayLearning = await getTodayLearning();
                Object.assign(todayData, todayLearning);

                const libraries = await getSystemLibraries();
                systemLibraries.value = libraries;

                selectedLibraries.value = profileData.selected_library_ids || [];
            } catch (error) {
                if (error.message && error.message.includes('fetch')) {
                    handleNetworkError(error);
                } else {
                    showToast('加载数据失败: ' + error.message);
                }
            } finally {
                loading.value = false;
            }
        }

        // 加载学习任务
        async function loadLearningTasks() {
            loading.value = true;
            try {
                const data = await getTodayLearning();
                todayTasks.value = data.today_tasks || [];
                currentWordIndex.value = 0;

                if (todayTasks.value.length > 0) {
                    await loadNextWord();
                } else {
                    showToast('今天的学习任务已完成！');
                    currentPage.value = 'home';
                }
            } catch (error) {
                showToast('加载学习任务失败');
            } finally {
                loading.value = false;
            }
        }

        // 加载下一个单词
        async function loadNextWord() {
            clearAdvance();
            if (currentWordIndex.value >= todayTasks.value.length) {
                showToast('学习完成！🎉');
                currentPage.value = 'home';
                await loadHomeData();
                return;
            }

            const task = todayTasks.value[currentWordIndex.value];
            currentWord.value = task;
            showResult.value = false;
            selectedOption.value = null;

            // 进入单词先读单词本身：放在 await 之前，保留用户手势，移动端才不会被拦
            playAudio(task.word).catch(() => {});

            try {
                const options = await getQuizOptions(task.word_id);
                currentOptions.value = options.options || [];
                // 用题库返回的最新释义/例句/词性/词形补全（复习任务里没有这些字段）
                currentWord.value = {
                    ...task,
                    meaning: options.meaning || task.meaning,
                    phonetic: options.phonetic || task.phonetic,
                    example_sentence: options.example_sentence || task.example_sentence || '',
                    example_zh: options.example_zh || task.example_zh || '',
                    example_source: options.example_source || task.example_source || '',
                    pos: options.pos || task.pos || '',
                    irregular_forms: options.irregular_forms || task.irregular_forms || null,
                    word_forms: options.word_forms || task.word_forms || null,
                };
            } catch (error) {
                showToast('加载选项失败');
            }

            // 预取下一题音频，减少等待
            preloadTask(currentWordIndex.value + 1);
        }

        function preloadTask(idx) {
            const next = todayTasks.value[idx];
            if (!next) return;
            preloadAudio(next.word);
            if (next.example_sentence) preloadAudio(next.example_sentence);
        }

        function preloadAudio(text) {
            if (!text) return;
            try {
                fetch(audioUrl(text), { cache: 'force-cache' }).catch(() => {});
            } catch (e) {}
        }

        function audioUrl(text) {
            return `${CONFIG.API_BASE}/tts?text=${encodeURIComponent(text)}`;
        }

        // ==================== 生命周期 ====================

        onMounted(async () => {
            // 监听全局 401 事件：token 失效时回到登录页
            window.addEventListener('auth:invalid', () => {
                logout();
                currentUser.value = null;
                currentPage.value = 'login';
                showToast('登录已过期，请重新登录');
            });

            const token = localStorage.getItem(CONFIG.TOKEN_KEY);
            const userStr = localStorage.getItem(CONFIG.USER_KEY);

            if (token && userStr) {
                try {
                    // 先校验 token 是否有效（后端密钥可能已更换）
                    const user = await getCurrentUser();
                    currentUser.value = user;
                    localStorage.setItem(CONFIG.USER_KEY, JSON.stringify(user));
                    currentPage.value = 'home';
                    await loadHomeData();
                } catch (e) {
                    console.error('登录状态恢复失败:', e);
                    logout();
                    currentPage.value = 'login';
                }
            }
        });

        // ==================== 登录注册 ====================

        async function handleLogin() {
            if (!loginForm.username || !loginForm.password) {
                showToast('请填写用户名和密码');
                return;
            }

            loading.value = true;
            try {
                await login(loginForm.username, loginForm.password);
                const userStr = localStorage.getItem(CONFIG.USER_KEY);
                currentUser.value = JSON.parse(userStr);
                currentPage.value = 'home';
                showToast('登录成功！');
                await loadHomeData();
            } catch (error) {
                showToast('登录失败: ' + error.message);
            } finally {
                loading.value = false;
            }
        }

        async function handleRegister() {
            if (!registerForm.name || !registerForm.password) {
                showToast('请填写姓名和密码');
                return;
            }

            loading.value = true;
            try {
                await register(registerForm);
                showToast('注册成功，请登录！');
                showRegister.value = false;
                loginForm.username = '';
                loginForm.password = '';
            } catch (error) {
                showToast('注册失败: ' + error.message);
            } finally {
                loading.value = false;
            }
        }

        async function handleResetPassword() {
            if (!resetForm.username || !resetForm.new_password) {
                showToast('请填写用户名和新密码');
                return;
            }

            if (!resetForm.phone && !resetForm.email) {
                showToast('请填写手机号或邮箱');
                return;
            }

            loading.value = true;
            try {
                await resetPassword(
                    resetForm.username,
                    resetForm.phone,
                    resetForm.email,
                    resetForm.new_password
                );
                showToast('密码重置成功，请登录！');
                showResetPassword.value = false;
            } catch (error) {
                showToast('密码重置失败: ' + error.message);
            } finally {
                loading.value = false;
            }
        }

        function handleLogout() {
            logout();
            currentUser.value = null;
            currentPage.value = 'login';
            showToast('已退出登录');
        }

        // ==================== 签到 ====================

        async function handleSignIn() {
            loading.value = true;
            try {
                const data = await dailySignIn();
                if (typeof data.user_total_score === 'number') {
                    profile.total_score = data.user_total_score;
                } else {
                    profile.total_score += data.bonus_score || 0;
                }
                if (typeof data.daily_points === 'number') {
                    profile.today_points = data.daily_points;
                }
                todayData.signed_in = true;
                if (data.continuous_signin_days) {
                    profile.continuous_signin_days = data.continuous_signin_days;
                }
                showToast(data.message || '签到成功！');
                await loadHomeData();
            } catch (error) {
                showToast('签到失败: ' + error.message);
            } finally {
                loading.value = false;
            }
        }

        // ==================== 学习相关 ====================

        // 词性中文名（学生看得懂）
        const POS_NAMES = {
            'n.': '名词', 'v.': '动词', 'adj.': '形容词', 'adv.': '副词',
            'pron.': '代词', 'prep.': '介词', 'conj.': '连词', 'num.': '数词',
            'det.': '限定词', 'art.': '冠词', 'interj.': '感叹词',
            'phr.': '短语', 'v.phr.': '动词短语', 'modal v.': '情态动词',
            'abbr.': '缩写',
        };

        function posText(pos) {
            if (!pos) return '';
            return String(pos)
                .replace(/&/g, '/')
                .split('/')
                .map(p => p.trim())
                .filter(Boolean)
                .map(p => (POS_NAMES[p] ? `${p} ${POS_NAMES[p]}` : p))
                .join(' / ');
        }

        // 词形变化展示项
        const FORM_LABELS = {
            plural: '复数',
            third: '第三人称单数',
            ing: '现在分词',
            past: '过去式',
            pp: '过去分词',
            comparative: '比较级',
            superlative: '最高级',
        };

        const formItems = computed(() => {
            const forms = (currentWord.value && currentWord.value.word_forms) || {};
            const irr = (currentWord.value && currentWord.value.irregular_forms) || {};
            return Object.keys(FORM_LABELS)
                .filter(k => forms[k])
                .map(k => ({ key: k, label: FORM_LABELS[k], value: forms[k], irregular: !!irr[k] }));
        });

        // 例句里高亮目标词（含各种词形）
        const highlightExample = computed(() => {
            const w = currentWord.value;
            if (!w || !w.example_sentence) return '';
            const escapeHtml = s => String(s)
                .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
            const text = escapeHtml(w.example_sentence);

            const forms = new Set();
            const base = (w.word || '').trim();
            if (base) forms.add(base);
            const f = w.word_forms || {};
            Object.values(f).forEach(v => {
                if (typeof v !== 'string') return;
                v.split('/').forEach(x => {
                    const t = x.trim().replace(/^(more|most)\s+/i, '');
                    if (t) forms.add(t);
                });
            });
            const pattern = [...forms]
                .sort((a, b) => b.length - a.length)
                .map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))
                .join('|');
            if (!pattern) return text;
            try {
                return text.replace(new RegExp(`(?<![A-Za-z])(${pattern})(?![A-Za-z])`, 'gi'),
                    '<b class="hit-word">$1</b>');
            } catch (e) {
                // 老浏览器不支持后行断言时退回 \b
                return text.replace(new RegExp(`\\b(${pattern})\\b`, 'gi'), '<b class="hit-word">$1</b>');
            }
        });

        // 音频：复用一个元素，进入学习页时用用户手势解锁自动播放
        let audioEl = null;
        let audioUnlocked = false;
        const SILENT_WAV = 'data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=';

        function getAudioEl() {
            if (!audioEl) {
                audioEl = new Audio();
                audioEl.preload = 'auto';
            }
            return audioEl;
        }

        function unlockAudio() {
            if (audioUnlocked) return;
            try {
                const a = getAudioEl();
                a.src = SILENT_WAV;
                a.volume = 0;
                const p = a.play();
                const reset = () => { try { a.pause(); a.volume = 1; } catch (e) {} };
                if (p && typeof p.then === 'function') p.then(reset).catch(() => { a.volume = 1; });
                else reset();
                audioUnlocked = true;
            } catch (e) {
                console.warn('音频解锁失败:', e);
            }
        }

        // 自动跳转计时器（答对后播完例句再进下一题）
        let advanceTimer = null;
        function clearAdvance() {
            if (advanceTimer) {
                clearTimeout(advanceTimer);
                advanceTimer = null;
            }
        }
        function scheduleAdvance(delay) {
            clearAdvance();
            advanceTimer = setTimeout(() => {
                advanceTimer = null;
                nextWord();
            }, delay);
        }

        function startLearning() {
            unlockAudio();          // 必须在点击手势内解锁，否则自动朗读会被浏览器拦截
            currentPage.value = 'learning';
            loadLearningTasks();
        }

        async function handleOptionClick(option) {
            if (showResult.value) return;

            selectedOption.value = option;
            isCorrect.value = option.text === currentWord.value.meaning;
            showResult.value = true;

            const task = currentWord.value;
            const answeredKey = task.word_id;
            const isReviewTask = task.taskType === 'review' || task.type === 'review';

            // 答对立刻朗读例句：在请求之前触发，保住用户手势（移动端关键）
            let audioDone = null;
            const exampleText = currentWord.value.example_sentence;
            if (isCorrect.value && exampleText) {
                audioDone = playAudio(exampleText).catch(() => false);
            }

            try {
                const score = isCorrect.value ? 100 : 0;
                let result;
                if (isReviewTask) {
                    // 复习任务必须走错题复习接口：更新错题状态、下次复习日期、今日复习数
                    result = await submitReview(task.id, score);
                } else {
                    result = await submitQuiz(
                        task.word_id,
                        score,
                        isCorrect.value,
                        option.text  // 发送选中的选项文本供后端验证
                    );
                }

                // 积分实时反馈
                const delta = typeof result.score_change === 'number' ? result.score_change : 0;
                if (typeof result.user_total_score === 'number') {
                    profile.total_score = result.user_total_score;
                } else if (delta) {
                    profile.total_score = Math.round((profile.total_score + delta) * 10) / 10;
                }
                if (typeof result.daily_points === 'number') {
                    profile.today_points = result.daily_points;
                }
                if (delta) {
                    showToast(`${isCorrect.value ? '答对' : '答错'} ${delta > 0 ? '+' : ''}${delta} 积分`);
                }
            } catch (error) {
                console.error('提交结果失败:', error);
                showToast('提交失败: ' + error.message);
            }

            // 答对：例句播完自动下一题（也可以手动点"下一题"）
            if (isCorrect.value) {
                if (audioDone) {
                    audioDone.then(() => {
                        // 播放过程中用户可能已手动翻页，避免重复跳转
                        if (currentWord.value && currentWord.value.word_id === answeredKey) {
                            scheduleAdvance(400);
                        }
                    });
                } else {
                    scheduleAdvance(700);
                }
            }
        }

        // 手动跳转下一个单词
        async function nextWord() {
            clearAdvance();
            if (currentWordIndex.value < todayTasks.value.length - 1) {
                currentWordIndex.value++;
                await loadNextWord();
            } else {
                showToast('学习完成！🎉');
                currentPage.value = 'home';
                loadHomeData();
            }
        }

        async function playAudio(text) {
            if (!text) return false;
            const el = getAudioEl();
            isPlayingAudio.value = true;

            try {
                el.pause();
                el.volume = 1;
                el.src = audioUrl(text);
                // 直接 play()：保留用户手势，移动端不会因异步等待而丢掉播放权限
                await el.play();

                await new Promise(resolve => {
                    let done = false;
                    const fin = () => { if (!done) { done = true; resolve(); } };
                    el.onended = fin;
                    el.onerror = fin;
                    setTimeout(fin, 30000);
                });
                audioFailed.value = false;
                return true;
            } catch (error) {
                console.warn('音频播放失败:', error && error.name, error && error.message);
                if (error && error.name === 'NotAllowedError') {
                    audioFailed.value = true;   // 被浏览器拦截，提示用户点喇叭
                }
            } finally {
                isPlayingAudio.value = false;
            }

            // 兜底：浏览器语音合成
            try {
                if (!('speechSynthesis' in window)) return false;
                speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'en-US';
                utterance.rate = 0.9;
                utterance.pitch = 1.0;
                utterance.volume = 1.0;
                const voices = speechSynthesis.getVoices();
                const englishVoice = voices.find(v => v.lang.startsWith('en') && v.name.includes('Female')) ||
                                     voices.find(v => v.lang.startsWith('en'));
                if (englishVoice) utterance.voice = englishVoice;
                isPlayingAudio.value = true;
                return await new Promise(resolve => {
                    utterance.onend = () => resolve(true);
                    utterance.onerror = () => resolve(false);
                    speechSynthesis.speak(utterance);
                });
            } catch (error) {
                console.error('播放音频失败:', error);
                return false;
            } finally {
                isPlayingAudio.value = false;
            }
        }

        function replayExample() {
            const w = currentWord.value;
            if (w && w.example_sentence) playAudio(w.example_sentence);
        }


        // ==================== 词库相关 ====================

        // 点击切换选择词库
        function toggleLibrary(libId) {
            const idx = selectedLibraries.value.indexOf(libId);
            if (idx >= 0) {
                selectedLibraries.value.splice(idx, 1);
            } else {
                selectedLibraries.value.push(libId);
            }
        }

        async function saveSelectedLibraries() {
            loading.value = true;
            try {
                await saveUserLibraries(selectedLibraries.value);
                showToast('保存成功！');
                currentPage.value = 'home';
                await loadHomeData();
            } catch (error) {
                showToast('保存失败: ' + error.message);
            } finally {
                loading.value = false;
            }
        }

        // ==================== 设置相关 ====================

        async function saveDailyGoal() {
            const goal = Math.round(Number(editingDailyGoal.value) || 0);
            if (goal < 1 || goal > 200) {
                showToast('每日目标需在 1~200 之间');
                return;
            }
            loading.value = true;
            try {
                const result = await updateDailyGoal(goal);
                profile.daily_goal = result.daily_goal || goal;
                editingDailyGoal.value = profile.daily_goal;
                // 目标变了，今日任务配额也跟着变，刷新一下
                const todayLearning = await getTodayLearning();
                Object.assign(todayData, todayLearning);
                showToast('保存成功！');
            } catch (error) {
                showToast('保存失败: ' + error.message);
            } finally {
                loading.value = false;
            }
        }

        // ==================== 错题本 ====================

        async function loadWrongBook() {
            wrongLoading.value = true;
            try {
                const status = wrongFilter.value === 'all' ? null : wrongFilter.value;
                const [list, stats] = await Promise.all([getWrongQuestions(status), getWrongStats()]);
                wrongList.value = list || [];
                Object.assign(wrongStats, stats || {});
            } catch (error) {
                showToast('加载错题本失败: ' + error.message);
            } finally {
                wrongLoading.value = false;
            }
        }

        async function openWrongBook() {
            currentPage.value = 'wrongbook';
            await loadWrongBook();
        }

        function setWrongFilter(filter) {
            wrongFilter.value = filter;
            loadWrongBook();
        }

        // 把错题转换成学习页能消费的任务结构
        function wrongToTask(q) {
            return {
                type: 'review',
                taskType: 'review',
                id: q.id,                 // 错题记录 id，提交复习用这个
                wrong_question_id: q.id,
                word_id: q.word_id,
                word: q.word,
                phonetic: q.phonetic,
                meaning: q.meaning,
                example_sentence: '',
                wrong_count: q.wrong_count,
                correct_count: q.correct_count,
                familiarity: q.familiarity,
            };
        }

        function startReviewList(items) {
            if (!items.length) {
                showToast('没有可复习的错题');
                return;
            }
            unlockAudio();
            clearAdvance();
            todayTasks.value = items.map(wrongToTask);
            currentWordIndex.value = 0;
            currentPage.value = 'learning';
            loadNextWord();
        }

        function startReviewOne(q) {
            startReviewList([q]);
        }

        function startReviewAll() {
            const items = wrongList.value.filter(q => q.status === 'reviewing');
            // 全部复习时不受"今天到期"限制，主动复习也是有效的
            startReviewList(items);
        }

        function startReviewDue() {
            const items = wrongList.value.filter(q => q.is_due);
            startReviewList(items);
        }

        async function removeWrongQuestion(q) {
            if (!window.confirm(`确定从错题本删除「${q.word}」？删除后不再出现在复习里。`)) return;
            try {
                await deleteWrongQuestion(q.id);
                showToast('已删除');
                await loadWrongBook();
                await loadHomeData();
            } catch (error) {
                showToast('删除失败: ' + error.message);
            }
        }

        // ==================== 返回 ====================

        return {
            // 状态
            currentPage,
            loading,
            networkError,
            currentUser,
            profile,
            loginForm,
            registerForm,
            resetForm,
            showRegister,
            showResetPassword,
            todayData,
            editingDailyGoal,
            systemLibraries,
            selectedLibraries,
            currentWord,
            currentOptions,
            currentWordIndex,
            todayTasks,
            showResult,
            selectedOption,
            isCorrect,
            isPlayingAudio,
            toast,
            wrongList,
            wrongFilter,
            wrongLoading,
            wrongStats,

            // 方法
            handleLogin,
            handleRegister,
            handleResetPassword,
            handleLogout,
            handleSignIn,
            startLearning,
            handleOptionClick,
            nextWord,
            playAudio,
            audioFailed,
            replayExample,
            posText,
            formItems,
            highlightExample,
            toggleLibrary,
            saveSelectedLibraries,
            saveDailyGoal,
            openWrongBook,
            loadWrongBook,
            setWrongFilter,
            startReviewOne,
            startReviewAll,
            startReviewDue,
            removeWrongQuestion,
        };
    },
});

// 挂载应用
app.mount('#app');
