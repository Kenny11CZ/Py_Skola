__author__ = 'Kenny'
"""
if 5==5:
    print"jo"
else:
    print "ne"

cislo=int(raw_input("Zadejte cislo: "))
print cislo+3

for i in range(0,5):
    print i

pole = [1,2,3]
retezec = "Ahoj"
print pole[1]

class Kohoutek():
    def __init__(self):
        self.tece = False

    def otoc(self):
        self.tece = not(self.tece)
        print self.tece

test = Kohoutek()
test.otoc()
"""
class Roura():
    def __init__(self, prumer=5):
        self.tece = True
        self.prumer = prumer

class Kohoutek(Roura):
    def otoc(self):
        print self.tece

test = Roura(20)
print test.prumer