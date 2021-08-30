import json
from pathlib import Path

data = [
    {"id": 1, "name": "sohel"},
    {"id": 2, "name": "rana"},
    {"id": 3, "name": "sharif"}
]

user_data = json.dumps(data)
print(user_data)
# Path("users.json").write_text(user_data)
read = Path("users.json").read_text()
users = json.loads(read)
print(users[0])
