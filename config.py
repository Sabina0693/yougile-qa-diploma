import os

BASE_URL = "https://yougile.com/api-v2"

try:
    from local_settings import TOKEN
except ImportError:
    TOKEN = os.environ.get("YOUGILE_TOKEN")

try:
    from local_settings import EMAIL
except ImportError:
    EMAIL = os.environ.get("YOUGILE_EMAIL")

try:
    from local_settings import PASSWORD
except ImportError:
    PASSWORD = os.environ.get("YOUGILE_PASSWORD")
