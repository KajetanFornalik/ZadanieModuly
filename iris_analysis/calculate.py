from statistics import mean, variance, median

#Usuwanie wiersza z głowy (pierwszego wiersza z nazwami kolumn)
def France1799(mtx):
    return mtx[1:]


def means(mtx):
    gole = []
    col = []
    for i in range(len(mtx[0]) - 1): #bo nie chcemy liczyć tej wartosci dla ostatniej kolumny
        for row in mtx[1:]:
            col = col + [row[i]]
        gole = gole + [mean([float(x) for x in col])]
    return gole

def variances(mtx):
    gole = []
    col = []
    for i in range(len(mtx[0]) - 1):  # bo nie chcemy liczyć tej wartosci dla ostatniej kolumny
        for row in mtx[1:]:
            col = col + [row[i]]
        gole = gole + [variance([float(x) for x in col])]
    return gole

def medians(mtx):
    gole = []
    col = []
    for i in range(len(mtx[0]) - 1):  # bo nie chcemy liczyć tej wartosci dla ostatniej kolumny
        for row in mtx[1:]:
            col = col + [row[i]]
        gole = gole + [median([float(x) for x in col])]
    return gole


if __name__ == "__main__":
    import load as ld
    data = ld.load_iris()
#C:\Users\Kajtek\OneDrive\Pulpit\ZadanieDomowe\Iris_data\iris.csv
    print(means(France1799(data)))
    print(variances(France1799(data)))
    print(medians(France1799(data)))


