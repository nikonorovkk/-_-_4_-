import json
# TODO решите задачу
def point() -> float:
    fname = "input.json"
    # Чтение данных из файла в формате JSON
    with open(fname) as file:
        data = json.load(file)
    sum_values = sum([item["score"] * item["weight"] for item in data])
    return round(sum_values, 3)
print(point())
