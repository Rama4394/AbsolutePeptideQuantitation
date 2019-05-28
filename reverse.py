import pandas as pd
from quantitation import calc
data = pd.read_csv('sample1.csv')
print (calc(data))