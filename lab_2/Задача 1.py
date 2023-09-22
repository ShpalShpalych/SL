def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


print(f"Введите строку")
input_text = input()
if is_palindrome(input_text):
    print(f"Строка {input_text} палиндром")
else:
    print(f"Строка {input_text} не палиндром")
