from aiogram import Bot
import logging
from database import Database
from aiogram import Dispatcher, executor

API_TOKEN = "1660454722:AAGw5BcM7LfGXk0y1Iufqa6UyE5k2PaEp3c"

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)
database = Database('db.db')
#logging.basicConfig(level=logging.DEBUG)
