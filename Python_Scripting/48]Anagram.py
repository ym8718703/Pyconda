def anagrams(s1, s2):
   return sorted(s1) == sorted(s2)

print(anagrams(input("Enter Fisrt Word :"),input("Enter Fisrt Word :")))