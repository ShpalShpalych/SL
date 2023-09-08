string = 'Never look back'
char_count = {}
for char in string:
    if char != ' ':
        char_count[char] = char_count.get(char, 0) + 1
print(char_count)
