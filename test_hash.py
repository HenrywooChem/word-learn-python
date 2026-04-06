# Test password hashing
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "test123"
print(f"Password: {password}")
print(f"Password length: {len(password)}")
print(f"Password bytes: {password.encode('utf-8')}")

try:
    hashed = pwd_context.hash(password)
    print(f"Hashed: {hashed}")
except Exception as e:
    print(f"Error: {e}")
