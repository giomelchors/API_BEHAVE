import os
from dotenv import load_dotenv


load_dotenv(".env")

URL_PAGE = os.getenv('URL_PAGE')
EMAIL_USER = os.getenv('USER_EMAIL')
PASSWORD_USER = os.getenv('PASSWORD')