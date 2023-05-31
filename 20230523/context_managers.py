rf = open('../texte/data.txt', 'w+')

try:
    data = rf.read()
    print(data)
    rf.write('ceva nou')
finally:
    rf.close()

