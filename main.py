from telegramBot import TelegramBot

if __name__ == '__main__':
    import yaml

    with open('config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    api_token = config.get('telegram_api_token')

    if api_token is None:
        raise ValueError('Telegram API token not found in the configuration file')

    telegramBot = TelegramBot(api_token)
    # telegramBot.join_group(-1001397114707)
    # telegramBot.join_group(-1001908727000)
    invite_link = 'https://t.me/+wECw9MIc53AwMTI0'
    telegramBot.join_group(invite_link)
    telegramBot.start_polling()
    while True:
        pass
