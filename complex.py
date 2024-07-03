class Complex:
    def __init__(self, real = 0, img = 0):
        self.real = real
        self.img = img
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)
    
    def __mul__(self, other):
        return Complex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)

    def __truediv__(self, other):
        r = other.real ** 2 + other.img ** 2
        return Complex((self.real * other.real + self.img * other.img) / r, (self.img * other.real - self.real * other.img) / r)
    
    def __str__(self):
        return f"{round(self.real, 2)} + {round(self.img, 2)}i"
    
    def __repr__(self):
        return f"Complex({self.real}, {self.img})"


z1 = Complex(1, 2)
z2 = Complex(2, 3)

print(z1)
print(z2)
print(z1 + z2)
print(z1 - z2)
print(z1 * z2)
print(z1 / z2)
