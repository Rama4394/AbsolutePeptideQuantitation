import pandas as pd
import quantitation as qt
if __name__ == '__main__':
    data = pd.read_csv('sample1.csv')
    out = qt.validation(data)
    out.to_csv('out.csv', index=False)