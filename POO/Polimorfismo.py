import math

class Forma:    # classe mãe
    def calcular_area(self):
        return "Ainda não tenho uma lógica implementada para calcular esta área."
    
    def calcular_perimetro(self):
        return "Ainda não tenho uma lógica implementada para calcular este perímetro."

class Circulo(Forma):   # classe filha
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):            # polimorfismo do método da superclasse
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
    def redimensionar_raio(self, novo_raio):
        self.raio = novo_raio

class Retangulo(Forma):     # classe filha
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):        # polimorfismo do método da superclasse
        return self.base * self.altura
    
    def calcular_perimetro(self):       # polimorfismo do método da superclasse
        return 2 * (self.base + self.altura)
    
    def redimensionar_base(self, nova_base):
        self.base = nova_base
        
    def redimensionar_altura(self, nova_altura):
        self.altura = nova_altura
        
circulo1 = Circulo(3)
retangulo1 = Retangulo(10, 2)

print(circulo1.calcular_area())     # 28.274333882308138
print(circulo1.calcular_perimetro())    # 18.84955592153876
print(retangulo1.calcular_area())   # 20
print(retangulo1.calcular_perimetro())  # 24