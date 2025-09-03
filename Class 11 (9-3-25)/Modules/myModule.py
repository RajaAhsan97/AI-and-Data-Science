# MyModule file

# Multiply
def multiply(a,b):
    return a * b

# Compute Factorial
def fact(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1

    return result

# square root
def square_root(n):
    return n ** 0.5

# Euclidean distance

def Euclidean_dist(p, q):
    distance = square_root((q[0] - p[0])**2 + (q[1] - p[1])**2)
    return distance
