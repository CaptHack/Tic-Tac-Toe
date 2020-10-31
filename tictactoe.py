import sys
board={'a1': ' ','a2': ' ','a3': ' ','b1': ' ','b2': ' ','b3': ' ','c1': ' ','c2': ' ','c3': ' '}

def pBoard(Board):
    print(Board['a1'], ' | ',Board['a2'], ' | ',Board['a3'], )
    print('---|-----|---')
    print(Board['b1'], ' | ',Board['b2'], ' | ',Board['b3'], )
    print('---|-----|---')
    print(Board['c1'], ' | ',Board['c2'], ' | ',Board['c3'], )

p1=input("Enter the name of player 1 :")
print(p1, 'will mark X')
p2=input("Enter the name of player 2 :")
print(p2, 'will mark 0')
check='X'
for i in range(9):
    while True:
        choice=input('Enter :')
        if choice not in board.keys():
            continue
        else:
            if board[choice]==' ':
                break
            else:
                continue
        
    if choice in board.keys():
        if board[choice]==' ':
            
            board[choice]=check
            if check=='X':
                check='0'
            else:
                check='X'
            if board['a1']==board['a2']==board['a3']=='X' or board['b1']==board['b2']==board['b3']=='X'or board['c1']==board['c2']==board['c3']=='X' or board['a1']==board['b2']==board['c3']=='X' or board['a3']==board['b2']==board['c1']=='X' or board['a1']==board['b1']==board['c1']=='X' or board['a2']==board['b2']==board['c2']=='X':
                pBoard(board)
                print(p1, 'won the game')
                end=input("Press 'Enter' to quit")
                sys.exit()
            if board['a1']==board['a2']==board['a3']=='0' or board['b1']==board['b2']==board['b3']=='0'or board['c1']==board['c2']==board['c3']=='0' or board['a1']==board['b2']==board['c3']=='0' or board['a3']==board['b2']==board['c1']=='0' or board['a1']==board['b1']==board['c1']=='0' or board['a2']==board['b2']==board['c2']=='0':
                pBoard(board)
                print(p2, ' won the game')
                end=input("Press'Enter' to quit")

                sys.exit()
    pBoard(board)
