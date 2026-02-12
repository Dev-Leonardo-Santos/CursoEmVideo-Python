print('{:=^50}'.format(' EXE 043 '), end = '\n\n')

print('{:-^50}'.format('Calculando IMC'))
altura = float(input('altura: '))
peso = float(input('Peso: '))
imc = peso / (altura * altura)
if imc < 18.5:
  print('Abaixo do peso')
elif imc < 25:
  print('Peso ideal')
elif imc < 30:
  print('Sobrepeso')
elif imc < 40:
  print('Obesidade')
else:
  print('Obesidade mórbida')
print(('-' * 50), end = '\n')
print('=' * 50)