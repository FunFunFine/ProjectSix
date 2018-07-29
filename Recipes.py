from requests_html import HTMLSession
import json
import random
from time import time

with open('./ingridients.json', 'r') as f:
    INGRIDIENTS = json.load(f)



def get_recipes(ingridients, amount=1):
    try:
        nums = words_to_digits(ingridients)
        print(nums)
        links = get_links(nums)
        print(links)
        return links[:amount]
    except Exception as e:
        print(e)


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
    for ingredient in ingredients:
        result = [value for key, value in d.items() if ingredient in key.lower()]
        if result:
            index = random.randint(0, len(result)-1)
            ingred.append(result[index])
    return ingred

SESSION = HTMLSession()
SESSION.get('https://eda.ru/')

def get_links(ingr_nums, n=1):
    init_link = 'https://eda.ru/recepty/ingredienty/' + '/'.join(ingr_nums)
    print(init_link)
    session = HTMLSession()
    r = session.get(init_link)
    dict1 = r.html.find('div,p,div,ul,div')
    links = []
    names = []
    pic = []
    for e in dict1[1:]:
        if 'data-title' in e.attrs:
            names.append(e.attrs['data-title'])
        if 'data-src' in e.attrs:
            pic.append(e.attrs['data-src'])
        if 'data-href' in e.attrs:
            s = e.attrs['data-href']
            if s.startswith('/'):
                # link = 'https://eda.ru/' + s
                # ingredients = get_recipe_ingredients(link)
                # ingred.append(ingredients)
                links.append('https://eda.ru/' + s)
    return list(iter(zip(names, links, pic)))


def get_recipe_ingredients(url):
    session = HTMLSession()
    r = session.get(url)
    dict1 = r.html.find('div,p,div,ul,div')
    # tuple = ('recipe__steps',)
    list = []
    for e in dict1:
        # if tuple in e.attrs.values():
        #     x = (e.find('li,div'))
        #     print(x)
        #     print(e.attrs.values())
        if 'data-ingredient-object' in e.attrs:
            dict = e.attrs['data-ingredient-object']
            d = json.loads(dict)
            # id = d['id']
            name = d['name']
            amount = d['amount']
            list.append((name, amount))
        if 'in_read' in e.attrs.values():
            break
    return tuple(list)

# print(get_recipe_ingredients('https://eda.ru//recepty/supy/tomatnij-sup-pjure-20131'))
# result = get_recipes(['сыр','колбаса'])



