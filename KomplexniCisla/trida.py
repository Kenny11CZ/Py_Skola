import math

class Complex():
    def __init__(self, cela_slozka = 0, imaginarni_slozka = 0):
        self.real = cela_slozka
        self.imag = imaginarni_slozka
    def velikost(self):
        vector = math.sqrt((self.real**2)+(self.imag**2))
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
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __eq__(self, other):
        vysledek = (self.imag == other.imag) and (self.imag == other.imag)
        return vysledek
    def __gt__(self, other):
        return self.velikost() > other.velikost()
    def __lt__(self, other):
        return self.velikost() < other.velikost()
    def __del__(self):
        print("Good bye fellaz")


