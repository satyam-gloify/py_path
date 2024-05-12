import pandas as pd

class MyAnalytics(object):
    def __init__(self,records):
        self.mypanda =pd.DataFrame.from_dict(records)
      
    def getDataby(self,operator,operand):
        return self.mypanda.groupby([operator])[operand].count().reset_index()