
n = int(input("Rows: "))
num = 2

for i in range(1, n+1):
    print(" " * (n - i) * 3, end="") 
    for j in range(i):
        print(f"{num:<4}", end="")  
        num += 2
    print()
