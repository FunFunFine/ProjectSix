import json

class Dish(object):
    @staticmethod
    def get_dishes(dishes):
        res = list()
        for dish in dishes:
            res.append(Dish.get_dish('5717', dish[0], 'description', dish[0], dish[1]))

        return res

    @staticmethod
    def get_dish(image_id, name, description, button_text, url):
        dish = {
            'image_id': image_id,
            'title': name,
            'description': description,
            'button': {
                'text': button_text,
                'url': url
            }
        }

        return dish