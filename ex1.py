try :
    print("digite 2 numeros inteiros")
    num1= int(input())
    num2= int(input())
    print(f"adicao:{num1+num2}")
    print(f"subtracao:{num1-num2}")
    print(f"multiplicacao:{num1*num2}")
    print(f"divisao:{num1//num2}")
except ZeroDivisionError:
    print("erro!divisao por zero")
except ValueError:
    print("erro! somente numeros inteiros")