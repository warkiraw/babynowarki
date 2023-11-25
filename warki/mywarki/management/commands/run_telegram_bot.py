from django.core.management.base import BaseCommand

import telebot
bot = telebot.TeleBot("6441802059:AAHCv8NGXxvUZZR1zhpPvzNSfFvB0FI-KSk") # Вставьте сюда свой токен

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")