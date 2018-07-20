import random


def random_10():
    random_num = random.randint(0, 10)
    return random_num


def summarizer(num):
    result = 0
    result = random_10() + num

    if result > 100:
        print(result)

    else:
        pass


summarizer(95)