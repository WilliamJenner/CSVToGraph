import csv_factory

class factory:
    def __init__(self, path, rowNum):
        self.path = path
        self.rowNum = rowNum
        self.csv = csv_factory.factory(path)
        self.data = self.csv.data
        self.size = self.csv.dataSize
        self.testName = ""
        self.collectionSize = initCollectionSize(self.csv.collectionSize)
        self.y = initY(self)

# Removes the first element from the list, then turns it into an int list so that it can be plotted
def initCollectionSize(colList):
    del colList[0]
    toInt = lambda x : int(x)
    return list(map(toInt, colList))

# Creates a list, y, for the y axis containing the times from the given CSV file
def initY(self):
    y = []
    for i in range(self.size):
        if i == 0:
            self.testName = self.data[i][self.rowNum]
        else: 
             y.append(self.data[i][self.rowNum])
    return y