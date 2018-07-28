import json


class AliceRequest(object):
    def __init__(self, request_dict):
        self._request_dict = request_dict

    @property
    def version(self):
        return self._request_dict['version']

    @property
    def session(self):
        return self._request_dict['session']

    @property
    def user_id(self):
        return self.session['user_id']

    @property
    def is_new_session(self):
        return bool(self.session['new'])

    @property
    def command(self):
        return self._request_dict['request']['command']

    def __str__(self):
        return str(self._request_dict)


class AliceResponse(object):
    def __init__(self, alice_request):
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "end_session": False
            }
        }

    def dumps(self):
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2
        )

    def set_text(self, text):
        self._response_dict['response']['text'] = text[:1024]

    def set_buttons(self, buttons):
        self._response_dict['response']['buttons'] = buttons

    def set_items(self, items):
        self._response_dict['response']['card'] = {
            'type': 'ItemList',
            'header': {
                'text': 'Блюда'
            },
            'items': items
        }

    def set_items(self):
        self._response_dict['response']['card'] = {
                'type': "ItemsList",
                'header': {
                    'text': "Блюда"
                },
                'items': [
                    {
                    'image_id': "5274",
                    'title': "Фуагра",
                    'description': "Специальным образом приготовленная печень откормленного гуся или утки.",
                    'button': {
                        'text': 'Текст кнопки',
                        'url': "https://4damki.ru/wp-content/uploads/2016/02/chto-takoe-fuagra-800x445.jpg"
                    }
                    }
                ]
            }

    def end(self):
        self._response_dict["response"]["end_session"] = True

    def __str__(self):
        return self.dumps()