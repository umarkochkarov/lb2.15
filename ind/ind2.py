#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    litters = {
            "Аа": 0,
            "Бб": 0,
            "Вв": 0,
            "Гг": 0,
            "Дд": 0,
            "Ее": 0,
            "Ёё": 0,
            "Жж": 0,
            "Зз": 0,
            "Ии": 0,
            "Йй": 0,
            "Кк": 0,
            "Лл": 0,
            "Мм": 0,
            "Нн": 0,
            "Оо": 0,
            "Пп": 0,
            "Рр": 0,
            "Сс": 0,
            "Тт": 0,
            "Уу": 0,
            "Фф": 0,
            "Хх": 0,
            "Цц": 0,
            "Чч": 0,
            "Шш": 0,
            "Щщ": 0,
            "Ъъ": 0,
            "Ыы": 0,
            "Ьь": 0,
            "Ээ": 0,
            "Юю": 0,
            "Яя": 0,
        }

    if len(sys.argv) != 2:
        print(
            "Передайте имя файла в качестве аргумента командной строки: ",
            sys.argv,
            len(sys.argv),
        )
        quit()

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            sentences = f.readlines()

            for sentence in sentences:
                for i in sentence:
                    i = (i.upper() + i.lower())
                    if i in litters:
                        litters[i] += 1


        for key in litters.keys():
            if (litters[key] != 0):
                print(key, ":", litters[key])
    
       
    except IOError:
        # Отображаем ошибку, если с чтением из файла возникли проблемы
        print("Ошибка при доступе к файлу.")
