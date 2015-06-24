#_*_coding:utf-8_*_
import pandas as pd
def datasetplot(dataset):
    color_wheel = {'Iris-virginica': "#0392cf",'Iris-setosa': "#7bc043",'Iris-versicolor': "#ee4035"}
    colors = dataset["class"].map(lambda x: color_wheel.get(x))
    pd.scatter_matrix(dataset,color=colors, alpha=0.6, figsize=(15, 15), diagonal='hist')
