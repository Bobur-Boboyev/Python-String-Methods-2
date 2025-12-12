temple = "Bugun {week_day} kuni, dars soat {time} da."

week_day = input("Week day: ")
time = int(input("Time: "))

result = temple.format(week_day=week_day, time=time)

print(result)