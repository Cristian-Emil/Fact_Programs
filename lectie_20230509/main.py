from lectie_20230509.clasa_caine import Caine


def deseneaza_traseu(p, c):
    for i in range(10):
        line = ''
        for j in range(10):
            if p['x'] == j and p['y'] == i:
                line += '\033[38;5;198mP '
            elif c.x == j and c.y == i:
                line += '\033[38;5;100mC '
            else:
                line += '\033[38;5;255m. '

        print(line)
    print('- ' * 10)
    print()


p = {'x': 5, 'y': 7}
rex = Caine()

print(f'x: {rex.x} y: {rex.y}')
deseneaza_traseu(p, rex)
