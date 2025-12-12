temple = "Salom, mening ismim {name} va yoshim {age}."

name = input("Name: ").capitalize()
age = int(input("Age: "))

result = temple.format(name=name, age=age)

print(result)