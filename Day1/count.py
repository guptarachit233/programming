n = int(input("Enter number of elements: "))
arr = [] 
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
even = 0
odd = 0
for i in range(n):
    if arr[i] %2 == 0:
        even +=1
    else:
        odd +=1
print("Even numbers =", even)
print("Odd numbers =", odd)