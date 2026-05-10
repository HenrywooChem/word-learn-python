import requests

# Login first
login_resp = requests.post("http://localhost:8000/api/auth/login", json={"username": "test", "password": "test123"})
print("Login status:", login_resp.status_code)
if login_resp.status_code != 200:
    print("Login failed, trying to register...")
    reg_resp = requests.post("http://localhost:8000/api/auth/register", json={"username": "test_check", "password": "test123"})
    print("Register status:", reg_resp.status_code)
    login_resp = requests.post("http://localhost:8000/api/auth/login", json={"username": "test_check", "password": "test123"})

token = login_resp.json().get("access_token", "")
print("Token:", token[:50] if token else "NONE")

headers = {"Authorization": f"Bearer {token}"}
libs_resp = requests.get("http://localhost:8000/api/libraries?lib_type=system", headers=headers)
print(f"\nLibraries status: {libs_resp.status_code}")
libs = libs_resp.json()
print(f"Total libraries: {len(libs)}")
for lib in libs:
    words_count = len(lib.get("words", [])) if isinstance(lib.get("words"), list) else "?"
    print(f"  {lib['id']}: {lib['name']} ({words_count} words) | grade={lib.get('grade')}")
