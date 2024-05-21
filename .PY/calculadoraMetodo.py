i = 0
tatu =''
while True:
    tatu = input("\n\n digite\n so para somar,\n d divisão,\n su subtração,\n m multiplicção")
    num01 = 0
    num02 = 0
    resultado = 0
    
#oldo codec a ser alterado por guilherme
    if tatu == ("so") or tatu == ("SO"):

        num01 = input ("digite um numero: ")
        num02 = input ("digite outro numero")
        print("resultado é: ", int(num01) + int(num02))
        
    if tatu == ("s") or tatu == ("S"):

        num01 = input ("digite um numero: ")
        num02 = input ("digite outro numero")
        print("resultado é: ", int(num01) + int(num02))

    if tatu == ("d") or tatu == ("D"):

        num01 = input ("digite um numero: ")
        num02 = input ("digite outro numero")
        print("resultado é: ", int(num01)/ int(num02))

    if tatu == ("su") or tatu == ("SU"):

        num01 = input ("digite um numero: ")
        num02 = input ("digite outro numero")
        print("resultado é: ", int(num01) - int(num02)) 

    if tatu == ("m") or tatu == ("M"):

        num01 = input ("digite um numero: ")
        num02 = input ("digite outro numero")
        print("resultado é: ", int(num01) * int(num02))
      
    tatu = ""
    print(tatu)
    
    tatu1 = input("digite S para um novo calculo ou N para sair")

    if tatu1 == "s" or tatu1 == "S" :

        print("teste")


    else:

        
        break


def soma (num01 num02):

    print (num01 + num02)
