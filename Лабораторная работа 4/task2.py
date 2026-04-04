import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
# Чтение CSV
    with open(INPUT_FILENAME, newline="", encoding='utf-8') as source:
        csv_reader = csv.DictReader(source)
        for item in csv_reader:
            data.append(item)

# Запись JSON
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as target:
        json.dump(data, target, indent=4, ensure_ascii=False)



if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
