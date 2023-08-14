
P = 10000
n = 12
r = 0.08
print("What is the number of years?")
t = int(input())
A = P * (1 + (r / n)) ** (n * t)
print("The final amount is", A)
