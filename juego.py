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

# init game
print("Nerdle.py empezar!")

win = False
Operacion = '8x4=36'
board = []
for i in range(6):
    board.append(['_' for l in range(6)])

game_loop_counter = 0
while not win:
    text = input("")
    while len(text) != len(Operacion):
        print(f"la operacion debe tener {len(Operacion)} de caracteres")
        text = input("")

    #win logic
    if Operacion == text:
        board[game_loop_counter] = [l for l in text]
        win = True

    # Draw
    for i in range(6):
        print(" ".join(board[i]))

    game_loop_counter += 1