import json

for _ in range(1000):
    with open('data.json') as file:
        text = file.read()

    data = json.loads(text)

    for d in data:
        print(d["Name"],",",list(d['marks'].keys())[-1])

