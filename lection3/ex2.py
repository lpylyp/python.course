# Створіть новий файл у текстовому редакторі і напишіть 3 рядки тексту у ньому про можливості
# Python. Кожен рядок повинен починатися з фрази: In Python you can .... Збережіть файл під ім’ям
# learning_python.txt. Напишіть функцію, яка зчитує файл і виводить текст з перебором рядків об’
# єкта файлу і зі збереженням рядків у списку з подальшим виведенням списку поза блоком with
import os

def read_file():
    file_name = 'learning_python.txt'.format(os.path.dirname(__file__))
    with open(file_name, 'r') as test_file:
        new_list = list()
        for line in test_file:
            new_list.append(line.strip())

    return new_list

read_file()


