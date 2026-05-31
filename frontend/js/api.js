// API 通信模块

/**
 * 通用 API 请求函数
 */
async function api(endpoint, options = {}) {
    const token = localStorage.getItem(CONFIG.TOKEN_KEY);
    const headers = {
        'Content-Type': 'application/json',
    };
    
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    
    try {
        const res = await fetch(`${CONFIG.API_BASE}${endpoint}`, {
            ...options,
            headers: { ...headers, ...options.headers },
        });
        
        if (!res.ok) {
            const err = await res.json().catch(() => ({ detail: '请求失败' }));
            throw new Error(err.detail || '请求失败');
        }
        
        return await res.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// ==================== 认证相关 ====================

/**
 * 用户登录
 */
async function login(username, password) {
    // OAuth2PasswordRequestForm 需要 form-data 格式，不是 JSON
    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);
    
    const data = await api('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString(),
    });
    
    if (data.access_token) {
        localStorage.setItem(CONFIG.TOKEN_KEY, data.access_token);
        localStorage.setItem(CONFIG.USER_KEY, JSON.stringify(data.user));
    }
    
    return data;
}

/**
 * 用户注册
 */
async function register(formData) {
    return await api('/auth/register', {
        method: 'POST',
        body: JSON.stringify(formData),
    });
}

/**
 * 获取当前用户信息
 */
async function getCurrentUser() {
    return await api('/auth/me');
}

/**
 * 重置密码
 */
async function resetPassword(username, phone, email, newPassword) {
    return await api('/auth/reset-password', {
        method: 'POST',
        body: JSON.stringify({
            username,
            phone: phone || undefined,
            email: email || undefined,
            new_password: newPassword,
        }),
    });
}

/**
 * 退出登录
 */
function logout() {
    localStorage.removeItem(CONFIG.TOKEN_KEY);
    localStorage.removeItem(CONFIG.USER_KEY);
}

// ==================== 词库相关 ====================

/**
 * 获取系统词库列表
 */
async function getSystemLibraries() {
    return await api('/libraries/system');
}

/**
 * 获取用户已选择的词库
 */
async function getUserLibraries() {
    return await api('/libraries');
}

/**
 * 保存用户选择的词库
 */
async function saveUserLibraries(libraryIds) {
    return await api('/records/profile', {
        method: 'PUT',
        body: JSON.stringify({ selected_library_ids: libraryIds }),
    });
}

// ==================== 学习相关 ====================

/**
 * 获取今日学习任务
 */
async function getTodayLearning() {
    return await api('/learning/today');
}

/**
 * 获取测验选项
 */
async function getQuizOptions(wordId) {
    return await api(`/learning/quiz-options?word_id=${encodeURIComponent(wordId)}`);
}

/**
 * 提交学习结果
 */
async function submitQuiz(wordId, score, isCorrect, selectedMeaning) {
    return await api('/learning/submit-quiz', {
        method: 'POST',
        body: JSON.stringify({
            word_id: wordId,
            score,
            is_correct: isCorrect,
            selected_meaning: selectedMeaning,
        }),
    });
}

/**
 * 提交错题复习结果
 */
async function submitReview(wordId, isCorrect) {
    return await api('/learning/review', {
        method: 'POST',
        body: JSON.stringify({
            word_id: wordId,
            is_correct: isCorrect,
        }),
    });
}

/**
 * 每日签到
 */
async function dailySignIn() {
    return await api('/learning/signin', {
        method: 'POST',
    });
}

// ==================== 用户数据 ====================

/**
 * 获取用户学习资料
 */
async function getUserProfile() {
    return await api('/records/profile');
}

/**
 * 获取学习统计
 */
async function getUserStats() {
    return await api('/records/stats');
}

/**
 * 更新每日目标
 */
async function updateDailyGoal(goal) {
    return await api('/records/daily-goal', {
        method: 'POST',
        body: JSON.stringify({ daily_goal: goal }),
    });
}

// ==================== 错题本相关 ====================

/**
 * 获取错题列表
 */
async function getWrongQuestions() {
    return await api('/wrong-questions');
}

/**
 * 获取今日待复习的错题
 */
async function getDueWrongQuestions() {
    return await api('/wrong-questions/due-today');
}

/**
 * 删除错题
 */
async function deleteWrongQuestion(wordId) {
    return await api(`/wrong-questions/${wordId}`, {
        method: 'DELETE',
    });
}