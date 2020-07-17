import requests
import json
from time import sleep

token = ''
owner_id = input('Enter groud_ip:')
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
