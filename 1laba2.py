n = int(input( "Введите ваше место: "))
if n <= 36 and n % 2 == 0:
    print("Верхнее место")
elif n <= 35 and n % 2 != 0:
    print("Нижнее место")
elif n > 36 and n % 2 == 0:
    print("Верхнее боковое место")
else:
    print("Нижнее боковое место")