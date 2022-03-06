from matplotlib.pyplot import fill
from numpy import column_stack
import pandas as pd

lst = pd.read_csv("lst.csv", header=None)
lst1 = pd.read_csv("lst1.csv", header=None)
lst2 = pd.read_csv("lst2.csv", header=None)
lst1.columns = [lst2]
data = lst.reindex(columns=list(lst2), fill_value=5)
print(data)