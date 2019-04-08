import os
from time import sleep
from instabot import Bot
from dotenv import load_dotenv


def send_foto(path, username, password):
    bot = Bot()
    bot.login(username=username, password=password)

    images = os.listdir(path)

    for image in images:
        bot.upload_photo(f'{path}/{image}')
        if not bot.api.last_response.ok:
            print(bot.api.last_response)


def main():
    load_dotenv()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    send_foto('images', username, password)

if __name__ == '__main__':
    main()


