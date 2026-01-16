def add(a, b):
    return a + b

def greet(name="Student"):
    return "Hello, " + name

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Testing functions
print("Add 10 + 5 =", add(10, 5))
print(greet("Basava"))
print("Is 8 even?", is_even(8))
