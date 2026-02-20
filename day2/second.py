n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
a = arr[0]
b = arr[0]

for i in range(1, n):
    if arr[i] > a:
        b=a
        a = arr[i]
    elif arr[i] > b and arr[i] < a:
        b = arr[i]
print("Second Largest =", b)