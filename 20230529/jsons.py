import json


with open('users.json', 'r') as f:
    # users = json.load(f)
    users_str = f.read()


users = json.loads(users_str)

print(type(users))

for user in users:
    print(user['adresa']['strada'])

users[1]['adresa']['strada'] = 'Bld. Muncii'

users_new_str = json.dumps(users)
print(type(users_new_str))
print(users_new_str)

with open('users.json', 'w') as f:
    # json.dump(users, f)
    f.write(users_new_str)
