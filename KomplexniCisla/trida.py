import math
class Complex():
    def __init__(self, cela_slozka = 0, imaginarni_slozka = 0):
        self.real = cela_slozka
        self.imag = imaginarni_slozka
    def velikost(self):
        vector = math.sqrt((self.real*self.real)+(self.imag*self.imag))
        return vector
    def sdruzene(self):
        return Complex(self.real, -self.imag)
    def __str__(self):
        if self.imag>0:
            result = str(self.real) + " + " + str(self.imag) + "i"
        elif self.imag == 0:
            result = str(self.real)
        else:
            result = str(self.real) + " - " + str(-self.imag) + "i"
        return result
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)