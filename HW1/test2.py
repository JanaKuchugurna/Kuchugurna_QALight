my_str = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
def multiple_replace(target_str, replace_values):
    # отримуємо замінне: підставляємо зі словаря в цикл
    for i, j in replace_values.items():
        # міняємо все на target_str
        target_str = target_str.replace(i, j)
    return target_str

# створюємо словник зі значенням та рядок, який будемо змінювати
replace_values = {"о": "*", "у": "*", "е": "*", "і": "*", "а": "*", "и": "*", "я": "*", "є": "*"}
my_str = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"

# змінюємо та друкуємо рядок
my_str = multiple_replace(my_str, replace_values)
print(my_str)

d = [1, 2][1]
print(d)
pow_products = input("Enter products: ")

filtered = pow_products.replace(" ","")
products = filtered.split(",")
message = "\n".join(products)
result = "\n".join(["products", message])
print(result)

