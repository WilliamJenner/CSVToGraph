import os
import sys
import pandas as pd 

class factory:
    def __init__(self, path):
        # Set directory to local
        os.chdir(os.path.dirname(sys.argv[0]))
        self.path = path
        self.data = createDataList(self)
        self.dataSize = len(self.data)
        self.collectionSize = createHeaders(self)

def createDataList(self):
    df = pd.read_csv(self.path, sep=",")
    data = []
    for x in range(df.columns.size):
        data.append(df[df.columns[x]].tolist())
    return data

def createHeaders(self):
    collectionSize = pd.read_csv(self.path, nrows=0)
    sizes = []
    for i in range(len(collectionSize.columns)):
        sizes.append(collectionSize.columns[i])
    return sizes


#data[0][5] 0 refers to column. 5 refers to row
#print(data[4][1])
#print(data)
#collectionSizeHeaders[2] would = 10000
#print(collectionSizeHeaders[2])



