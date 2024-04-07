given_number = int(input("please give me a number: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(given_number, "x", i, given_number * i)