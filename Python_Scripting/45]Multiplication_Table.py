def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
num = int(input("Enter a number :"))
print("Multiplication of given number is :")
table(num)