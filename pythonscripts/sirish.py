s = "zekeLabs"
print (s[::-1])
r= s[::-1]
print("Print in reverse order:",r)
##replace L with Small l
z= s.replace("L","l")
print("Print l in small",z)

#print(help(s.replace))

##COUNT THE OCCURANCES OF L in var s
print(s.count("L"))

print(s.center(33,"*"))

print(s.rjust(25,"#"))

i = input("please enter your name: ")
print(i)

i=int(i)
print(type(i))
