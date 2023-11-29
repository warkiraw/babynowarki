from django.core.management.base import BaseCommand
from mywarki.models import Product
import telebot
bot = telebot.TeleBot("6441802059:AAHCv8NGXxvUZZR1zhpPvzNSfFvB0FI-KSk") # Вставьте сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Hello world!")
@bot.message_handler(commands=['products'])
def products(message):
	products = Product.objects.all()
	for product in products:
		bot.send_message(message.chat.id, product.name)
class Command(BaseCommand):
	def handle(self, *args, **options):
		print("Starting bot...")
		bot.polling()
		print("Bot stopped")
#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)
@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, 'Привет вот мои функции:\n'
						'/start - запуск бота\n'
						'/bio - моя биография\n'
						'/help - список команд\n'
						'/exit - выход'
	)
@bot.message_handler(commands=['bio'])
def bio(message):
	bot.send_message(message.chat.id,"Меня зовут Рустам Итаков и я создатель этого бота")
@bot.message_handler(commands=['exit'])
def exit(message):
	bot.send_message(message.chat.id,'Change the world...\n'
					'My final message...\n'
					'Goodbye...'
	)
	bot.stop_polling()
@bot.message_handler(commands=['marina'])
def marina(message):
	bot.send_message(message.chat.id,"Марина самая красивая,и я ее очень сильно люблю,она самая самая лучшая")
