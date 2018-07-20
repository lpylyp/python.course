# Напишіть функцію!, яка приймає список ( в списку можуть бути дублікати елементів) і повертає
# новий список, який містить всі елементи першого списку, мінус усі дублікати. Викликати функцію,
# надрукувати результат.


def get_list(some_list):
    new_list = []

    for i in some_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)

    return print(new_list)



get_list(['a','b','c','c','d', '111111', '1', '2', '1'])