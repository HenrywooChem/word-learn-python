import requests

# 登录获取 token
login_resp = requests.post(
    "http://localhost:8000/api/auth/login",
    data={"username": "testuser999", "password": "test123"}
)
print(f"Login: {login_resp.status_code}")
token = login_resp.json()["access_token"]
user_id = login_resp.json()["user"]["id"]

# 获取词库列表
libs_resp = requests.get(
    "http://localhost:8000/api/libraries?lib_type=system",
    headers={"Authorization": f"Bearer {token}"}
)
print(f"\nLibraries: {libs_resp.status_code}")
libs = libs_resp.json()
print(f"Found {len(libs)} libraries")

if libs:
    lib_id = libs[0]["id"]
    print(f"First library: {libs[0]['name']}")
    
    # 选择第一个词库
    profile_resp = requests.put(
        "http://localhost:8000/api/records/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={"selected_library_ids": [lib_id]}
    )
    print(f"\nSelect Library: {profile_resp.status_code}")
    
    # 获取今日学习任务
    today_resp = requests.get(
        "http://localhost:8000/api/learning/today",
        headers={"Authorization": f"Bearer {token}"}
    )
    print(f"\nToday Tasks: {today_resp.status_code}")
    data = today_resp.json()
    print(f"Tasks: {len(data.get('today_tasks', []))}")
    print(f"New count: {data.get('new_count', 0)}")
    
    if data.get('today_tasks'):
        task = data['today_tasks'][0]
        word_id = task['word_id']
        print(f"\nFirst task: {task['word']} ({word_id})")
        
        # 获取选择题选项
        quiz_resp = requests.get(
            f"http://localhost:8000/api/learning/quiz-options/{word_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        print(f"\nQuiz Options: {quiz_resp.status_code}")
        print(f"Response: {quiz_resp.json()}")
