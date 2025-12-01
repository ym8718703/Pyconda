num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10
if num == rev:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")

#OR

num = (input("Enter a number: "))
if num == num[::-1] :
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")
    

