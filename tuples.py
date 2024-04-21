t = tuple()
print(type(t)) # empty tuple creating

tup1 = ('a',2024,'comps')
print(tup1)

t1 = tuple()
n = int(input("Enter the length of tuple: "))
i = 1

while(i <= n):
    a = input("Enter the number: ")
    t1 = t1 + (a,)
    i += 1
print("output: ",t1)

