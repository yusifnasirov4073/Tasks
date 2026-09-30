name=input("enter your name: ")
age=input("enter your age: ")
favnum=input("enter your favorite number: ")
age=int(age)
favnum=int(favnum)
age=age+10
favnum=favnum**2
print(age)
print(favnum)
if favnum%2==0:
    type="even"
else:
    type="odd"
print(f"\nHi {name} In 10 years you'll be {age}.")
print(f"Your favourite number squared is {favnum}.")
print(f"and it's {type}.")

#I think everything we type is a character. The symbols we use to represent numbers are also characters. So, everything is treated as text, and str is used by default. That is why whatever we type with input() is taken as a string.