culori = {
    'alb',
    'rosu',
    'albastru',
    'verde'
}

culori.add('galben')
culori.remove('rosu')

print(culori)
# print(culori[0]) - genereaza eroare

if 'albastru' in culori:
    print('Avem albastru')
else:
    print('Nu avem albastru')

if 'rosu' in culori:
    print('Avem rosu')
else:
    print('Nu avem rosu')

