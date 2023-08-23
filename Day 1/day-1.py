1. 
name = input("Введите имя и фамилию: ")
day = input("Введите номер дня: ")
print("Привет, %s. Это мой %s день учебной практики" % (name, day))

2.
int_num = int(input("Введите целое число: "))
float_num = float(input("Введите дробное число: "))
result = float_num + float_num - int(int_num) -  int(int_num)

print("Сумма дробного числа и целого числа равна:", result)

3.
n = len(input("Введите свои имя и фамилию: "))
m = len(input("Введите свое имя: "))
print("m чисел предшествующие числу n это:", end=" ")
for i in range(m):
    print(n-i-1, end=" ")
print("\nm чисел следующих за числом n это:", end=" ")
for i in range(m):
    print(n+i+1, end=" ")

4.
name = input("Введите свое имя: ")
birth_year = int(input("Введите год своего рождения: "))
current_year = int(input("Введите год: "))
age_now = current_year - birth_year
i = int (input ("Введите свой курс") )
university_age = age_now + (4-i)
print("Привет, %s! Сейчас Вам %s лет. Когда Вы закончите университет, Ваш возраст будет равен %s." % (name, age_now, university_age))

5.
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num1 % 2 == num2 % 2:
    print(True)
else:
    print(False)

6.
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
if num1 > 0 or num2 > 0 or num3 > 0:
    print(True)
else:
    print(False)

7.
num = input("Введите шестизначное число: ")
if len(num) != 6:
    print("Ошибка! Введено не шестизначное число!")
elif int(num) % 2 == 0:
    print("Первая цифра числа:", num[0])
else:
    print("Последняя цифра числа:", num[-1])

8.
num = int(input("Введите трехзначное число: "))
sum_of_digits = 0
for digit in str(num):
    sum_of_digits += int(digit)
print("Сумма цифр числа %s равна %s" % (num, sum_of_digits))

9.
num = input("Введите четырехзначное число: ")
if len(num) != 4:
    print("Ошибка! Введено не четырехзначное число!")
elif len(set(num)) == 4:
    print(True)
else:
    print(False)

10.
hours = int(input("Введите количество часов: "))
minutes = int(input("Введите количество минут: "))
seconds = hours*3600 + minutes*60
print("С начала суток прошло %s секунд" % seconds)