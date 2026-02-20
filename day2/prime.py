n = int(input("Enter number: ")) 
if n<=1 :
    print("it is not a prime")
else :
    for i in range(2,n): 
        if n%i == 0: 
            print("it is not prime") 
            break 
    else: 
        print("it is prime")