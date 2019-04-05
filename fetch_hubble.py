import os
import requests


def fetch_hubble_by_id(path, image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url).json()
    images_url = [image_file['file_url'] for image_file in response['image_files']]
    best_image_url = images_url[-1]
    name = f'{image_id}.{get_url_extension(best_image_url)}'
    print(f'{name}...', end=' ')
    image = requests.get(best_image_url).content
    with open(f'{path}/{name}', 'wb') as file:
        file.write(image)
        print('Ok.')
        

def fetch_hubble_by_collection(path, collection):
    url_collection = f'http://hubblesite.org/api/v3/images/{collection}'
    response = requests.get(url_collection).json()
    images_id = [image['id'] for image in response]

    if not os.path.exists(path):
        os.mkdir(path)
        
    print(f'Downloads {len(images_id)} images:')

    for num, image_id in enumerate(images_id, start=1):
        fetch_hubble_by_id(path, image_id)
    
    print('Done.')


def get_url_extension(url):
    return url.split('.')[-1]


def main():
    collection = 'holiday_cards'
    fetch_hubble_by_collection('images', collection)


if __name__ == '__main__':
    main()
    

