# Импорт модулей
import os, sys
from time import sleep
import requests
import json
import colorama

RED = '\033[31m'
YELLOW = '\033[93m'

# Приветствие
print("[+] Привет! Спасибо за установку данной утилиты!")
print("[+] Напоминает, что автор данной утилиты не несёт ответственности за её использование!!!")
print("[+] Она создана ИСКЛЮЧИТЕЛЬНО в ознакомительных целях и для проверки только на своём ip и телефонном номере!!!")

# Выбор способа проверки
print("[+] Выберите способ проверки: ")
print("[+] IP: 1")
print("[+] Telephone Number: 2")
print("[+] Messangers: 3")
enter = input()

# Вывод информации

# IP
if enter == 1:
    try:
        ip = input("[+] Введите IP для проверки: ")
        ip_site = requests.post(f'https://htmlweb.ru/geo/api.php?json&ip={ip}')
        ip_json = ip_site.json()
        country = ip_json['country']

        region = ip_json['region']
        location = ip_json["location"]
        city = ip_json["city"]
        latitude = ip_json["latitude"]
        longitude = ip_json["longitude"]

        print(f"[+] IP: {ip}")
        print(f"[+] Страна: {country[name]}")
        print(f"[+] Регион: {region[name]}")
        print(f"[+] Округ: {region[okryg]}")
        print(f"[+] Локация: {location}")
        print(f"[+] Город: {city}")
        print(f"[+] Ширина: {latitude}")
        print(f"[+] Долгота: {longitude}")

    except:
        print("Что-то пошло не так!")

# Телефонный номер
if enter == 2:
    try:
        number = input(f"{RED} [+]" + f"{YELLOW}Введите номер телефона (вместе с +): ")
        number_site = requests.post(f'https://htmlweb.ru/geo/api.php?json&ip={number}')
        number_json = number_site.json()
        oper = number_json['oper']
        city = number_json['city']
        regionn = number_json['region']
        print(f"[+] Телефон: {number}")
        print(f"[+] Город: {city['name']}")
        print(f"[+] Область: {region['name']}")
        print(f"[+] Округ: {region['okryg']}")
        print(f"[+] Оператор: {oper[brand]}")
        print(f"[+] Сайт оператора: {oper[url]}")
    except:
        print("Что-то пошло не так!")

# Мессенджеры
if enter == 3:
    try:
        numberr = input("Введите номер телефона: ")
        print(f'[+] https://api.whatsapp.com/send?phone={numberr} - WhatsApp')
        print(f'[+] https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - FaceBook')
        print(f'[+] https://twitter.com/account/begin_password_reset - Twitter')
        print(f'[+] https://viber://add?number={numberr} - Viber')
        print(f'[+] https://skype:{numberr}?call - Звонок на номер с Skype')
        print(f'[+] https://nuga.app - Поиск аккаунтов Instagram')
    except:
        print("Что-то пошло не так!")