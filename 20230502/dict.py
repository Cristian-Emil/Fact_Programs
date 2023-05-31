car = {
    'brand': 'Ford',
    'model': 'Focus',
    'year': 2005
}

# car = dict()
# car['brand'] = 'Ford'
# car['model'] = 'Focus'
# car['year'] = 2005

print(f'Informatii masina: \n- brand: {car["brand"]}\n- model: {car["model"]}\n- year: {car["year"]}')

car['color'] = 'red'

print(f'- color: {car["color"]}')


print(car)
del car['model']
print(car)

if 'brand' in car:
    print(f'Brandul este {car["brand"]}')
else:
    print('Nu avem brand')

if 'weight' in car:
    print(f'Greutate este {car["weight"]}')
else:
    print('Nu avem acest camp')



