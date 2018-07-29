from requests_html import HTMLSession
import json
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
            ingred.append(result[0])
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
    for e in dict1[1:]:
        if 'data-title' in e.attrs:
            links.append(e.attrs['data-title'])
        if 'data-href' in e.attrs:
            s = e.attrs['data-href']
            if s.startswith('/'):
                names.append('https://eda.ru/' + s)
    return list(iter(zip(links, names)))



