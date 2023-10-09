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
    def join_group(self, group_id):
        try:
            self.bot.get_chat(group_id)  # Check if the bot can access the group
            self.group_ids.append(group_id)
            print(f"Bot has joined group with ID {group_id}")
        except telebot.apihelper.ApiTelegramException as e:
            print(f"Failed to join group with ID {group_id}: {e}")
    def join_group_or_channel(self, invite_link):
        try:
            invite_info = self._parse_invite_link(invite_link)

            if invite_info['type'] == 'channel':
                self.bot.send_message(invite_info['id'], "Hello! I've joined this channel.")
                print(f"Bot has joined channel with ID {invite_info['id']}")
            elif invite_info['type'] == 'group':
                self.bot.send_message(invite_info['id'], "Hello! I've joined this group.")
                print(f"Bot has joined group with ID {invite_info['id']}")
            else:
                print("Invalid invite link.")

        except telebot.apihelper.ApiTelegramException as e:
            print(f"Failed to join using invite link: {e}")

    def _parse_invite_link(self, link):
        # Regular expressions to extract ID and type from the invite link
        channel_pattern = re.compile(r'https:\/\/t\.me\/joinchat\/([A-Za-z0-9_\-]+)')
        group_pattern = re.compile(r'https:\/\/t\.me\/joinchat\/([A-Za-z0-9_\-]+)')

        # Check if it's a channel or group invite link
        if re.match(channel_pattern, link):
            return {'type': 'channel', 'id': re.match(channel_pattern, link).group(1)}
        elif re.match(group_pattern, link):
            return {'type': 'group', 'id': re.match(group_pattern, link).group(1)}
        else:
            return {'type': None, 'id': None}
    def start_polling(self):
        self.bot.polling(none_stop=True)