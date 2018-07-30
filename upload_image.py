import requests
import json

# Provide your own skill_id and token!
SKILL_ID = '4d4e9490-394b-4031-be59-6b6aba57f198'
OAUTH_TOKEN = 'AQAAAAAElAJwAAT7o_-SdfTt3kz9r1aoh_ueFWY'

def download_image(url):
    # payload = {}
    headers = {
        # 'Host': 'https://dialogs.yandex.net',
        'Authorization': 'OAuth {0}'.format(OAUTH_TOKEN),
        'Content-Type': 'application/json'}

    payload = {
        'url': url
    }
    r = requests.post(
        "https://dialogs.yandex.net/api/v1/skills/{0}/images".format(SKILL_ID),
        headers=headers,
        data=json.dumps(payload),
        # data=({'url': url})
    )

    # response = requests.get('https://httpbin.org/get')
    return r.json()

def get_image_id(url):
    response = download_image(url)
    return response['image']['id']
