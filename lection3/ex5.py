# Завантажте текстову версію книги The Life and Adventures of Robinson Crusoe By Daniel Defoe із
# сайту Project Gutenberg’s. Витягніть із тексту заголовки усіх розділів, які мають вигляд, на зразок:
# CHAPTER I—START IN LIFE. Запишіть знайдені назви у новий файл chapters.txt


import os

def read_file():
    file_name = 'DDEfoe.txt'.format(os.path.dirname(__file__))
    output_file = 'chapters.txt'.format(os.path.dirname(__file__))
    with open(file_name, 'r') as test_file:
        with open(output_file, 'w') as out_file:
            for line in test_file:
                if 'CHAPTER' not in line:
                    continue
            else:
                out_file.write(line)




    return


read_file()