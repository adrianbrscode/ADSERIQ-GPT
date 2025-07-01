
from dotenv import load_dotenv
import os

load_dotenv()

open_api_key = os.getenv("OPEN_API_KEY")

if not open_api_key:
    raise ValueError("no exist clave")