// Vue 应用主模块

const { createApp, ref, reactive, onMounted } = Vue;

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

            try {
                const options = await getQuizOptions(task.word_id);
                currentOptions.value = options.options || [];
            } catch (error) {
                showToast('加载选项失败');
            }

            // 自动播放单词读音
            try {
                await playAudio(task.word);
            } catch (err) {
                console.error('自动播放失败:', err);
            }
        }

        // ==================== 生命周期 ====================

        onMounted(async () => {
            const token = localStorage.getItem(CONFIG.TOKEN_KEY);
            const userStr = localStorage.getItem(CONFIG.USER_KEY);

            if (token && userStr) {
                try {
                    const user = JSON.parse(userStr);
                    currentUser.value = user;
                    currentPage.value = 'home';
                    await loadHomeData();
                } catch (e) {
                    console.error('登录状态恢复失败:', e);
                    logout();
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
                profile.total_score += data.bonus_score || 0;
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

        function startLearning() {
            currentPage.value = 'learning';
            loadLearningTasks();
        }

        async function handleOptionClick(option) {
            if (showResult.value) return;

            selectedOption.value = option;
            isCorrect.value = option.text === currentWord.value.meaning;
            showResult.value = true;

            try {
                const score = isCorrect.value ? 100 : 0;
                await submitQuiz(
                    currentWord.value.word_id,
                    score,
                    isCorrect.value
                );
            } catch (error) {
                console.error('提交结果失败:', error);
            }

            // 答对时朗读例句，播放完成后自动跳转
            if (isCorrect.value) {
                const exampleText = currentWord.value.example_sentence || currentWord.value.word;

                await new Promise(resolve => setTimeout(resolve, 500));

                try {
                    await playAudio(exampleText);
                } catch (error) {
                    console.error('播放例句失败:', error);
                }

                await new Promise(resolve => setTimeout(resolve, 300));

                if (currentWordIndex.value < todayTasks.value.length - 1) {
                    currentWordIndex.value++;
                    await loadNextWord();
                } else {
                    showToast('学习完成！🎉');
                    currentPage.value = 'home';
                    loadHomeData();
                }
            }
        }

        // 手动跳转下一个单词（答错时使用）
        async function nextWord() {
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
            isPlayingAudio.value = true;
            // 优先使用后端 Edge TTS
            try {
                const audio = new Audio();
                audio.src = `${CONFIG.API_BASE}/tts?text=${encodeURIComponent(text)}`;
                audio.crossOrigin = "anonymous";

                await new Promise((resolve, reject) => {
                    audio.oncanplaythrough = resolve;
                    audio.onerror = () => reject(new Error('音频加载失败'));
                    audio.load();
                });

                await audio.play();

                await new Promise((resolve) => {
                    audio.onended = resolve;
                });

                return;
            } catch (error) {
                console.error('后端 TTS 播放失败:', error);
            }

            // 后端 TTS 失败，尝试 Web Speech API
            try {
                if ('speechSynthesis' in window) {
                    speechSynthesis.cancel();

                    const utterance = new SpeechSynthesisUtterance(text);
                    utterance.lang = 'en-US';
                    utterance.rate = 0.9;
                    utterance.pitch = 1.0;
                    utterance.volume = 1.0;

                    const voices = speechSynthesis.getVoices();
                    const englishVoice = voices.find(v => v.lang.startsWith('en') && v.name.includes('Female')) ||
                                         voices.find(v => v.lang.startsWith('en'));
                    if (englishVoice) {
                        utterance.voice = englishVoice;
                    }

                    return new Promise((resolve) => {
                        utterance.onend = () => resolve();
                        utterance.onerror = () => {
                            console.error('Web Speech API 错误');
                            resolve();
                        };
                        speechSynthesis.speak(utterance);
                    });
                }
            } catch (error) {
                console.error('播放音频失败:', error);
            } finally {
                isPlayingAudio.value = false;
            }
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
            loading.value = true;
            try {
                await updateDailyGoal(editingDailyGoal.value);
                profile.daily_goal = editingDailyGoal.value;
                showToast('保存成功！');
            } catch (error) {
                showToast('保存失败: ' + error.message);
            } finally {
                loading.value = false;
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
            toggleLibrary,
            saveSelectedLibraries,
            saveDailyGoal,
        };
    },
});

// 挂载应用
app.mount('#app');
