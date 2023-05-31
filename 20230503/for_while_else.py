ls = [12, 16, 21, 34]
# i = 0
#
# while i < len(ls):
#     if ls[i] % 2 == 1:
#         break
#
#     print(2 * ls[i])
#     i += 1
# else:
#     print('Am parcurs toata lista')
#
# print('Salutare')

for elem in ls:
    if elem % 2 == 1:
        break

    print(2 * elem)
else:
    print('Am parcurs toata lista')

print('Salutare')
