"""Домашнє завдання №1: Робота зі списками та словником

1. Створити список з 3-4 елементів, вивести суму всіх його елементів
    (це можуть бути цифри, або рядки, головне щоб усе одного типу)
2. Створити список з 5-6 елементів, деякі з яких повторюються. Вивести суму унікальних значень.
3. Створити словник де є поле "зарплата". Перевизначити значення цього поля,
    щоб воно дорівнювало 1.5 від початкової зарплати."""

list1 = [15, 25, 30, 12]
print("sum:", sum(list1))

list2 = [25, 11, 13, 11, 18, 25]
my_set = set(list2)
print(sum(my_set))

dict= {'salary': 1000}
dict['salary'] *= 1.5
print(dict)
