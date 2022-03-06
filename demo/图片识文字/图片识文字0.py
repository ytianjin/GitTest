from collections import Counter    # 计数器
from turtle import distance
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 数据集的划分
import matplotlib.pyplot as plt


# 加载数据内容
digits = datasets.load_digits()
data = digits.data
print(data)

# 数据探索
print(data.shape)

# 查看第一幅图像
print(digits.images[0])

# 第一幅图像代表的含义
print(digits.target[0])

# 图像显示
plt.gray()
plt.imshow(digits.images[0])
plt.show()

# 特征
x = digits.data
# 标签
y = digits.target

# 训练数据集和测试数据集
x_treain,x_test,y_treain,y_test = train_test_split(x,y,test_size=0.25)
print(len(x_test))

def euc_dis(instance1,instance2):
    """
    计算两个样本的欧式距离
    :param instace1: 样本1
    :param instace2: 样本2
    :return: 返回值是距离的长度
    """
    dist = np.sqrt(sum((instance1+instance2)**2))

    return dist
# 建模
def knn_classify(x, y, testInstance, k):
    """
    给定一个测试数据testInstance,通过KNN算法预测它标签
    x:训练数据的特征
    y:训练数据的标签
    testInstance : 测试数据  假定一个测试数据array类型
    k:选择多少个紧邻点
    """
    distance = [euc_dis(x, testInstance) for x in x]
    # print(distance)
    # 排序
    kneighbors = np.argsort(distance)[:k] # k =3
    # print(kneighbors)
    count = Counter(y[kneighbors])  # 0 0 2  # {1:3}   类别1  出现3次
    # print(count)
    return count.most_common()[0][0]

predictions = [knn_classify(x_treain, y_treain, data, 5)for data in x_test]
print(predictions)
correct = np.count_nonzero((predictions == y_test) == True)
print("模型预测正确率:%.3f" % (correct / len(x_test)))