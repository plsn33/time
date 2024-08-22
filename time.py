from random import shuffle
from time import sleep
#Sortear times me um racha
quantidade_jogadores = int(input('Digite o número de jogadores que vão jogar: '))
nome_jogadores = []

for jogadores in range  (quantidade_jogadores):
        jogador  = input('Digite o nome dos jogadores: ')
        nome_jogadores.append(jogador)
shuffle(nome_jogadores)

sleep(2)

quantidade_times = int(input('Digite o número de times: '))

if quantidade_times <=  0:
    print('Número de times deve ser maior que zero')
elif quantidade_times > quantidade_jogadores:
    print('Número de jogadores não pode ser maior que o número de jogadores')
else:
    times = [nome_jogadores[i::quantidade_times] for i in range(quantidade_times)]

for i, time in enumerate(times, 1):
    print(f'Time {i}: {", ".join(time)}')





    
