class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self, area):
        self.area = self.base * self.altura

    def perimetro(self, perimetro):
        self.perimetro = (self.base * 2) + (self.altura * 2)


r1 = Retangulo(0, 0)
r1.base = int(input("Digite a medida da BASE do retangulo "))
r1.altura = int(input("Digite a medida da ALTURA do retangulo "))

print("Para este retangulo temos: ")
r1.area(0)
print("Medida da AREA do retangulo: ", r1.area)
r1.perimetro(0)
print("Medida do PERIMETRO do retangulo: ", r1.perimetro)

