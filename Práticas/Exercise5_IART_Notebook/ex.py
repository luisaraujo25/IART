import pandas as p
import matplotlib as mpl
import seaborn as sb


f = p.read_csv('iris-data.csv')

f = p.read_csv('iris-data.csv', na_values = ['NA'])
# print(f.to_string())
print(f.describe())