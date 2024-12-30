'''
ListaDeClientes
Criado Por: O BRUXO PYTHON
13/12/2024
'''

Lista = []

print("lista de Convidados")

while True:

    EntradaDeNome = str(input("Digite Nomes Para Lista"))

    Lista.append(EntradaDeNome)

    for i in Lista:

        print(i)

    NovoNome =  str(input("Clique em Enter Para Continuar. E Qualquer Tecla + ENTER Para Sair"))

    if NovoNome == "" or  NovoNome=="":
        print("------------------------")


    else:
        print(Lista)
        break