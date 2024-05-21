'''
manipulando strings

'''


texto1 = 'oi'
texto2 = 'mundo'
texto3 = '!!!!'


#concatenando strings, ou seja, juntando duas ou mais strings:
print(texto1+texto2+texto3,'\n')

#O operador * também funciona com strings, multiplicando seu conteúdo por um inteiro
print(texto1*5+texto2*5+texto3*5,'\n')
print((texto1+texto2+texto3)*5,'\n')
print('{},{},{}\n'.format(texto1,texto2,texto3))
print('{2},{0},{1}\n'.format(texto1,texto2,texto3))
print('declarando uma variavel \n{0},{1},{2} e {x}\n'.format(texto1,texto2,texto3, x = 123 * 5))

print('upper \n',texto1.upper(),texto2.upper(),texto3)

print('\ncapitalize deixa a primeira letra maiúscula\n',texto1.capitalize(),texto2.capitalize(),texto3)

x = 245.2346454
print('\nformatando o numero {}, para duas casa decimais '.format(x))
#O :.2f diz que queremos apenas duas casas decimais para a variável
print('{:.2f}'.format(x))

