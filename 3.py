import random
import json
import string

names = ["Mikhail Pukhov", "Gleb Borisovich", "Max Siniy", "Andrey Ivanov"]
emails = ["mikh@example.com", "gleb.b@example.com", "maxss@example.com", "aivanov@example.com"]

password_chars = string.ascii_letters + string.digits + string.punctuation
generated_password = "".join(random.choices(password_chars, k=12))

user_data = {
    "name": random.choice(names),
    "age": random.randint(18, 65),
    "email": random.choice(emails),
    "password": generated_password
}

filename = "user_info.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(user_data, f, indent=4, ensure_ascii=False)

with open(filename, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(json.dumps(loaded_data, indent=4, ensure_ascii=False))