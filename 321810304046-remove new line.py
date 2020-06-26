j,t="","abcd\nefgh\nijkl"
for i in t:
 if(i!='\n'):
  j+=i
 else:
  j+=""
print("string without newline is:",j)