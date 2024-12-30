
#importa a lib date, está lib pega a data do sistema
from datetime import date


data_atual = date.today()


list_nome =[]
str_codificando =''
Str_descodificando = ''


str_codificando = input("digite um texto para ser codificado!!\n")

#este laço le o input, e trasforma as letras digitadas, em código asc(números) através da função ord
for i in str_codificando:
    list_nome.append(ord(i))

print("\n\ntexto codificado:\n{}".format(list_nome))

#este laço pega os números e transforma em caracter, reconstruindo a frase
for i in list_nome:
    Str_descodificando+= chr(i)

    
print("\n\ntexto descodificado: {}\nNo texto digitado, o teclado foi acionado {} vezes!".format(Str_descodificando,len(Str_descodificando)))

#cria o arquivo de nome tatu extenção .txt
arquivo = open('tatu.txt','w')
#escreve a data da criação através da nossa lib importada
arquivo.write('data da criação:' + str(data_atual))
# pula uma linha
arquivo.write('\n')
#escreve no nosso arquivo criado a nossa senha
arquivo.write(Str_descodificando)
arquivo.close()

print('\n\nArquivo aberto')


#le o arquivo atraves do open
arquivo = open('tatu.txt','r')
#este laço le o arquivo
for i in arquivo:
    i = i.rstrip()
    print(i)
#facha o arquivo atraves do close
arquivo.close()
