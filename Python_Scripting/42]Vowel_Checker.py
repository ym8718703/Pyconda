def vowel(ch):
    vowels = "AEIOUaeiou"
    if char in vowels:
          return True
    else:
          return False
Vowel = 0
word = input("Enter a Word\n")
for char in word:
    if vowel(char) :
        Vowel += 1
    
print("Number of vowels: ",Vowel)
