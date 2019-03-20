import matplotlib.pyplot as graph
import graph_type_one_factory
from graph_type_one_factory import genPlot
import graph_type_two_factory
from graph_type_two_factory import genTypesPlot
import numpy as np

# File paths of all the csv files to generate graphs from. 
# Could probably be automated to read every .csv file in the directory
filePaths = ['ArrayDeque_test.csv', 'ArrayList_test.csv', 
            'HashMap_test.csv', 'HashSet_test.csv', 
            'LinkedHashMap_test.csv', 'LinkedHashSet_test.csv', 
            'LinkedList_test.csv', 'TreeMap_test.csv' ,
            'TreeSet_test.csv']

# Generates type one graphs, plotting all operations for a type
for path in filePaths:
    title = path[:-9]
    genPlot(graph_type_one_factory.graphTypeOne(path, title))

# Generates type two graphs, plotting all types for an operation
for x in range (19):
    genTypesPlot(graph_type_two_factory.graphTypeTwo(filePaths, x))