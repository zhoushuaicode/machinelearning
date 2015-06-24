import pandas as pd
import numpy as np
import operator
def classify(trainset,testset,k):
    trainlabel=pd.DataFrame(trainset['class'])
    #testlabel=pd.DataFrame(testset['class'])
    trainfeatrue=trainset.drop('class',axis=1)
    testfeature=testset.drop('class',axis=1)
    result=list()
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
            #print label.ix[sortofdis.idxmin(),'class']
            count[label.ix[sortofdis.idxmin(),'class']]=count.get(label.ix[sortofdis.idxmin(),'class'],0)+1
            sortofdis=sortofdis.drop(sortofdis.idxmin())
        sortedcount=sorted(count.iteritems(),key=operator.itemgetter(1),reverse=True)
        #return sortedcount[0][0]
        #print sortedcount[0][0]
        result.append(sortedcount[0][0])
    #print result
    return result
    

            
            
            
            
           