# Space
**Instagram: @a_space_fan**

Scripts for downloading photos of the latest launch SpaceX, photos from the Hubble telescope and posting to Instagram.
### How to install

Python3 should be already installed. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
For posting to Instagram create `.env` file with environment variables, Instagram login and password:
```
USERNAME=<username>
PASSWORD=<password>
```
### Usage
- Downloading photos of the latest launch SpaceX:
```
python3 fetch_spacex.py <path to save images>
```
- Downloading collection of photos from the Hubble telescope, available collections: `holiday_cards`, `wallpapers`, `spacecraft`, `news`, `printshop`, `stsci_gallery`:
```
python3 fetch_hubble.py <path to save images> <collection>
```
- Posting to Instagram:
```
python3 send.py <path_to_images>
```
### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org)


