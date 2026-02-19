n = int(input("Enter number of elements: "))
arr = [] 
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
    print(arr)
p = arr[0]
for i in range(n):
    if arr[i] > p:
        p = arr[i]

print("largest element =", p)