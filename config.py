import os
from dotenv import load_dotenv
load_dotenv()
KEY_PASS=os.getenv("PUSHPLUS_KEY")
URL_KEY=os.getenv("URL_PASS")

#数据库
DB_NAME="ling.db"
