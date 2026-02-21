n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
a = {}

for i in range(n):
    a[i]= arr[i]

print("Original array:", arr)
print("Copied dictionary:", a)