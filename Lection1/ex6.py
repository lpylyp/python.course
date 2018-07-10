lloyd = { "name": "Lloyd", "homework": [90.0,97.0,75.0,92.0], "quizzes": [88.0,40.0,94.0], "tests": [75.0,90.0] }
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0] }
tyler = { "name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0] }

#Створити список ( students ), що містить lloyd, alice, tyle
students = [lloyd, alice, tyler]




#Для кожного студента надрукувати інформацію у читабельному форматі


for name in students:
    print (name["name"])
    print (name["homework"])
    print (name["quizzes"])
    print (name["tests"])

# Напишіть функцію average ( Приймає список, вертає результат. Всередині функції викличіть
# вбудовану функцію sum() передавши аргумент. Результат помістити в змінну total. Привести total до типу
# float ( число з плаваючою точкою). Поділити total на кількість елементів у вхідному списку використавши
# len функцію. Вернути результат.

def average(data):
    total = float(sum(data))/ float(len(data))
    return total


# Написати функцію get_letter_grade ( Використати if elif else. Якщо 90 і більше A, 70-90 B, 50-70 C,
# решта D. Функція примає число вертає Оцінку A, B, C або D.)

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    else:
        return 'F'

# перевірити функцію get_letter_grade. Знайти середню оцінку по домашніх завданнях для кожного
# студента і надрукувати. (Тобто спочатку викликати функцію average[‘homework’], і передати результат в
# функцію get_letter_grade)


for homework in students:
    print(' {} avagare is: {}'.format(homework['name'],average(homework['homework'])))
    print ('His grade is: {}'.format(get_letter_grade(average(homework['homework']))))


# Знайти середню оцінку для всього класу. ( в числовому і буквенному виразі )

av_homework  = 0
av_quizzes = 0
av_tests = 0
for student in students:

    av_homework += average(student['homework'])

    av_quizzes += average(student['quizzes'])
    av_tests += average(student['tests'])
print('Average homework is: {} grade is {}'.format((av_homework/3),get_letter_grade(av_homework/3)))
print('Average quizzes is: {} grade is {}'.format((av_quizzes/3),get_letter_grade(av_quizzes/3)))
print('Average tests is: {} grade is {}'.format((av_tests/3),get_letter_grade(av_tests/3)))

