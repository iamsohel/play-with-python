for number in range(1, 10):
    print("attempt", number, (number) * ".")


for number in range(1, 10, 2):  # every time increment by 2
    print("attempt", number, (number) * ".")

successful = False
for number in range(3):
    print("attempted", number)
    if successful:
        print("successful")
        break

else:  # will call if break is executed
    print("3 time failed")


for x in range(1, 4):
    for y in range(1, 3):
        print(f"({x}, {y})")
