import matplotlib.pyplot as plt
import plot_factory
import numpy as np

class graphTypeOne:
        def __init__(self, path, title):
                self.path = path
                self.title = title

# Plots all operations for a type
def genPlot(self):
        plt.title(self.title)
        plt.xlabel('Collection Size')
        plt.ylabel('Time (ms)')
        for x in range(19):
                plot = plot_factory.factory(self.path, x)
                if (np.isnan(plot.y[0]) == False):
                        name = plot.testName
                        plt.plot(plot.collectionSize, plot.y, label=name)
        plt.legend()
        plt.savefig(self.title + '.png')
        plt.clf()
