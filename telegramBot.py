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
    def join_group(self, invite_link):
        try:
            group_id = self._parse_invite_link(invite_link)
            if group_id:
                self.bot.send_message(group_id, "Hello! I've joined this group.")
                self.group_ids.append(group_id)
                print(f"Bot has joined group with ID {group_id}")
            else:
                print("Invalid invite link.")

        except telebot.apihelper.ApiTelegramException as e:
            print(f"Failed to join group using invite link: {e}")

    def _parse_invite_link(self, invite_link):
        # Regular expression to extract group ID from the invite link
        pattern = re.compile(r'https:\/\/t\.me\/\+(\w+)')

        match = re.match(pattern, invite_link)
        if match:
            return match.group(1)
        else:
            return None
    def start_polling(self):
        self.bot.polling(none_stop=True)