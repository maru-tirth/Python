n = int(input("Enter a number: "))
a = 0
b = 1
print("Fibonacci sequence up to", n, ":")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b