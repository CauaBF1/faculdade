class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):  
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):  # divisão com decimal == truediv
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def __str__(self):  # Sobrecarrega print
        return f"{self.real} + {self.imag}i"


z1 = Complex(2, 3)
z2 = Complex(4, 2)


soma = z1 + z2
subtracao = z1 - z2
multiplicacao = z1 * z2
divisao = z1 / z2

# Imprimindo os resultados
print("z1:", z1)
print("z2:", z2)
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
