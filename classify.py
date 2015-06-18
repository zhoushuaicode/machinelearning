import pandas as pd
import numpy as np
def classify(trainset,testset,k):
    trainlabel=pd.DataFrame(trainset['class'])
    testlabel=pd.DataFrame(testset['class'])
    trainfeatrue=trainset.drop('class',axis=1)
    testfeature=testset.drop('class',axis=1)
    for i in list(testfeature.index):      
        diff=trainfeatrue-testfeature.ix[i]
        sqdiff=diff**2
        sqdistance=sqdiff.sum(axis=1)
        distance=sqdistance**0.5
        sortofdis=distance.rank(method='first')
        indexlist=np.zeros(k)
        label=pd.DataFrame()
        count={}
        for i in range(k):
            indexlist[i]=sortofdis.idxmin()
            label=label.append(trainlabel.ix[sortofdis.idxmin()])
            #a=label.get_value(sortofdis.idxmin())
            #print a
            sortofdis=sortofdis.drop(sortofdis.idxmin())

            
            
            
            
           