
# n =int(input("Enter number of terms: "))
def fab(n):
    a = 0
    b = 1
    print("Fibonacci Series:")
    for i in range(n):
        # print(a)
        a, b = b, a + b
    return a,b

print(fab(7))
print(fab(10))
print(fab(17))
print(fab(12))
print(fab(5))
a = [1,2,3,5,6,61,1]
print(sum(a))