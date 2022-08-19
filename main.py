import os.path

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

#TASK #1
# Кто самый умный супергерой? Есть API по информации о супергероях с информацией по всем супергероям.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
from pprint import pprint
# def get_heroes():
#     heroes = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
#     heroes_dict = heroes.json()
#     powerstats_dict = {}
#     heroes_in_task = ['Hulk', 'Captain America', 'Thanos']
#     for hero in heroes_dict:
#         if hero['name'] in heroes_in_task:
#             powerstats_dict[hero['name']] = hero['powerstats']
#     print(powerstats_dict)
#     intelligence_dict = {}
#     for name, parameters in powerstats_dict.items():
#         # intelligence_dict[k] = []
#         intelligence_dict[name] = parameters['intelligence']
#     print(intelligence_dict)
#     most_intelligent = max(intelligence_dict, key=intelligence_dict.get)
#     print(f'Самый умный геой {most_intelligent}')
#     with open('test_heroes.txt','w') as f:
#         f.write(most_intelligent)
#     f.close()
#
# get_heroes()


#TASK #2
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на ЯндексДиск с таким же именем.
# Все ответы приходят в формате json; Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443
# Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!
# Шаблон для программы


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def folder_creation(self):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'{folder_name}',
                  'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        print(response)

    def upload(self, file_path: str):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'{folder_name}/{file_name}',
                  'overwrite': 'true'}

        response = requests.get(url=url, headers=headers, params=params)
        href = response.json().get('href')

        uploader = requests.put(href, data=open(files_path, 'rb'))
        print(uploader)

if __name__ == '__main__':
    ya_token = ''
    file_name = "test_heroes.txt"
    folder_name = 'Requests'
    import os
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    files_path = os.path.join(desktop, file_name)
    uploader = YaUploader(ya_token)
    uploader.folder_creation()
    uploader.upload(files_path)




