import argparse
import os
import requests


def fetch_hubble_by_id(path, image_id):
    os.makedirs(path, exist_ok=True)
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url).json()
    images_url = [image_file['file_url'] for image_file in response['image_files']]
    best_image_url = images_url[-1]
    name = f'{image_id}.{get_url_extension(best_image_url)}'
    image = requests.get(best_image_url).content
    with open(f'{path}/{name}', 'wb') as file:
        file.write(image)
        

def fetch_hubble_by_collection(path, collection):
    os.makedirs(path, exist_ok=True)
    url_collection = f'http://hubblesite.org/api/v3/images/{collection}'
    response = requests.get(url_collection).json()
    images_id = [image['id'] for image in response]
    for num, image_id in enumerate(images_id, start=1):
        fetch_hubble_by_id(path, image_id)


def get_url_extension(url):
    return url.split('.')[-1]


def main():
    parser = argparse.ArgumentParser(description='Downloading photos from the Hubble')
    parser.add_argument('path', help='Path to save images')
    parser.add_argument('collection', help='Collection name')
    args = parser.parse_args()
    path = args.path
    collection = args.collection
    print('Images download...')
    fetch_hubble_by_collection(path, collection)
    print('Done.')


if __name__ == '__main__':
    main()
    

