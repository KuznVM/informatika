# TODO решите задачу
import json

def sum_of_products()->float:
    with open("input.json",'r', encoding='utf-8') as file:
        data = json.load(file)
    result = 0.0
    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        result += score * weight
    return round(result, 3)
print(sum_of_products())
