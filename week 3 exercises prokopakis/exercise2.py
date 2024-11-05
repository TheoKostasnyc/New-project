import random

random_numbers = [random.randint(1, 100) for _ in range(20)]

even_count = 0
for number in random_numbers:
    if number % 2 == 0:
        even_count = even_count + 1


print("Random Numbers:", random_numbers)
print("Count of even numbers:", even_count)

