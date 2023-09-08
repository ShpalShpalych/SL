def is_vowel(char):
    vowels = "АаУуЕеОоЭэЁёЯяИиЮюЫы"
    return char in vowels


text = input("Введите текст: ")
vowel_count = 0
consonant_count = 0
vowels_list = []
words = text.split()
word_count = len(words)
for char in text:
    if char.isalpha():
        if is_vowel(char):
            vowel_count += 1
            vowels_list.append(char)
        else:
            consonant_count += 1
print(f"Количество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")
print(f"Количество слов в тексте: {word_count}")
if vowel_count == consonant_count and vowel_count != 0:
    print("Гласные буквы в тексте:", " ".join(vowels_list))
