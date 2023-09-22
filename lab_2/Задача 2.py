def analyze_argument(arg):
    if isinstance(arg, tuple):
        if all(isinstance(item, str) for item in arg):
            total_length = sum(len(word) for word in arg)
            return f"Общая длина слов в кортеже: {total_length}"
        else:
            return "Кортеж должен содержать только строки"

    elif isinstance(arg, list):
        if all(isinstance(item, (str, int)) for item in arg):
            num_letters = sum(len(str(item)) for item in arg if isinstance(item, str))
            num_odd_digits = sum(1 for item in arg if isinstance(item, int) and item % 2 != 0)
            return f"Количество букв в списке: {num_letters}, Количество нечётных цифр: {num_odd_digits}"
        else:
            return "Список должен содержать только строки и/или числа"

    elif isinstance(arg, int):
        if arg >= 0:
            num_odd_digits = sum(1 for digit in str(arg) if int(digit) % 2 != 0)
            return f"Количество нечётных цифр в числе: {num_odd_digits}"
        else:
            return "Число должно быть неотрицательным"

    elif isinstance(arg, str):
        num_letters = sum(1 for char in arg if char.isalpha())
        return f"Количество букв в строке: {num_letters}"

    else:
        return "Неизвестный тип аргумента"

print(analyze_argument(("apple", "banana", "cherry")))
print(analyze_argument([1, "hello", 42, "world"]))
print(analyze_argument(13579))
print(analyze_argument("Python3.8"))
print(analyze_argument({"key": "value"}))