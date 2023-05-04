senha =""
frase= "acesso concedido!"
cont =0
while senha != "p4ssw0rd":
    print(" digite a senha")
    senha = input()
    cont+=1
    if cont >=5 :
        frase = "conta bloqueada!"
        break
print(frase)