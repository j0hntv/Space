import argparse
import os
import requests


def fetch_spacex_last_launch(path):
    os.makedirs(path, exist_ok=True)
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url).json()
    images_url = response['links']['flickr_images']

    print(f'Downloads {len(images_url)} images:')

    for num, image_url in enumerate(images_url, start=1):
        name = f'SpaceX_{num}.jpg'
        print(f'{num}. {name}...', end=' ')
        image = requests.get(image_url).content
        with open(f'{path}/{name}', 'wb') as file:
            file.write(image)
            print('Ok.')
    
    print('Done.')


def main():
    parser = argparse.ArgumentParser(description='Downloading photos of the latest launch SpaceX')
    parser.add_argument('path', help='Path to save images')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.path)


if __name__ == '__main__':
    main()
