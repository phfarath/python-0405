qi=7981
cont=0
try:
    while qi!= 0:
        print("digite o qi aqui:")
        qi=int(input())
        if qi >140:
            cont+=1
        elif qi >0 and qi<140:
            continue
        elif qi==0:
            print("acabou")
            break
    print(f'voce digitou {cont} genios')
except ValueError:
    print("so é aceito numeros inteiros!")

