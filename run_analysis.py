from iris_analysis.io.load import load_iris
from iris_analysis.io.save import save
from iris_analysis.calculate import *

if __name__ == "__main__":

    data = load_iris()

    stats = []
    stats.append( ["statistic" ] + data[0][:-1] )

    data = France1799(data)

    stats.append( ["means"     ] + means(data)      )
    stats.append( ["variances" ] + variances(data)  )
    stats.append( ["medians"   ] + medians(data)    )

    print( stats )

    save( stats , "output.csv" )