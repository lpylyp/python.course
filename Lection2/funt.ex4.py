# Написати функцію ( find_super ). Функція приймає на вхід число. А повинна вернути суму цифр
# вхідного числа ( якщо ця сума менша 10). Тобто якщо вхідне число = 12345. То сума цифр = 15 (
# 15 > 10 ), тобто треба вернути суму цифр вже 15. (застосувати рекурсію)


def find_super(num):

    if len(str(num)) ==1:
        return str(num)[0]

    else:
        return str(num)[0] + find_super(str(num)[1:])


find_super(123)



