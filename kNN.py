import numpy as np
import matplotlib.pyplot as plt
import operator
class kNN():
    def createdata(self):
        # 六组二维特征
        group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
        # 六组特征的标签
        labels = ['爱情片', '爱情片', '爱情片', '动作片', '动作片', '动作片']
        return group, labels

    def showdata(self,group,label):
        group_numpy=[]
        for i in range(len(group)):
            group_numpy.append(group[i])
        group_numpy=np.array(group_numpy)
        plt.scatter(np.transpose(group_numpy)[0],np.transpose(group_numpy)[1])
        plt.show()

    def classify(self,test,train_dataset,train_label,k):
        dataset_size=train_dataset.shape[0]
        print(dataset_size)
        diffence=np.tile(test,(dataset_size,1))-train_dataset#将测试集扩大到与训练集相同的大小，以矩阵形式进行加减
        diffence=diffence**2
        print(diffence)
        distance=diffence.sum(axis=1)
        distance=distance**0.5
        print(distance)
        sorted_indice=distance.argsort()
        print(sorted_indice)
        classCount={}
        for i in range(k):
            klabels=train_label[sorted_indice[i]]
            classCount[klabels]=classCount.get(klabels,0) + 1
        sorted_classCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        # key=operator.itemgetter(1)根据字典的值进行排序
        # key=operator.itemgetter(0)根据字典的键进行排序
        # reverse降序排序字典
        print(sorted_classCount)
        return sorted_classCount[0][0]
        


kN=kNN()
group,labels=kN.createdata()
kN.showdata(group,labels)
test=np.array([100,20])
test_class=kN.classify(test,group,labels,3)
print(test_class)