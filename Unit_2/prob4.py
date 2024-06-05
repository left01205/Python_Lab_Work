class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Create two complex numbers
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(4, 5)

# Add the complex numbers
result = num1 + num2

# Print the result
print(result)