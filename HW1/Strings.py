"""Домашнє завдання №3: Робота з рядками (strings)

Preconditions:
Є рядок "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"

Завдання:
1. Вивести в консоль довжину рядка (кількість символів)
2. Вивести в консоль довжину рядка (кількість слів)
3. Розбити рядок на список окремих слів та замінити в кожному слові усі голосні літери
    іншим символом, наприклад #;
4. Відновити рядок зі списку, зі вже заміненими словами."""

#sentence = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
my_str = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
def multiple_replace(target_str, replace_values):
    # отримуємо замінне: підставляємо зі словаря в цикл
    for i, j in replace_values.items():
        # міняємо все на target_str
        target_str = target_str.replace(i, j)
    return target_str

# створюємо словник зі значенням та рядок, який будемо змінювати
replace_values = {"о": "*", "у": "*", "е": "*", "і": "*", "а": "*", "и": "*", "я": "*", "є": "*"}
my_str1 = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"

# змінюємо та друкуємо рядок
my_str = multiple_replace(my_str, replace_values)
print(my_str)

result_of_split = my_str.split(" ")
print(result_of_split)
result1 = "".join(my_str)
print(result1)
print(len(my_str))
print(len(my_str.split(" ")))

"""result = sentence.replace("о", "#")
result1 = sentence.replace("е", "#")
result2 = sentence.replace("і", "#")
result3 = sentence.replace("у", "#")
result4 = sentence.replace("и", "#")
result5 = sentence.replace("я", "#")
result6 = sentence.replace("є", "#")
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)"""





