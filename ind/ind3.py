#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":
    with open("newfile.txt", "w") as f:
        f.write("Имя текущего пользователя: ")
        f.write(os.getlogin())
        f.write("\nТекущая директория: ")
        f.write(os.getcwd())
    ch = os.path.exists("ind3.txt")
    if not ch:
        os.rename("newfile.txt", "ind3.txt")
    else:
        print("Файл уже существует")
        