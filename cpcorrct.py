import random
sorteio= random.randint(1,5)
if sorteio ==1:
    nomefunc="pedro"
elif sorteio ==2:
    nomefunc="lucas"
elif sorteio ==3:
    nomefunc="joao"
elif sorteio==4:
    nomefunc="kleber"
else:
    nomefunc="rogerio"
print("bemvindo a vinheria")
print(f"quem te atendera sera {nomefunc}")
print("informe seu nome")
nome= input()
print("informe seu cep")
cep=input()
print("informe o seu ano de nascimento")
anonasc=int(input())
idade =2023 - anonasc
if idade<18:
    print(f'{nome} nao é permitida a sua entrada no site')
else:
    #exibir os vinhos
    subtotal=total=0
    #prep msg final
    msgfinal=f"dados da compra:\nAtendido por:{nomefunc}\nCliente:{nome}\nItens da compra\tValor\tQtde\tSubtotal\n"
    #repetindo a venda de vinhos
    continua="sim"
    while continua.lower()=="sim":
        #exibindo opcoes de vinho
        listavinhos=" Escolha um dos vinhos da lista:\n(1)Vinho suave tinto\tR$ 15.00\n(2)Vinho seco tinto\tR$ 25.00\n(3)Vinho Suave Branco\tR$ 35.00\n(4)Vinho seco branco\tR$ 45.00\n(5)Vinho sem alcool\tR$ 20.00"
        print(listavinhos)
        vinho=int(input())
        print("qual quantidade deseja?")
        quant=int(input())
        match vinho:
            case 1:
                subtotal=15 *quant
                msgfinal +=f"vinho suave tinto\tR$ 15.00\t{quant}\tR$ {subtotal:.2f}"
            case 2:
                subtotal=25 *quant
                msgfinal +=f"vinho seco tinto\tR$ 25.00\t{quant}\tR$ {subtotal:.2f}"
            case 3:
                subtotal=35 *quant
                msgfinal +=f"vinho suave branco\tR$ 35.00\t{quant}\tR$ {subtotal:.2f}"
            case 4:
                subtotal=45 *quant
                msgfinal +=f"vinho seco branco\tR$ 45.00\t{quant}\tR$ {subtotal:.2f}"
            case 5:
                subtotal=20 *quant
                msgfinal +=f"vinho sem alcool\tR$ 20.00\t{quant}\tR$ {subtotal:.2f}"
            case _:
                print("Escolha uma das opcoes por favor")
                subtotal =0
        #calculando o total da compra
        total += subtotal
        print("deseja continuar comprando?Sim ou Nao")
        continua=input()
    #exibir as info finais 
    print(msgfinal)
    print(f'Total da compra: R${total:.2f}')