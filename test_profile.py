import requests

# 登录获取 token
login_resp = requests.post(
    "http://localhost:8000/api/auth/login",
    data={"username": "testuser999", "password": "test123"}
)
print(f"Login: {login_resp.status_code}")
token = login_resp.json()["access_token"]

# 测试保存词库选择
profile_resp = requests.put(
    "http://localhost:8000/api/records/profile",
    headers={"Authorization": f"Bearer {token}"},
    json={"selected_library_ids": ["lib1", "lib2"]}
)
print(f"Profile PUT: {profile_resp.status_code}")
print(f"Response: {profile_resp.text}")
