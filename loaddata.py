#_*_codeing:utf-8_*_
import pandas as pd
import random
def loadDataset(filename,split,trainset,testset):
    dataset=pd.read_csv(filename,names=['sepal length','sepal width','petal length','petal width','class'])
    for x in range(len(list(dataset.index))):
        a=random.random()
        if a < split:
            trainset=trainset.append(dataset.ix[x])
        else:
            testset=testset.append(dataset.ix[x])       
    return trainset,testset,dataset	       
#loadDataset('iris.data',0.67)