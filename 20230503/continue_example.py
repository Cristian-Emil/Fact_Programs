# `depozite` este o lista cu mai multe obiecte de tip dictionar.
# Fiecare contine date despre depozitul unei anumite persoane:
#  - nume: string
#  - suma: int/float
#  - tip_depozit: int (1, 2 sau 3)

depozite = [
    {
        'nume': 'Marian',
        'suma': 100,
        'tip_depozit': 1
    },
    {
        'nume': 'Cristina',
        'suma': 200,
        'tip_depozit': 3
    },
    {
        'nume': 'Liana',
        'suma': 60,
        'tip_depozit': 2
    },
    {
        'nume': 'Adi',
        'suma': 100,
        'tip_depozit': 2
    }
]

# Vom calcula suma finala a fiecarui client al bancii dupa ce au trecut 1 luna
# Regulile sunt:
# - tipul de depozit este 1, atunci primeste 5% daca sume este mai mic decat 100 RON, 6% altfel
# - tipul de depozit este 2, atunci primeste 5% daca suma este sub 100 RON, si 7% in caz contrar
# - tipul de depozit este 3, atunci primeste 5% daca suma este sub 100 RON, si 8% alfel
# - aditional, orice tip de depozit primeste un bonus de 50 de lei lunar daca are minim 200 RON

# aici depozit reprezinta, pe rand, fiecare dict din lista de depozite
# varianta 1
for depozit in depozite:
    # suma mai mica decat 100 => toata lumea primeste aceeasi dobanda
    if depozit['suma'] < 100:
        depozit['suma'] += depozit['suma'] * 0.05
    else:
        # tinem minte suma initiala pentru a stabili ulterior daca aplicam un bonus
        suma_initiala = depozit['suma']

        # dobanda in functie detipul de cont
        if depozit['tip_depozit'] == 1:
            depozit['suma'] += depozit['suma'] * 0.06
        elif depozit['tip_depozit'] == 2:
            depozit['suma'] += depozit['suma'] * 0.07
        else:
            depozit['suma'] += depozit['suma'] * 0.08

        # verificam daca se aplica bonusul
        if suma_initiala >= 200:
            depozit['suma'] += 50

# varainta 2
for depozit in depozite:
    # suma mai mica decat 100 => toata lumea primeste aceeasi dobanda
    if depozit['suma'] < 100:
        depozit['suma'] += depozit['suma'] * 0.05
        continue

    # tinem minte suma initiala pentru a stabili ulterior daca aplicam un bonus
    suma_initiala = depozit['suma']

    # dobanda in functie detipul de cont
    if depozit['tip_depozit'] == 1:
        depozit['suma'] += depozit['suma'] * 0.06
    elif depozit['tip_depozit'] == 2:
        depozit['suma'] += depozit['suma'] * 0.07
    else:
        depozit['suma'] += depozit['suma'] * 0.08

    # verificam daca se aplica bonusul
    if suma_initiala >= 200:
        depozit['suma'] += 50

# Dupa cum se observa, prin folosierea instructiunii continue, am evitat folosirea mai multor nivele
#   de if(nested ifs), una dintre ramuri fiind foarte putin complexa, iar astfel codul arata mai clean
