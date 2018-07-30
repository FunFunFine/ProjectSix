import requests
import json

# Provide your own skill_id and token!
SKILL_ID = '4d4e9490-394b-4031-be59-6b6aba57f198'
OAUTH_TOKEN = 'AQAAAAAElAJwAAT7o_-SdfTt3kz9r1aoh_ueFWY'

r = requests.post(
    "https://dialogs.yandex.net/api/v1/skills/{0}/images".format(SKILL_ID)
)

def download_image(url):
    headers = {
        'Authorization': 'OAuth {0}'.format(OAUTH_TOKEN),
        'Content-Type': 'application/json'
    }

    payload = {
        'url': url
    }

    r = requests.post(
        "https://dialogs.yandex.net/api/v1/skills/{0}/images".format(SKILL_ID),
        headers=headers,
        data=json.dumps(payload),
    )
    print(r.text)
    return r.json()

IMGS = []

def get_image_id(url):
    id = None

    for img in IMGS:
        if url == img['image']['origUrl']:
            id = img['image']['id']
            break

    if not id:
        # from threading import Thread

        def downld_img():
            response = download_image(url)
            IMGS.append(response)
            return response

        response = downld_img()

        id = response['image']['id']

    return id



# from time import time
# import Recipes
# t1 = time()
# dishes = Recipes.get_recipes(['рис'], amount=2)
# print(dishes[0][2])
# for dish in dishes:
#     img_id = get_image_id(dish[2])
# print(IMGS)
# t2 = time()
# print(t2-t1)
#
# t1 = time()
# dishes = Recipes.get_recipes(['рис'], amount=2)
# print(dishes[0][2])
# for dish in dishes:
#     img_id = get_image_id(dish[2])
# print(IMGS)
# t2 = time()
# print(t2-t1)