import csv

def load_iris():
    filepath = input('Prosze podac sciezke do pliku iris.csv : ')
    with open(filepath) as iris:
        mtx = csv.reader(iris, delimiter=",")
    return mtx


if __name__ == "__main__":
    filepath = r"C:\Users\Kajtek\OneDrive\Pulpit\ZadanieDomowe\Iris_data\iris.csv"
    with open(filepath) as iris:
        mtx = csv.reader(iris, delimiter=",")
        for row in mtx:
            print(row)