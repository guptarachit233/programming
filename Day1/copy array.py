n = int(input("Enter number of elements: "))
arr1 = []
arr2 = [] 
for i in range(n):
    num = int(input("Enter element: "))
    arr1.append(num)
    print(arr1)
    
for i in range(n):
       arr2.append(arr1[i]) 
print("original array= ", arr1)
print("copied array= ", arr2)
