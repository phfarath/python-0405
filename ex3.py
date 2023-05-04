import math
a=b=c=0
try:
    print("digite o valor de a:")
    a=int(input())
    print("digite o valor de b:")
    b=int(input())
    print("digite o valor de c:")
    c=int(input())
    delta= b**2-4*a*c
    if delta >=0:
        x1= (-b+math.sqrt(delta))/2*a
        x2= (-b-math.sqrt(delta))/2*a
        print(f'seu delta foi {delta}')
        print(f'seu x1 foi igual a :{x1}')
        print(f'seu x2 foi igual a :{x2}')
    else:
        print("delta negativo, impossivel continuar. Seu delta foi de", delta)
except ValueError:
    print("somente numeros inteiros!")

