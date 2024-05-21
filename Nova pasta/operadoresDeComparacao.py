'''
a == b	a igual a b
a!= b   a diferente de b
a < b	a menor	do que b
a > b 	a maior do que b
a <= b	a menor ou igual b
a >= b 	a maior	ou igual b

Outros operadores que retornam valores booleanos são:
a is b 		True se	a e b são idênticos
a is not b 	True se	a e b não são idênticos
a in b 		True se	a é membro de b
a not in b 	True se	a não é membro de b


'''

a = [1, 2, 3]
b = [1, 2, 3]
bb =3
print('\na==b ', a == b)

print('\na!= b ', a != b)

print('\na<b ', a < b)

print('\na>b ', a > b)

print('\na<=b ', a <= b)

print('\na>=b', a >= b)


print('\n\na is b ', a is b)
print('\na is not b ', a is not b)
print('\na in b ', a in b)
print('\na not in b ', a not in b)


print('\na is b ', a is bb)
print('\na is not b \n', a is not bb)
print('\na in b \n', a in bb)
print('\na not in b \n', a not in bb)
