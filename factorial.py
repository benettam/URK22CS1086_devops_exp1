def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
print("This is from the feature branch.")
