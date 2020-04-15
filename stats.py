# program to perform statistical operations
import io
import statistics as stat

class Stats:
    def __init__(self, dataset_x, dataset_f):
        self.xi = dataset_x
        self.fi = dataset_f
    
    def getSetValues(self):
        pass
        self.computedSet = []
        for i in range(len(self.xi)):
            self.computedSet.append(self.xi[i] * self.fi[i])
    
    def generateStatisticalData(self):
        pass
        print("Mean> " + str(stat.mean(self.computedSet)))
        print("Median> " + str(stat.median(self.computedSet)))
        print("Variation> " + str(stat.variance(self.computedSet)))
        print("Standard Deviation> " + str(stat.stdev(self.computedSet)))
        
''' main function unit '''
class_mark_set = [4, 5, 7, 3, 8, 9, 1, 2]
frequency_set =  [2, 6, 7, 5, 6, 8, 4, 3]
stat_generator = Stats(class_mark_set, frequency_set)
stat_generator.getSetValues()
stat_generator.generateStatisticalData()        
        
