users = [
    (0, "Bob", "password"),
    (1, "Lisa", "121212"),
    (2, "Homer", "123456")
]

username_mapping = {user[1] : user for user in users}

print(username_mapping)

print(username_mapping["Lisa"])