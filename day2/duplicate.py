#n = int(input("Enter number of element: "))

def rachit(n):
    arr = []
    for i in range(n):
        x = int(input("Enter element: "))
        arr.append(x)
        print(x)
    for i in range(n):
        a = arr[i]       
        for j in range(i+1, n):
            b = arr[j]           
            if a == b:
                print("Duplicate number is:", a)
                break

rachit(5)
rachit(7)
rachit(10)
rachit(12)