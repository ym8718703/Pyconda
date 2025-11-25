salary = float(input("enter your salary :"))

if salary > 0 and salary <= 10000 :
    bonus = salary*0.1
elif salary > 10000 and salary <= 20000 :
    bonus = salary*0.2   
elif salary > 20000 :
    bonus = salary*0.4
else :
    print("Enter Valid number")
print(f"Bonus = {bonus}")
print("Final salary",salary+bonus)