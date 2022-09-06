import requests
import json
from datetime import date
from datetime import timedelta

api_key = ''

api_url = 'https://api.nasa.gov/planetary/apod'

apod_images = []

day = date(2000, 10, 31)

num_images = 500

file_name = 'data.json'

while len(apod_images) < num_images:
    day += timedelta(days=1)

    # Parameters / Key Points
    params = {
        'date': date.isoformat(day),
        'hd': 'True',
        'api_key': api_key
        }

    response = requests.get(api_url, params=params)
    json_data = json.loads(response.text)

    img_explanation = json_data['explanation']
    img_tilte = json_data['title']
    img_url = json_data['url']

    # some images do not have hdurl
    # try and catch assures always having images with hdurl
    try:
        img_hdurl = json_data['hdurl']
        image = {
            'title': img_tilte,
            'explanation': img_explanation,
            'url': img_url,
            'hdurl': img_hdurl
            }

        apod_images.append(image)
    except:
        pass

with open(file_name, 'w') as fp:
    json.dump(list(apod_images), fp)
