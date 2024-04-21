name = "john Doe"
for i in name:
    print(i, end="")

print("\n")

print(name[0])

a = str(2) + 'name'
print(a)

s = '''this is shilla
        and my name is shilla'''
print(s)

print(len(name))

print(name.capitalize()) #first letter as uppercase

st = 'blue;red;green'
print(st.split(';'))


st1 = "This is a string example"
print(st1.replace("  is","was"))

st2 = "Cold coffee"
print(st2.replace("Cold","Hot"))

st3 = "green revolution"
result = st3.find('green')
result = st3.find("e",4)
print(result)

st4 = "Good"
print(st4.isalpha()) #True

st5 = "23"
print(st5.isdigit())

st6 = "LEARN"
print(st6.lower())

st7 = "learn"
print(st7.upper())

#-----------------------------------------------------------------------------------------

# line = input("Enter the string: ")
# lowercount = 0
# uppercount = 0
# digitcount = 0
# alphabetcount = 0
# spacecount = 0

# for i in line:
#     if i.islower():
#         lowercount += 1
#     elif i.isupper():
#         uppercount += 1
#     elif i.isdigit():
#         digitcount += 1
#     elif i.isalpha():
#         alphabetcount += 1
#     if i.isspace():
#         spacecount += 1

# print("Number of uppercase letters: ", uppercount)
# print("Number of lowercase letters: ",lowercount)
# print("Number of digits: ",digitcount)
# print("Number of alphabets: ",alphabetcount)
# print("Number of spaces: ",spacecount)

#-----------------------------------------------------------------------------

st = "All New Python"
print(st.istitle())

s1t = "12345"
s = '-'
print(s.join(s1t))

s2t = "Welcome"
print(s2t.swapcase())

s3t = "xyz@gmail.com"
print(s3t.partition('.'))


print(ord('a')) # ord -> returns the ASCII/Unicode of the character

print(chr(97)) # chr -> returns the characters represented by ASCII/ Unicode



