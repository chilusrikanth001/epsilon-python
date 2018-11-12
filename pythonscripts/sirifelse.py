
s=input("Enther the value for s:")
#s="ajklaksdfjasldu"
vowel="aeiou"



#for i in s:
#	print(i)

i=0
while (i < len(s)):
	if (s[i] in vowel):
		print("Got a vowel ", s[i], "Breaking now")
		i +=1
		continue
	print(s[i])
	i +=1



'''
if (s[0] in vowel):
	print("1st character is a vowel")
	print("condition is true")
elif(s[0].isdigit()):
	print("1st character is digit")
else:
	print("1st character is n0t a vowel or digit")
print("Condition is out of if-else block")
'''
