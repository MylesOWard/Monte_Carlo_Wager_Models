import matplotlib.pyplot as plt
import csv

def graph():
    with open('monteCarlo.csv','r') as montecarlo:
        datas = csv.reader(montecarlo, delimiter=',')
        for eachLine in datas:
            percentROI = float(eachLine[0])
            wagerSizePercent = float(eachLine[1])
            wagerCount = float(eachLine[2])
            pcolor = eachLine[3]

            plt.scatter(wagerSizePercent,wagerCount,color=pcolor)

    plt.show()
            
graph()
