// Vue 应用主模块

const { createApp, ref, reactive, onMounted, computed } = Vue;

// 创建 Vue 应用
const app = createApp({
    setup() {
        // ==================== 状态管理 ====================
        
        // 当前页面
        const currentPage = ref('login');
        
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
        
        // Toast 提示
        const toast = reactive({
            show: false,
            message: '',
        });
        
        // ==================== 工具函数 ====================
        
        // 显示 Toast
        function showToast(msg) {
            toast.message = msg;
            toast.show = true;
            setTimeout(() => {
                toast.show = false;
            }, 2000);
        }
        
        // ==================== 生命周期 ====================
        
        onMounted(async () => {
            // 检查是否已登录
            const token = localStorage.getItem(CONFIG.TOKEN_KEY);
            const userStr = localStorage.getItem(CONFIG.USER_KEY);
            
            if (token && userStr) {
                try {
                    const user = JSON.parse(userStr);
                    currentUser.value = user;
                    currentPage.value = 'home';
                    
                    // 加载首页数据
                    await loadHomeData();
                } catch (e) {
                    console.error('登录状态恢复失败:', e);
                    logout();
                }
            }
        });
        
        // ==================== 数据加载 ====================
        
        // 加载首页数据
        async function loadHomeData() {
            try {
                // 获取用户资料
                const profileData = await getUserProfile();
                Object.assign(profile, profileData);
                editingDailyGoal.value = profileData.daily_goal || 10;
                
                // 获取今日学习任务
                const todayLearning = await getTodayLearning();
                Object.assign(todayData, todayLearning);
                
                // 获取词库列表
                const libraries = await getSystemLibraries();
                systemLibraries.value = libraries;
                
                // 获取用户已选择的词库（从profile中获取）
                selectedLibraries.value = profileData.selected_library_ids || [];
                
            } catch (error) {
                console.error('加载数据失败:', error);
                showToast('加载数据失败: ' + error.message);
            }
        }
        
        // 加载学习任务
        async function loadLearningTasks() {
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
                console.error('加载学习任务失败:', error);
                showToast('加载学习任务失败');
            }
        }
        
        // 加载下一个单词
        async function loadNextWord() {
            if (currentWordIndex.value >= todayTasks.value.length) {
                showToast('学习完成！');
                currentPage.value = 'home';
                await loadHomeData();
                return;
            }
            
            const task = todayTasks.value[currentWordIndex.value];
            currentWord.value = task;
            showResult.value = false;
            selectedOption.value = null;
            
            // 获取测验选项
            try {
                const options = await getQuizOptions(task.word_id);
                currentOptions.value = options.options || [];
            } catch (error) {
                console.error('加载选项失败:', error);
                showToast('加载选项失败');
            }
            
            // 自动播放单词读音（选项加载完成后播放）
            playAudio(task.word).catch(err => console.error('自动播放失败:', err));
        }
        
        // ==================== 登录注册 ====================
        
        async function handleLogin() {
            if (!loginForm.username || !loginForm.password) {
                showToast('请填写用户名和密码');
                return;
            }
            
            try {
                await login(loginForm.username, loginForm.password);
                const userStr = localStorage.getItem(CONFIG.USER_KEY);
                currentUser.value = JSON.parse(userStr);
                currentPage.value = 'home';
                showToast('登录成功！');
                await loadHomeData();
            } catch (error) {
                showToast('登录失败: ' + error.message);
            }
        }
        
        async function handleRegister() {
            if (!registerForm.name || !registerForm.password) {
                showToast('请填写姓名和密码');
                return;
            }
            
            try {
                await register(registerForm);
                showToast('注册成功，请登录！');
                showRegister.value = false;
                loginForm.username = '';
                loginForm.password = '';
            } catch (error) {
                showToast('注册失败: ' + error.message);
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
            }
        }
        
        function handleLogout() {
            logout();
            currentUser.value = null;
            currentPage.value = 'login';
            showToast('已退出登录');
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
            
            // 提交学习结果
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
                // 答对：播放例句（如果有的话，没有就用单词）
                const exampleText = currentWord.value.example_sentence || currentWord.value.word;
                
                // 等待一小段时间后播放例句
                await new Promise(resolve => setTimeout(resolve, 300));
                
                try {
                    // 播放例句，等待播放完成
                    await playAudio(exampleText);
                } catch (error) {
                    console.error('播放例句失败:', error);
                }
                
                // 自动跳转到下一个单词
                if (currentWordIndex.value < todayTasks.value.length - 1) {
                    nextWord();
                } else {
                    showToast('学习完成！');
                    currentPage.value = 'home';
                    loadHomeData();
                }
            } else {
                // 答错：给用户时间看正确答案，不自动跳转
                // 用户需要手动点击"下一题"
            }
        }
        
        function nextWord() {
            currentWordIndex.value++;
            loadNextWord();
        }
        
        async function playAudio(text) {
            // 优先使用后端 Edge TTS（更稳定，支持手机端）
            try {
                const audio = new Audio();
                audio.src = `${CONFIG.API_BASE}/tts?text=${encodeURIComponent(text)}`;
                audio.crossOrigin = "anonymous";
                
                // 1. 等待音频加载完成
                await new Promise((resolve, reject) => {
                    audio.oncanplaythrough = resolve;
                    audio.onerror = (e) => reject(new Error('音频加载失败'));
                    audio.load();
                });
                
                // 2. 开始播放
                await audio.play();
                
                // 3. 等待音频播放完成
                await new Promise((resolve) => {
                    audio.onended = resolve;
                });
                
                return; // 播放成功则退出
            } catch (error) {
                console.error('后端 TTS 播放失败:', error);
            }
            
            // 如果后端 TTS 失败，尝试 Web Speech API（作为后备）
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
                    
                    return new Promise((resolve, reject) => {
                        utterance.onend = () => resolve();
                        utterance.onerror = (e) => {
                            console.error('Web Speech API 错误:', e);
                            reject(e);
                        };
                        speechSynthesis.speak(utterance);
                    });
                }
            } catch (error) {
                console.error('播放音频失败:', error);
            }
        }
        
        // ==================== 词库相关 ====================
        
        async function saveSelectedLibraries() {
            try {
                await saveUserLibraries(selectedLibraries.value);
                showToast('保存成功！');
                currentPage.value = 'home';
                await loadHomeData();
            } catch (error) {
                showToast('保存失败: ' + error.message);
            }
        }
        
        // ==================== 设置相关 ====================
        
        async function saveDailyGoal() {
            try {
                await updateDailyGoal(editingDailyGoal.value);
                profile.daily_goal = editingDailyGoal.value;
                showToast('保存成功！');
            } catch (error) {
                showToast('保存失败: ' + error.message);
            }
        }
        
        // ==================== 返回 ====================
        
        return {
            // 状态
            currentPage,
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
            toast,
            
            // 方法
            handleLogin,
            handleRegister,
            handleResetPassword,
            handleLogout,
            startLearning,
            handleOptionClick,
            nextWord,
            playAudio,
            saveSelectedLibraries,
            saveDailyGoal,
        };
    },
});

// 挂载应用
app.mount('#app');