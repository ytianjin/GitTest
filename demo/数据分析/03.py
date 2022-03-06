import pandas as pd
import matplotlib.pyplot as plt

datas = pd.read_csv("中国票房榜.csv", header=None)
data2 = datas.loc[:, [0, 2]]
data1 = data2.groupby(0).mean().round(2)
print(data1)
# data1.to_csv("piafai.csv")