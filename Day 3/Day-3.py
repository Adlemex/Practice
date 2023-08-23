1. 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in a:
    if element < 5:
        print(element)

2.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = []
for element in a:
    if element in b:
        common_elements.append(element)
print(common_elements)

3.
import random

list1 = [random.randint(1,10) for i in range(5)]
list2 = [random.randint(1,10) for i in range(5)]
merged_list = list1 + list2
print("Объединенный список: ", merged_list)
print("Длина списка: ", len(merged_list))
print("Сумма элементов списка: ", sum(merged_list))

4.
import random

random_list = [random.randint(1,10) for i in range(10)]
last_local_max_index = None
for i in range(1,len(random_list)-1):
    if random_list[i] > random_list[i-1] and random_list[i] > random_list[i+1]:
        last_local_max_index = i
print("Номер последнего локального максимума: ", last_local_max_index)

5.
import random

names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Helen', 'Ivan', 'John']
ages = [random.randint(18,80) for i in range(10)]
people = dict(zip(names, ages))
sorted_people = dict(sorted(people.items(), key=lambda x: x[1]))
print(sorted_people)

6.
points = {'А':1, 'Б':3, 'В':1, 'Г':3, 'Д':2, 'Е':1, 'Ё':3, 'Ж':5, 'З':5, 'И':1, 
          'Й':4, 'К':2, 'Л':2, 'М':2, 'Н':1, 'О':1, 'П':2, 'Р':1, 'С':1, 'Т':1,
          'У':2, 'Ф':10, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Щ':10, 'Ъ':10, 'Ы':4,
          'Ь':3, 'Э':8, 'Ю':8, 'Я':3}

word = input("Введите слово: ")
score = 0
for letter in word:
    score += points.get(letter.upper(), 0)
print("Стоймость слова", word, "равна", score)

7.
cats = [('Мурзик', 3, 'Иван', 'Иванов'), ('Барсик', 2, 'Петр', 'Петров'), 
        ('Том', 5, 'Иван', 'Иванов'), ('Кекс', 1, 'Мария', 'Сидорова'), 
        ('Матроскин', 4, 'Петр', 'Петров')]

owners = {}
for cat in cats:
    name, age, owner_name, owner_surname = cat
    if (owner_name, owner_surname) not in owners:
        owners[(owner_name, owner_surname)] = [name + " " + str(age)]
    else:
        owners[(owner_name, owner_surname)].append(name + " " + str(age))

for owner, cats in owners.items():
    print(owner[0], owner[1] + ":", ", ".join(cats))