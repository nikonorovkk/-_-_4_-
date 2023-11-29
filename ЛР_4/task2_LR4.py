import json
import csv
# TODO импортировать необходимые молули

input_filik = "input.csv"
ouput_filik = "output.json"

def point() -> None:
    with open(input_filik) as file:
        lines = [line for line in csv.DictReader(file)]
    # TODO считать содержимое csv файла

    with open(ouput_filik, "w") as file:
        json.dump(lines, file, indent=4)
    # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    point()

    with open(ouput_filik) as output_f:
        for line in output_f:
            print(line, end="")