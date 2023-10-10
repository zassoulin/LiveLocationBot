import re

import telebot


class TelegramBot:
    def __init__(self, api_token):
        self.bot = telebot.TeleBot(api_token)
        self.group_ids = []  # List to store the group IDs this bot is a member of
        self._register_handlers()

    def _register_handlers(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_messages(message):
            chat_id = message.chat.id
            message_text = message.text
            print(f"Received message from chat ID {chat_id}: {message_text}")
        @self.bot.channel_post_handler(func=lambda message: True)
        def handle_channel_posts(message):
            chat_id = message.chat.id
            message_text = message.text
            print(f"Received message in channel {chat_id}: {message_text}")
    def start_polling(self):

        self.bot.polling(none_stop=True)