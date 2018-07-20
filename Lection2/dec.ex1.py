# Напишіть декоратор ( функцію logg), яка обертає функції. Суть декоратора в тому, що він логує
# (записує у файл) позиційні і ключова аргументи. В кінці враппера записати у файл ‘Arguments are
# written\n’. Також створити дві функції add & multiply, які підповідно додають, перемножують позиційні
# аргументи і вертають результат. Обернути функції add & multiply декоратором logg і викликати їх
# через if __name__ == “__main__”. Перевірити лог файл чи декоратор спрацював.


def logg(func):
    output = []
    def wrapper(*args):
        for item in args:
            output.append(item)
        print ('Arguments are written {}'.format(len(output)))
    return wrapper



@logg
def add(*args):
    sum_result = 0
    for i in args:
        sum_result +=i
    return sum_result

@logg
def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result


if __name__ == '__main__':
    add(1,2,3,4,5)
    multiply(1,2,3,4,5,6)