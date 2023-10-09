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
    def join_group(self, group_id):
        try:
            self.bot.get_chat(group_id)  # Check if the bot can access the group
            self.group_ids.append(group_id)
            print(f"Bot has joined group with ID {group_id}")
        except telebot.apihelper.ApiTelegramException as e:
            print(f"Failed to join group with ID {group_id}: {e}")
    def start_polling(self):
        self.bot.polling(none_stop=True)