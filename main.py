import requests


# def get_response():
#     url = "https://httpbin.org/get"
#     resp = requests.get(url)
#     print(resp.json())
#
#
# get_response()

#
# def get_response1():
#     html_page = requests.get("https://netology.ru")
#     print(html_page.text)
#
#
# get_response1()


# def get_heroes():
#     heroes = requests.get("https://akabab.github.io/superhero-api/api/powerstats/")
#     heroes.raise_for_status()
#     if heroes.status_code != 204:
#         print(heroes.json())
#
# get_heroes()

#TASK
# Кто самый умный супергерой? Есть API по информации о супергероях с информацией по всем супергероям.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
from pprint import pprint
def get_heroes():
    heroes = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
    heroes_dict = heroes.json()
    powerstats_dict = {}
    heroes_in_task = ['Hulk', 'Captain America', 'Thanos']
    for hero in heroes_dict:
        if hero['name'] in heroes_in_task:
            powerstats_dict[hero['name']] = hero['powerstats']
    print(powerstats_dict)
    intelligence_dict = {}
    for name, parameters in powerstats_dict.items():
        # intelligence_dict[k] = []
        intelligence_dict[name] = parameters['intelligence']
    print(intelligence_dict)
    most_intelligent = max(intelligence_dict, key=intelligence_dict.get)
    print(f'Самый умный геой {most_intelligent}')
get_heroes()