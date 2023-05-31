i = 0

# while i < 7:
#     print(i)
#     i += 1

ls = [12, 16, 21]
i = 0
while i < len(ls):
    if ls[i] % 2 == 1:
        break

    print(2 * ls[i])
    i += 1
