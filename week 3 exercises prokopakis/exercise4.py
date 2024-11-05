import random


random_numbers = [random.randint(1, 50) for i in range(100)]

user_number = int(input("Enter a number between 1 and 50 : "))

count = [random_numbers.count(user_number)]

print(random_numbers , user_number)