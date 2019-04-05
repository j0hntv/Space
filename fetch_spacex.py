import os
import requests

def fetch_spacex_last_launch(path):
    url = 'https://api.spacexdata.com/v3/launches/latest'
    if not os.path.exists(path):
        os.mkdir(path)

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


if __name__ == '__main__':
    fetch_spacex_last_launch('images')
