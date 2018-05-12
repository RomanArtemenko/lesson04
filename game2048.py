from core import game as g

def main():
    game = g.Game(4)
 
    while True:
        field = game.get_field()
        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))
 
        print("\033[H\033[J", end="")
        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(cell).rjust(cell_width)
                for cell in row
            )
            for row in field
        ))
 
        if not game.has_moves():
            print("No available moves left, game over.")
            break
 
        print("L, R, U, D - move")
        print("Q - exit")
 
        try:
            c = input("> ")
        except (EOFError, KeyboardInterrupt):
            break
 
        if c in ('l', 'L'):
            game.move_left()
        elif c in ('r', 'R'):
            game.move_right()
        elif c in ('u', 'U'):
            game.move_up()
        elif c in ('d', 'D'):
            game.move_down()
        elif c in ('q', 'Q'):
            break
 
    print("Bye!")
 
 
if __name__ ==  '__main__':
    main()