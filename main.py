#_*_coding:utf-8_*_
import pandas as pd
import loaddata,classify,datasetplot,testresult
import numpy as np
import matplotlib.pyplot as plt
def main(filename,ratio,k):
    trainset=pd.DataFrame()
    testset=pd.DataFrame()
    dataset=pd.DataFrame()
    trainset,testset,dataset=loaddata.loadDataset(filename,ratio,trainset,testset)
    #datasetplot.datasetplot(dataset)
    #datasetplot.datasetplot(trainset)
    #datasetplot.datasetplot(testset)
    result=classify.classify(trainset,testset,k)
    #print 'The result is:\n',result
    #print 'The result accuracy rate is:',testresult.testresult(testset,result),'%'
    return testresult.testresult(testset,result)
	
if __name__=="__main__":
    #resultset=pd.DataFrame()
    accuracy=[]
    for i in range(1):
        #for j in range(20):
        accuracy.append(main('iris.data',0.67,i+1))
    mean=np.array(accuracy).mean()
    print mean
    #print accuracy
    #plt.plot(accuracy)
    #plt.show()
    #resultset['accuracy rate']=accuracy
    #resultset['ratio']=[(float(j)+1)/20 for j in range(20)]
    #resultset['k value']=[i+1 for i in range(20)]
    #resultset.plot()
    #print resultset
    #return accuracy  
    


	

    
    
    
     