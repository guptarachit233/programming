def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("No Factorial")
else:
    print(fact(num))