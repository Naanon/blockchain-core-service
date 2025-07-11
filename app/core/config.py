import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    NODE_PROVIDER_URL: str = os.getenv("NODE_PROVIDER_URL")

settings = Settings()