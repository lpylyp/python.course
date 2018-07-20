# Напишіть код, який приймає рядок як вхідний і повертає рядок задом наперед.
# def reverse(input_string):
#     return print(input_string[::-1])
#
#
# reverse('abcd')

# Юзер вводить строку. (наприклад inp = ‘saveChangesInTheEditor’). Вивести на екран скільки слів є
# цьому інпуті. ( враховувати що нове слово починається із великої літери)
import re

inp = 'saveChangesInTheEditor'

# def count_words(data):
#     temp = ''
#     for i in data:
#         if i.islower():
#             temp +=i
#         else:
#             temp +=','
#             temp +=i
#     comma_count = temp.count(',')
#     number_of_words = comma_count + 1
#     print ('There is a {} words in input'.format(number_of_words))
#
# count_words(inp)

# pangram - строка яка містись усі літери англійської абетки. Перевірити чи введена строка є
# pangram

# param = 'abcdefghijklmnopqrstuvwxyz'
#
# def check_if_param(data):
#
#     for i in param:
#         data = data.lower()
#
#         if i in data:
#             continue
#
#         else:
#             print('Sting is not param')
#             break
#     else:
#         print('Input is param')
#
#
# check_if_param('Abcdefghijklmnopqrstuvwxyz')


# Є строка S, ми можемо перетворити кожну букву окремо на малу або велику, щоб створити іншу
# строку. Треба вернути список всіх можливих комбінацій. Наприклад є строка var = ‘it’ результатом
# буде result_list = [‘IT’, “It”, “iT”, ‘it’].

s = 'it'


def all_variants(inp):
    list = []
    temp = ''


# Юзер вводить пароль. Вивести на екран кількість символів, яких не вистачає щоб
# цей пароль був “складним”. Для того щоб пароль був складним потрібно, щоб пароль складався як
# мінімум із 6 символів, містив у собі по одному символу із вказаних наборів:

s = input("Please enter password to validate: >> ")

if len(s) < 6 or len(s) > 16:
    print("must be in 6 to 16")
elif re.search(r"[a-z]", s) is None:
    print("at leat 1 lowercase should be present")
elif re.search(r'[A-Z]', s) is None:
    print("at least 1 uppercase should be present")
elif re.search(r'\d', s) is None:
    print("at least 1 digit")
elif re.search(r'\W', s) is None:
    print("at least 1 special character should be present")
else:
    print("Password is ok")
