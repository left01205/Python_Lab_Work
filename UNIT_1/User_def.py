def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def multiply_numbers(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def calculate_area(length, width=1):
    return length * width

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Testing the functions
greet("Jatin")
print(add_numbers(5, 3))
print(multiply_numbers(2, 3, 4))
print(calculate_area(5))
print(calculate_area(5, 2))
print_info(name="Brijesh", age=25, city="Raipur")