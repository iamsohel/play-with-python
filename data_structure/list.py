from collections import deque
letters = ['a', 'b', 'c', 'd', 'e']
combined = list(range(20)) + letters
# print(combined)
# print(['*'] * 4)

# print(letters[-1])
# print(letters[0:2])
# print(letters[:2])
# print(letters[1:])
# print(letters[:])
# print(letters[::2])
# print(list(range(20))[::2])  # =>[0,2,4,6,8]

# unpacking
numbers = [1, 2, 3, 4, 5, 9]
one, two, *others, last = numbers
# print(one, two, others, last)
for n in numbers:
    # print(n)
    pass

for index, number in enumerate(numbers):
    # print(index, number)
    pass

# add
nums = [1, 2, 3, 4, 56, 6]
nums.append(7)
nums.insert(1, 3)
# print(nums)
nums.pop()
nums.pop(0)
# print(nums)
del nums[0:1]  # delete a range of items
nums.clear()  # delete all the list
# nums.remove("0") if you don't know the index then use remove method, it will delete first matching element.
# print(nums)
# remove

# finding
letters = ["a", "b", "c", "d", "d"]
# 2, it will return the number of occur of d in this list
# print(letters.count("d"))
if "b" in letters:
    # print(letters.index("b"))
    pass

# sorting
numbers = [1, 3, 4, 2, 5]
numbers.sort()  # modify original list
numbers.sort(reverse=True)

sorted(numbers)  # don't modify original list
sorted(numbers, reverse=True)
# print(numbers)

# object/tuple sorting
items = [
    ('products1', 3),
    ('products2', 2),
    ('products3', 4)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
# print(items)


# (key=lambda parameters:expression)
items.sort(key=lambda item: item[1])
# print(items)

prices = []
for item in items:
    prices.append(item[1])

# print(prices)


# map
prices = list(map(lambda item: item[1], items))
# print(prices)


# filter
filtered = list(filter(lambda item: item[1] >= 3, items))
# print(filtered)

# comprehention
# [expression for item in items ]
# map
prices = [item[1] for item in items]
# print(prices)

# comprehention
# [expression for item in items ]
# filtered
filtered = [item for item in items if item[1] >= 3]

# zip
l = [1, 2, 3]
l2 = [2, 5, 6]
# print(list(zip(l, l2)))

# stack
browsering_session = []
browsering_session.append(1)
browsering_session.append(2)
browsering_session.append(3)
# print(browsering_session)
last = browsering_session.pop()
# print(last)

if browsering_session:
    # print(browsering_session[-1])
    pass

# queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
# print(queue)
queue.popleft()
# print(queue)

# swapping
x, y = 1, 2

x, y = y, x
# print(x, y)

# set

first = {1, 2, 3, 4, 5}
last = {1, 3, 5, 7}

# print(first | last)
# print(first & last)
# print(first - last)

# exercise

chracters = 'this is the collection of characters'

char_frequency = {}
for char in chracters:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_char = sorted(char_frequency.items(),
                     key=lambda kv: kv[1], reverse=True)

# print(char_frequency)
# print(char_frequency.items())
# print(sorted_char[1])

# print(len(list(range(20))))

letters = ['a', 'b', 'c']
# print(letters[:2])
