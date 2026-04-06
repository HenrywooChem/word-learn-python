import requests

# 测试登录
url = "http://localhost:8000/api/auth/login"
data = {
    "username": "testuser999",
    "password": "test123"
}

# 使用 form data 格式
response = requests.post(url, data=data)
print(f"Login Status: {response.status_code}")
print(f"Login Response: {response.text}")

if response.status_code == 200:
    token = response.json()["access_token"]
    print(f"\nToken: {token[:50]}...")
    
    # 测试 /records/profile
    profile_response = requests.get(
        "http://localhost:8000/api/records/profile",
        headers={"Authorization": f"Bearer {token}"}
    )
    print(f"\nProfile Status: {profile_response.status_code}")
    print(f"Profile Response: {profile_response.text}")
