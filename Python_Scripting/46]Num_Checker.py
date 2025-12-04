def checker(n):
    if n> 0 :
        return True
    else :
        return False
    
num = int(input("Enter a  number: "))
if num == 0:
    print("Number is 0")
elif checker(num):
    print(f"{num} is positive")
else :
    print(f"{num} is negative")
