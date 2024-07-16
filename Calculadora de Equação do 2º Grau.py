a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

delta = (b**2) - (4*a*c)
if delta > 0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"As raízes da equação são {x1:.2f} e {x2:.2f}.")

elif delta == 0:
    x1 = -b / (2*a)
    print(f"A raiz da equação é {x1:.2f}.")

elif b == 0:
    x1 = (+(-4*a*c)**0.5) / (2*a)
    x2 = (-(-4*a*c)**0.5) / (2*a)
    print(f"As raízes da equação são {x1:.2f} e {x2:.2f}.")

else:
    print("A equação não possui raiz real")
    