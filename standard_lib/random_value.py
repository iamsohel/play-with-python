import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 3, 6, 8]))
print(random.choices([1, 3, 4, 5, 6, 8, 7], k=2))  # [2,5]

print("".join(random.choices(string.ascii_letters + string.digits, k=8)))

string = 'asdlfj asldfk ertgwer'
result = string.split(" ")
print(",".join(result))


numbers = [1, 2, 3, 4]

random.shuffle(numbers)
print(numbers)
