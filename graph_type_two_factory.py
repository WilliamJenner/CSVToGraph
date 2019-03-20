import matplotlib.pyplot as plt
import plot_factory
import numpy as np

class graphTypeTwo:
        def __init__(self, paths, operNum):
                self.paths = paths
                self.operNum = operNum

# Plots all types for an operation
def genTypesPlot(self):
        plt.xlabel('Collection Size')
        plt.ylabel('Time (ms)')
        testName = ""
        for path in self.paths:
                plot = plot_factory.factory(path, self.operNum)
                if (np.isnan(plot.y[0]) == False):
                        plt.plot(plot.collectionSize, plot.y, label=path)
                        testName = plot.testName
        plt.title(testName)
        plt.legend()
        plt.savefig(testName + '.png')
        plt.clf()
