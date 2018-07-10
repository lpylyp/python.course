import random

inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

#Додайте ключ до словника під назвою "pocket".
inventory['pocket'] = ''

print(inventory)

#Встановіть значення "pocket" як список, що складається з рядків 'seashell', 'strange berry', і 'lint’
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)


#Відсортуйте ( .sort ()) елементи зі списку, що зберігаються під ключем "backpack". ( і надрукуйте)
backpack = inventory.get('backpack')
backpack.sort()

print(backpack)


#Потім видаліть ("dagger") зі списку предметів, що зберігаються під ключем “backpack"
backpack = inventory.get('backpack')
backpack.remove('dagger')
print(backpack)


#Додайте 50 до числа, збереженого під "gold" ключем. І надрукуйте результат.
inventory['gold'] = inventory.get('gold') + 50
print(inventory)


#Створіть новий словник під назвою prices за допомогою {}
prices = {}

#Покладіть в словник такі значення "banana": 4, "apple": 2, "orange": 1.5, "pear": 3
prices ['banana'] = 4
prices ['apple'] = 2
prices ['orange'] = 1.5
prices ['pear'] = 3

print (prices)


#Створити новий словник stocks.( який буде містити інформацію для кожного ключа із prices скільки \
# товару ( запасу є на складі). Згенерувати значення випадковим чином.

stocks = {}

for key in prices:
    stocks[key] = random.randint(0,100)

print(stocks)


#Проітеруйтесь в циклі через кожен ключ в prices. Для кожного ключа надрукуйте ключ разом із
# ціною, а також запасом на складі.

for (key,value), (key2,value2) in zip(prices.items(), stocks.items()):
    print (key)
    print ('Price: {}'.format(value))
    print ('Stock: {}'.format(value2))

# Давайте визначимо, скільки грошей ви зробили б, якщо б ви продали всю їжу ( змінна total, треба
# вирахувати і надрукувати її )
total = 0
for (key,value), (key2,value2) in zip(prices.items(), stocks.items()):
    total+=value*value2
print(total)

