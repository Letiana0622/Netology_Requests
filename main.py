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

    def get_ya_disk(self):
        resp_get = requests.get('https://cloud-api.yandex.net/v1/disk')
        print(resp_get)

    def upload(self, file_path: str):
        with open(file_path, 'rb') as f:
            resp = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload', files={"file": f})
        print(resp)
#         """Метод загружает файлы по списку file_list на яндекс диск"""
#         # Тут ваша логика
#         # Функция может ничего не возвращать

if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
    import os
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    path_to_file = os.path.join(desktop, "test_heroes.txt")
    print(path_to_file)
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    result_get = uploader.get_ya_disk()