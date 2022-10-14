from backend.internal.db.db import DB
from backend.internal.db.parser import parse_faqs
from backend.internal.service.service_impl import FAQServiceImpl
from frontend.bot import Bot

DB_FILEPATH = "faq.json"
TOKEN_FILEPATH = "token.txt"

db = DB(parse_faqs(DB_FILEPATH))
service = FAQServiceImpl(db)
token = ""
with open("token.txt") as f:
    token = f.readline().strip()
bot = Bot(token, service)
bot.start()

