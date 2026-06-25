import random as r

mylist = ['STONE', 'PAPER', 'SCISSOR']

player1 = r.choice(mylist)
player2 = r.choice(mylist)

print(f'PLAYER 1 - {player1}')
print(f'PLAYER 2 - {player2}')

if player1 == player2:
    print('MATCH DRAW')
elif player1 == 'STONE' and player2 == 'SCISSOR':
    print('PLAYER 1 WINS')
elif player1 == 'SCISSOR' and player2 == 'PAPER':
    print('PLAYER 1 WINS')
elif player1 == 'PAPER' and player2 == 'STONE':
    print('PLAYER 1 WINS')
else:
    print('PLAYER 2 WINS')
