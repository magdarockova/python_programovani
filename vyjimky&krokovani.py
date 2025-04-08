
#smeny
'''
lines = []
with open("smeny.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line)
avg_sales = []
for line in lines:
    line = line.split(",")
    # 2904,4
    total_sales, hours = line
    avg = int(total_sales) / int(hours)
    avg_sales.append(avg)
print(avg_sales)'
'''

# smeny2 -- ZeroDivisionError
'''
lines = []

with open("smeny-2.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line)

avg_sales = []
for line in lines:
    line = line.split(",")
    # pondělí,2904,4
    day, total_sales, hours = line
    hours = int(hours)
    if hours > 0:                           # IF je metoda "nejdriv otestuj a pak proved"
        avg = int(total_sales) / int(hours)
        avg_sales.append(avg)
    else:
        print(f"Údaj o délce směny pro {day} je chybný.")

print(avg_sales)
'''

# metoda Easier to Ask Forgiveness Than Permission (EAFP)
lines = []
with open("smeny-2.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line)
avg_sales = []
for line in lines:
    line = line.split(",")
    # pondělí,2904,4
    day, total_sales, hours = line
    hours = int(hours)
    try:
        avg = int(total_sales) / int(hours)
        avg_sales.append(avg)
    except ZeroDivisionError:
        print(f"Délka směny pro {day} je 0.")
print(avg_sales)


