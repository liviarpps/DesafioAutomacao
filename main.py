from supabase import create_client
from dotenv import load_dotenv

import requests
import os

load_dotenv()

supabase= create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY"),
)