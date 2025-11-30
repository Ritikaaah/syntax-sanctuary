class Complex:
    def __init__(self):
        self.real = int(input("Enter the real number: "))
        self.img = int(input("Enter the imaginary number: "))

    def show_number(self):
        if self.img < 0:
            print(f"{self.real} - {abs(self.img)}i")
        else:
            print(f"{self.real} + {self.img}i")

    def add(self, num2):
        return Complex.from_values(self.real + num2.real, self.img + num2.img)

    def sub(self, num2):
        return Complex.from_values(self.real - num2.real, self.img - num2.img)

    def mul(self, num2):
        real = self.real * num2.real - self.img * num2.img
        img = self.real * num2.img + self.img * num2.real
        return Complex.from_values(real, img)

    @classmethod
    def from_values(cls, real, img):
        obj = cls.__new__(cls)  
        obj.real = real
        obj.img = img
        return obj

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)


num1 = Complex()
num2 = Complex()

num3 = num1 + num2
num3.show_number()

num4 = num1 - num2
num4.show_number()

num5 = num1 * num2
num5.show_number()
