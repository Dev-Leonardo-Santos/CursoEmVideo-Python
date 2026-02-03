print('{:=^50}'.format(' EXE 038 '))

print('{:^50}'.format('Vamos comparar os números'), end = '\n\n')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo  número: '))
if n1 > n2:
    print(f'O número {n1} é MAIOR')
elif n2 > n1:
    print(f'O número {n2} é MAIOR')
else:
    print('NÃO EXISTE número maior, os dois números são iguais.')
print(end = '\n')

print('=' * 50)
