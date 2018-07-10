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

