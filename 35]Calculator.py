def add(x,y):
    Addition = x + y
    return(Addition)
def sub(x,y):
    Substraction = x - y
    return(Substraction)
def mul(x,y):
    Multiplication = x * y
    return(Multiplication)
def div(x,y):
    Division = x / y
    return(Division)

num1 = int(input("Enter First number :"))
op = input("Enter an Arithmetic Operation(+,-,*,/) :")
num2 = int(input("Enter Second number :"))

if op == '+':
   result = add(num1,num2)
elif op == '-':
   result =    sub(num1,num2)    
elif op == '*':
   result =    mul(num1,num2)
elif div == '/':
   result =    div(num1,num2)    
else :
    print("INVALID")

print(f"{num1} {op} {num2} = {result}")    



