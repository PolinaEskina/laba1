x = ("красный","синий","жёлтый")
x1 = input("Введите первый цвет: ")
x2 = input("Введите второй цвет: ")
if x1 in x and x2 in x:
    if x1 != x2:
        if (x1 in ("красный","синий")) and (x2 in ("красный","синий")):
            print("Полученный цвет: фиолетовый")
        if (x1 in ("красный","жёлтый")) and (x2 in ("красный","жёлтый")):
            print("Полученный цвет: оранжевый")
        if (x1 in ("синий","жёлтый")) and (x2 in ("синий","жёлтый")):
            print("Полученный цвет: зеленый")
    else:
        print("Полученный цвет:", x1)
else:
    print("Ошибка")