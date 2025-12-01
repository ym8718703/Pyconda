def leap(x):
    if x%4 == 0:
        return True
    else :
        return False
    
year = int(input("Enter a Year to check if it is Leap year\n"))
if leap(year):
    print(year," is a leap year")
else :
    print(year," is not a leap year")