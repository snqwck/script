import requests
import json
from time import sleep

token = 'e7693367debfd0ffe0e12129983fc2ea25b476491d2574105862b841e61adc5d564fa8ee21ace2aa9b152'
owner_id = input('Enter owner_id:')
url = f"https://api.vk.com/method/photos.get?owner_id=-{owner_id}&offset={0}&album_id=wall&count={1000}&access_token={token}&rev=1&v={5.103}"
r = requests.get(url)
response_json = json.loads(r.text)
id_photos = []


for photo in response_json['response']['items']:
    id_photos.append(photo['id'])


for id_photo in id_photos:
    vk_url_photo = f"https://vk.com/photo-{owner_id}_{id_photo}?rev=1"
    url_for_copy_photos = f"https://api.vk.com/method/photos.copy?owner_id=-{owner_id}&photo_id={id_photo}&access_token={token}&v={5.103}"
    requests.post(url_for_copy_photos)
    print(('ID:'), id_photo, (','), vk_url_photo)
    sleep(5)
