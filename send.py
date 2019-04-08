import argparse
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


def main():
    load_dotenv()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    parser = argparse.ArgumentParser(description='Posting to Instagram')
    parser.add_argument('path', help='Path to images')
    args = parser.parse_args()
    path = args.path
    send_foto(path, username, password)

if __name__ == '__main__':
    main()


