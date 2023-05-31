x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

suma_unghiuri = x + y + z

# Verificarea ca este triunghi.
# Trebuie ca toate sa fie fiecare in parte mai mare ca 0, nu conteaza care e ordinea intre ele.
# Nu putem folosi scurtatura x >= y >= z > 0 pentru ca inpune o ordine intre unghiuri.

nu_e_ascutitunghic = False
if suma_unghiuri == 180 and x > 0 and y > 0 and z > 0:
    str_triunghi = 'Triunghiul este'

    # acum verificam cazurile particulare in functie de masura maxima a unghiului
    if x > 90 or y > 90 or z > 90:
        str_triunghi += ' obtuzunghic'
        nu_e_ascutitunghic = True
    elif x == 90 or y == 90 or z == 90:
        str_triunghi += ' dreptunghic'
        nu_e_ascutitunghic = True

    # acum verificam cazurile particulare in functie de relatia dinre unghiuri
    if x == y == z:
        str_triunghi += ' echilateral.'
    elif x == y or y == z or x == z:
        str_triunghi += ' isoscel.'
    elif not nu_e_ascutitunghic:
        str_triunghi += ' oarecare.'
    else:
        str_triunghi += '.'

    print(str_triunghi)
else:
    print('Nu este triunghi.')
