def my_gen(x):
    n = 0

    while n < x:
        yield n
        n += 1


iterable = my_gen(10)
iterator = iter(iterable)

while True:
    try:
        current = next(iterator)
        # operations with current value

        print(current)
    except StopIteration:
        break

'''
Echivalent cu:

for key in iterable:
    print(key)
'''
