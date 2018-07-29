from __future__ import unicode_literals

import logging
import json
import Recipes

from alice_sdk import AliceRequest, AliceResponse

from flask import Flask, request
import random

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


def on_error(res):
    deny_phrase_words = "Я вас не понимаю", "Повторите пожалуйста", "Я не знаю таких {0}ов", \
                        "Мне кажется таких {0}ов не существует", "Думаю вы имели в виду что - то другое", \
                        "Вы считаете такие {0}ы существуют? Я - нет", "Откуда вы узнали об этих {0}ах"
    res.set_text(random.choice(deny_phrase_words).format('рецепт'))


def on_ok(res, dishes):
    def get_items(dishes):
        items = []
        for dish in dishes:
            items.append(Dish.get_dish('5274', dish[0], '', dish[0], dish[1]))
        return items

    res.set_text('Вы можете попробовать одно из этих блюд')
    res.set_items(get_items(dishes))


def handle_dialog(req, res, user_storage):
    if req.is_new_session:
        user_storage = {}
        res.set_text('Здравствуйте, я помогу вам подобрать рецепт блюда из имеющихся у вас ингредиентов.\n'
                     'Какие ингредиенты у вас есть?')
        res.end()

        return res, user_storage
    else:
        ingridients = req.command.split()

        dishes = Recipes.get_recipes(ingridients, amount=3)

        if len(dishes) <= 0:
            on_error(res)
        else:
            on_ok(res, dishes)

        res.end()
        user_storage = {}

        return res, user_storage
