from telegramBot import TelegramBot

if __name__ == '__main__':
    import yaml

    with open('config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    api_token = config.get('telegram_api_token')

    if api_token is None:
        raise ValueError('Telegram API token not found in the configuration file')

    telegramBot = TelegramBot(api_token)
