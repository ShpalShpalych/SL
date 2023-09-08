str_lower_value = input("Введите нижнюю границу: ")
str_upper_value = input("Введите верхнюю границу: ")
if str_lower_value.isdigit() and str_upper_value.isdigit():
    lower_value = int(str_lower_value)
    upper_value = int(str_upper_value)
    if lower_value >= upper_value or lower_value < 0 or upper_value < 0:
        print("Нижняя граница должна быть меньше")
        exit()
    print(f"Простые числа на отрезке [{lower_value}, {upper_value}]: ")
    for number in range(lower_value, upper_value + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number, end=' ')
else:
    print("Введите натуральные числа")
