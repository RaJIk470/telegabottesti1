from config import dp, database, bot
import asyncio
from asyncio import sleep, get_event_loop
from aiogram import types
def add_user(user):
	first, last, username, user_id = user.first_name, user.last_name, user.username, user.id
	database.add_user(first, last, username, user_id)

@dp.message_handler(commands=['start'])
async def send_message(message):
	add_user(message.from_user)
	await message.reply("Поздравляем! Вы внесены в базу данных бота!")

@dp.message_handler(commands=['dai'])	
async def get_database(message):
	if message.from_user.username == "RaJIk470":
		print(database.get_table())
	await bot.send_message(message.chat.id, "вс бро")

'''@dp.message_handler()
async def spam_off(message):
	print(message.from_user)
	if message.from_user.id == 1573724826 and len(message.text) > 30:
		await bot.delete_message(message.chat.id, message.message_id)'''



"""@dp.message_handler(content_types= ['sticker'])	
async def echo_stickers(message):
	print(message.from_user)
	add_user(message.from_user)
	#await bot.send_message(message.chat.id, message.sticker.file_id)
	await bot.send_sticker(message.chat.id, message.sticker.file_id)"""

@dp.message_handler(commands=['repit'])	
async def spam(message):
	wordList = message.text.split()
	if len(wordList) == 1:
		await bot.send_message(message.chat.id, "бро а чо пофтарять мож скажеш не?")
	else:
		if wordList[len(wordList) - 1].isnumeric() and len(wordList) > 2:
			msg, count = (wordList)[1: len(wordList) - 1], (wordList)[len(wordList) - 1]
			msg = ' '.join(msg)
			count = int(count)
		else:
			msg = ' '.join((wordList)[1:])
			count = 1
		for i in range(count):
			await asyncio.sleep(5)
			await bot.send_message(message.chat.id, msg)

@dp.message_handler(commands=['repitaftr'])	
async def repitaftr(message):
	wordList = message.text.split()
	if len(wordList) < 3:
		await bot.send_message(message.chat.id, "бро пиши чо пофтарять и через скока а то непанятн ваще ты такой тупой")
	else:
		wordList = wordList[1:]
		msg, aftr = ' '.join(wordList[0:len(wordList) - 1]), float(wordList[len(wordList) - 1])
		await asyncio.sleep(aftr * 60)
		await bot.send_message(message.chat.id, msg)
	

@dp.message_handler(content_types=types.ContentType.ANY)	
async def echo(message):
	add_user(message.from_user)
	print(message)
	await asyncio.sleep(1)