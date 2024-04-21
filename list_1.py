l1 = [1,2,3,4]
l1.append(5)
print(l1)

#find the second largest number 

# l2 = list(input("Enter the list: "))
# l2.sort(reverse=True)
# print(l2[1])

#
# l = []

# length = int(input("Enter the length: "))
# for i in range(length):
#     n = int(input("Enter the number in the list: "))
#     if n % 2 == 0:
#         l.append(n)

# print("List containing only even numbers:", l)

#-------------------------------

list_1 = [1,2,3]
list_2 = [4,5]
list_1.extend(list_2)
print(list_1)

#--------------------------------

num = [1,2,4,5]
num.insert(2,6)
print(num)

list_1.reverse()
print(list_1)

#-------------------------------

x = 'python'
print(x.index('t'))

l_1 = [1,2,3,4,5]
b = l_1.pop(1)
print(l_1)

del l_1[2:3]
print(l_1)

#----------------------

l = []

while True:
    element = input("Enter the elements (Type done to exit): ")
    if element.lower() == 'done':
        break
    l.append(int(element))

num = int(input("Enter the number: "))

count = 0
for i in l:
    if num == i:
        count += 1
    
print(num,"=" ,count)

#---------------------------LINEAR SEARCH

list1 = eval(input("Enter the list elements: "))
length = len(list1)

element = int(input("Enter the element we can search: "))

for i in range(0,length):
    if element == list1[i]:
        print("Element found at index", i)
        break
else:
    print("Not found")

#-----------------------------BUBBLE SORT

l = [42,29,74,11,65,58]
length = len(l)

print("Original list: ",l)

for i in range(length - 1):
    for j in range(length - i - 1):
        if(l[j] > l[j+1]):
            l[j], l[j+1] = l[j+1], l[j]

print("List after bubble sort: ",l)










