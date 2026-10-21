# Accessing substrings

s = 'python programming'
print(s[0] , s[-1])
print(s[0:6],s[7:],s[:6])
print(s[::2])
print(s[::-1])
print(len(s))

# Editing and deleting (immutability)



s = "hello"
# s[0] = "H"      # TypeError: strings are immutable
s = "H" + s[1:]   # create a new string instead
print(s)
s = s.replace("l", "L")
print(s)
del s             # deletes the variable
# print(s)        # NameError



# strings Operation

a , b = "Hello" , "World"
print(a + " " + b)
print(a * 3)
print("H" in a, "z" not in a)
print(a == "Hello" , a<b)
for ch in a:
    print(ch)






# String Functions

s = "Hello, python World "
print(s.upper() , s.lower() , s.title() ,s.capitalize())
print(s.strip(),s.lstrip(),s.rstrip())
print(s.count("o"), s.find("python"),s.index("W"))
print(s.replace("python" , "java"))
print(s.split(","))
print("-".join(["a" ,"b","c"]))
print("abc".isalpha(),"123".isdigit(),"a1".isalnum())
print("hello".startswith("he"),"hello".endswith("lo"))
print("hello".center(11,"*"))
print("5".zfill(3))



