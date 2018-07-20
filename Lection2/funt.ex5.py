# Написати функцію (len_of_args), яка приймає ключові та позиційні аргументи ( вертає довжину
# позиційних елементів - len(args) ) . Також написати функцію rand_of_el, яка двічі викликає функцію
# len_of_args і вертає різницю результатів. Викликати функцію rand_of_el і надрукувати результат.



def len_of_args(*args,**kwargs):

    return len(args)

def rand_of_el():
    a = len_of_args(1,2,3,4,5)
    b = len_of_args(3,4,5)

    return print (a - b)


rand_of_el()