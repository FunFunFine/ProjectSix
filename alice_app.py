from __future__ import unicode_literals

import logging
import json
import Recipes
import ingridients_string_to_list

from alice_sdk import AliceRequest, AliceResponse

from flask import Flask, request
app = Flask(__name__)

from Utilities import Dish

logging.basicConfig(level=logging.DEBUG)

session_storage = {}
@app.route("/", methods=['POST'])
def main():
    alice_request = AliceRequest(request.json)
    logging.info('Request: {}'.format(alice_request))

    alice_response = AliceResponse(alice_request)

    user_id = alice_request.user_id

    alice_response, session_storage[user_id] = handle_dialog(
        alice_request, alice_response, session_storage.get(user_id)
    )

    logging.info('Response: {}'.format(alice_response))

    return alice_response.dumps()


def handle_dialog(req, res, user_storage):
    if req.is_new_session:
        user_storage = {}
        res.set_text('Здравствуйте, я помогу вам подобрать рецепт блюди из имеющихся у вас ингредиентов.'
                          'Какие ингредиенты у вас есть?')
        dishes = Recipes.get_recipes()

        res.set_items(dishes)
        res.end()

        return res, user_storage
    else:

        ingridients = ingridients_string_to_list.string_to_list_space(req.command)

        dishes = Recipes.get_recipes(ingridients)

        res.set_items(Dish.get_dishes(dishes))

        user_storage = {}

        return res, user_storage
