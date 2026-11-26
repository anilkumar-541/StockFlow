import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
FRONTEND_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173,https://stockflow-gold-ten.vercel.app",
    ).split(",")
    if origin.strip()
]
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)
print(FRONTEND_ORIGINS)

if JWT_ACCESS_TOKEN_EXPIRE_MINUTES < 1:
    raise ValueError("JWT_ACCESS_TOKEN_EXPIRE_MINUTES must be greater than zero.")