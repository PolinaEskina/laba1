g = int(input("Введите год: "))
if (g % 4 == 0 or g % 400 == 0) and g % 100 != 0:
    print("Год", g, "- високосный")
else:
    print("Это год не високосный")