def identify(n):
    if n%2 == 0:
      return(1)
    else :
       return(0)
    
Num = int(input("Enter a Number :"))
A = identify(Num)
if A == 1 :
   print("Number is Even")
else :
   print("Number is ODD")   

    
