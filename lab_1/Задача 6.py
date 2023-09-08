text = input("Введите текст\n")
words = []
current_word = ""
for char in text:
    if char.isalnum():
        current_word += char
    elif current_word:
        words.append(current_word)
        current_word = ""
if current_word:
    words.append(current_word)
word_tuple = tuple(words)
print(word_tuple)
