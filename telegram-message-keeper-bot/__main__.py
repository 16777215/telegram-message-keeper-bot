import telegram
import yaml


with open('resources/confidential.yml') as f1:
    confidential = yaml.safe_load(f1)


def main():
    bot = telegram.Bot(token=confidential['bot_token'])
    owner_id = confidential['bot_owner_id']

    bot.sendMessage(chat_id=owner_id, text="hello world via python!")


if __name__ == "__main__":
    main()
