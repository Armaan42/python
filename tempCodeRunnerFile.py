t1 = tuple()
n = int(input("Enter the length of tuple: "))
i = 1

while(i <= n):
    a = input("Enter the number: ")
    t = t + (a,)
    i += 1
print("output: ",t)