import pandas as pd


def calc(data):
    df = pd.DataFrame(data)
    df['Ratio'], df['Calc.'] = [(df.Heavy / df.Light), (df.Heavy / df.Light * df.H)]
    return df


data = pd.read_csv('sample.csv')
print(calc(data))
