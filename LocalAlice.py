import random
import re
import Recipes


regex = re.compile(r'.*(покажи|попробовать|приготовить)')

deny_phrase_words = "Я вас не понимаю", "Повторите пожалуйста", "Я не знаю таких {0}ов", \
                     "Мне кажется таких {0}ов не существует", "Думаю вы имели в виду что - то другое",\
                     "Вы считаете такие {0}ы существуют? Я - нет", "Откуда вы узнали об этих {0}ах"

hello_phrase = "Здравствуйте, я помогу вам подобрать рецепт блюда из имеющихся у вас ингридиентов.\nНазовите нужные ингридиенты"

suggestion_phrase = "Вы можете приготовить {0}. Показать рецепт или поискать что нибудь другое?"

all_ingridients = Recipes.INGRIDIENTS.keys()


def find_ingridients(phrase):
    needed_ingridients = []
    phrase = re.split(r'[ |,|.]', phrase)
    for word in phrase:
        needed_ingridients.append(word)
    if len(needed_ingridients) != 0:
        return Recipes.get_recipes(needed_ingridients,amount=2)
    else:
        res = random.choice(deny_phrase_words)
        res = res.format('ингридиент')
        print(f"{res}")
        return find_ingridients(input())


def ingridients_to_food(ingridients):
    if ingridients:
        return ingridients[0][0]
    return None

def parse_suggestion_answer(answer):
    if re.search(r'другое', answer) is not None:
        return 1
    if re.search(r'рецепт', answer) is not None:
        return 2
    return 0

print(hello_phrase)
#прилетает какая-то фраза
string = input()
ingridients = find_ingridients(string)
print(ingridients)
reciept = ingridients_to_food(ingridients)
if reciept is None:
    res = random.choice(deny_phrase_words)
    res = res.format('рецепт')
    print(f"{res}")
else:
    print(suggestion_phrase.format(reciept.lower()))
    res = parse_suggestion_answer(input())


def show_receipt(param):
    pass


if res == 2:
    show_receipt(ingridients_to_food(ingridients))
"""regex = re.compile('')
... яблоко груша лимон"""