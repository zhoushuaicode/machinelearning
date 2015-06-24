#_*_coding:utf-8_*_
import numpy as np
def testresult(testset,result):
    testlist=[testset.ix[i,'class'] for i in testset.index]
    #resultlist=np.array(result)
    boolset=[]
    for i in range(len(result)-1):
        if result[i]==testlist[i]:
            boolset.append(True)
        else:
            boolset.append(False)
    cal=np.array(boolset)
    ratio=(float((cal>0).sum())/float(len(result)))*100

    return ratio
    

