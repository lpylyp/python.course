# Завантажте текстову версію однієї з книг із сайту Project Gutenberg’s. Замініть усі розриви рядків у
# тексті символом пропуску і запишіть відформатований текст у новий файл formatted_text.txt.
import os

def read_file():
    file_name = 'book.txt'.format(os.path.dirname(__file__))
    output_file = 'formatted_text.txt'.format(os.path.dirname(__file__))
    with open(file_name, 'r') as test_file:
        with open(output_file, 'w') as out_file:
            for line in test_file:
                for symbol in line:
                    if symbol == '\n':
                         symbol = ' '
                         out_file.write(symbol)
                    else:
                         out_file.write(symbol)

        return

read_file()