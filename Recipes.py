from requests_html import *
import json
with ('ingridients.json','r') as f:
    INGRIDIENTS = json.load(f)




def extract(page):
    session = HTMLSession()
    r = session.get(page)
    dict1 = r.html.find('div,p,div,ul,div,div,div,div')
    for e in dict1:
        if ('item-description',) in e.attrs.values():
            x = (e.find('h2,a'))
            y = x[1].attrs
            num = y['href'].rfind('-')
            n = y['href'][num + 1:]
            yield (x[1].text, n)


INITIAL_LINK = 'https://eda.ru/wiki/ingredienty/'
ADDONS = 'krupy-bobovye-muka bakaleya specii-pripravy syry molochnye-produkty-yayca ryba-moreprodukty' \
         ' ovoschi-korneplody ptica orehi ' \
         'myaso-myasnaya-gastronomiya gotovye-produkty griby frukty-yagody zelen-travy'.split()


def words_to_digits(ingredients):
    ingred = []
    with open('ingridients.json', 'r') as f:
        d = json.load(f)
        alphabet = {k.lower(): v for k, v in d.items()}
    for ingredient in ingredients:
        result = [value for key, value in alphabet.items() if ingredient in key.lower()]
        ingred.append(result[0])
    return ingred



print(words_to_digits(['рис', 'сыр']))

