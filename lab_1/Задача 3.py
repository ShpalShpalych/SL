import random

ran_numbers = []
for _ in range(20):
    ran_numbers.append(random.randint(1, 100))
print(ran_numbers)
unique_numbers = [x for x in ran_numbers if ran_numbers.count(x) <= 2]
unique_numbers.sort(reverse=True)
print(unique_numbers)
