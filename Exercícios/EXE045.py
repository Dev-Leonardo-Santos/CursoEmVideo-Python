print('{:=^50}'.format(' EXE 045 '))
import random

maquina = random.choice(['pedra','papel','tesoura'])
print('{:-^50}'.format(' JOGO PEDRA, PAPEL E TESOURA '))
jogador = int(input('''Escolha a sua jogada:
[1] Pedra
[2] Papel
[3] Tesoura
R: '''))
if not (jogador == 1 or jogador == 2 or jogador == 3 ):
    print('JOGADA ERRADA! Não existe essa jogada.')
# Jogadas pedra.
if maquina == 'pedra' and jogador == 1:
    print('EMPATE')
elif maquina == 'pedra' and jogador == 2:
    print('JOGADOR VENCEDOR')
elif maquina == 'pedra' and jogador == 3:
    print('MAQUINA VENCEDORA')
# Jogadas papel

