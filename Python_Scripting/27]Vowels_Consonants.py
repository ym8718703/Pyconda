def is_vowel(ch):
    # Convert to lowercase to handle both uppercase and lowercase
    ch = ch.lower()
    
    if ch in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

char = input("Enter a character: ")
if len(char) == 1:
    if is_vowel(char):
        print(char, "is a vowel.")
    else:
        print(char, "is not a vowel.")
else:
    print("Please enter only a single character.")
