import os
from dotenv import load_dotenv

load_dotenv('/etc/secrets/.env')

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LITERARY_API_KEY = os.getenv("LITERARY_API_KEY")
FACEBOOK_API_KEY = os.getenv("FACEBOOK_API_KEY")
FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
