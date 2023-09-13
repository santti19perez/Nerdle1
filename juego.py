"""
Nerdle.py
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _

Operacion == Intento -> Ganar!
Simbolo in Operacion -> Ayuda!
Simbolo not in Operacion -> No Existe!
"""

colors = {
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'ENDC': '\033[0m',
 }

def color_letter(letter,color):
    return colors[color] + letter + colors['ENDC']



# init game
print("Nerdle.py empezar!")

win = False
Operacion = '8x4=36'
board = []
for i in range(6):
    board.append(['_' for l in range(6)])

game_loop_counter = 0
while (not win) and ():
    text = input("")
    while len(text) != len(Operacion):
        print(f"la operacion debe tener {len(Operacion)} de caracteres")
        text = input("")

    #win logic
    if Operacion == text:
        board[game_loop_counter] = [l for l in text]
        win = True

    #letter in word

    else:
        test_line = []
        for j in range(len(Operacion)):
            if text[j] == Operacion[j]:
             if text[j] in Operacion:
                 test_line.append(text[j])
            elif text[j] in Operacion:
                test_line.append(color_letter(text[j],'yellow'))

            else:
                test_line.append(color_letter(text[j], 'red'))
        board[game_loop_counter] = test_line

    # Draw
    for i in range(6):
        print(" ".join(board[i]))

    game_loop_counter += 1