import math

co = float(input("valor do cateto oposto: "))
ca = float(input("valor do cateto adjascente: "))

hi = (co**2 + ca**2) ** (1/2)

print("o valor da hipotenusa é {:.2f}".format(hi))