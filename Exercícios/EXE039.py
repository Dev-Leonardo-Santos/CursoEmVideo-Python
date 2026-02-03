from datetime import date

print('{:=^50}'.format(' EXE 039 '), end = '\n\n')

print('{:-^50}'.format(' ALISTAMENTO MILITAR '))
nome = input('Nome: ').title().strip()
ano_nas = int(input('ano de nascimento: '))
hoje = date.today()
ano_atu = hoje.year
idade = ano_atu - ano_nas
if idade == 18:
    print(f'{nome}, esta na hora de se alistar e servir a patria!')
elif idade < 18:
    dif = 18 - idade
    print('Ainda não esta na hora de se alistar.')
    print(f'Falta {dif} anos para os seu alistamento.')
else:
    resp = input('Voce ja se apresentou para o serviço militar? [S/N] ').upper()
    if resp == 'N':
        dif = idade - 18
        print(f'Voce está em atrado {dif} anos! procure a Junta de Serviço Militar!')
    elif resp == 'S':
        print('Voce está em dia com a pátria!')
    else:
        print('Resposta inválida. Use S ou N.')

print('-' * 50)
    
print('=' * 50)