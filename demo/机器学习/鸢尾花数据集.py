from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

def datasets_demo():
    """
    sklearn数据集的使用
    : return:
    """
    iris = load_iris()
    # print("鸢尾花数据集:\n", iris)
    # print("查看数据集描述:\n", iris["DESCR"])

    # 数据集划分    训练集特征值, 测试集特征值, 训练集目标值, 训练集目标值
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print("训练集的特征:\n", x_train, x_train.shape)
    return None

def dict_demo():
    """
    字典特征提取:
    """
    data = [{'city': '北京', 'teperature':100}, {'city': '上海', 'teperature':60}, {'city': '深圳', 'teperature':30}]
    # 1.实例化一个转换器类
    # transfer = DictVectorizer()
    transfer = DictVectorizer(sparse=False)
    # 2.调用fit_transfrom()
    data_new = transfer.fit_transform(data)
    print("data_new\n", data_new)
    # print("特征名字\n", transfer.get_feature_names())# get_feature_names_out
    print("特征名字\n", transfer.get_feature_names_out())
    return None

if __name__ == '__main__':
    # 代码1:sklearn数据集的使用   
    # datasets_demo()
    # 代码2:字典特征提取:
    dict_demo()


    # sklearn 特征工程
    # pandas 数据清洗 数据处理:
    # 1.1:特征抽取/特征提取:
    # 机器学习-统计方法-数学公式: 文本类型->>数值  类型->>数值  
    # 1.2.1:特征提取:sklearn.feature_extraction
    # 1.2.2:字典特征提取:
    #  2:特征预处理, 3特征降维