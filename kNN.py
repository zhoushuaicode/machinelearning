#_*_codeing:utf-8_*_
import pandas as pd
from pandas import DataFrame
import random
import numpy as np
def loadDataset(filename,split,trainset,testset):
    dataset=pd.read_csv('iris.data',names=['sepal length','sepal width','petal length','petal width','class'])
    #trainset=DataFrame()
    #testset=DataFrame()
    for x in range(len(list(dataset.index))-1):
        a=random.random()
        if a < split:
            trainset=trainset.append(dataset.ix[x])
        else:
            testset=testset.append(dataset.ix[x])	        
    return trainset,testset	       
#loadDataset('iris.data',0.67)