#generamos una secuencia de números impares
from math import factorial, sin , pi

num_terminos = 1000
x= 0
resultado = 0
for i in range(num_terminos):
    exponente = (2*i+1)
    signo = (-1)**i
    termino = signo*(x** exponente) / factorial(exponente)
    resultado += termino

seno_math = sin(x)
print(f"sen{x} = {resultado} ----- debe dar {seno_math*180 / pi}")