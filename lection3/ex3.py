# Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом.
# Прочитайте кожен рядок зі створеного у попередньому завданні файлу learning_python.txt і
# замініть слово Python назвою іншої мови, наприклад C при виведенні на екран. Це завдання
# написати в окремій функції.


import os


def change_word():
    file_name = 'learning_python.txt'.format(os.path.dirname(__file__))
    with open(file_name, 'r') as test_file:
        new_list = list()
        for line in test_file:
            
            line = line.replace('Python', 'C')
            new_list.append(line.strip())

    return new_list


print(change_word())
