immutable_var = (27, 54, True, "Table")
print(immutable_var)
print(type(immutable_var))
# immutable_var[2] = False
# print(immutable_var)
# Как мы видим тип переменной immutable_var - 'tuple', т.е. кортеж - неизменяемый объект,
# поэтому изменение элемента кортежа, приводит к ошибке.
mutable_list = [74, 52, False, "Desk"]
print(mutable_list)
mutable_list[3] = "Desktop"
print(mutable_list)
mutable_list[2] = True
print(mutable_list)
print(type(mutable_list))