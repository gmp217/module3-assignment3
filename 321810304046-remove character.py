a,b=input('Enter string: '),input('character which you want to remove: ')
i=a.find(b)
for j in range(len(a)):
	if i==j:
		a=a.replace(a[i], '')
print('string after removing',b,'is',a)