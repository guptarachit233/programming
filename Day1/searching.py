n = int(input("Enter number of elements: "))
arr = [] 
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
x= int(input("enter the element to search"))
found = False
for i in range(n):
    if arr[i] == x:
        found = True
        break
if found == True:
    print("found")
else:
    print("not found")