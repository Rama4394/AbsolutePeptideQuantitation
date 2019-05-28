import pandas as pd

def validation(data):
    try:
        all(data.columns == ['L', 'H', 'Heavy', 'Light'])
        return concCalculation(data)
    except ValueError:
        try:
            all(data.columns == ['L_fm', 'L_ug', 'H', 'Light', 'Heavy'])
            return endogenous(data)
        except AttributeError:
            print("invalid format: Please check instruction (Endo)")
    except AttributeError:
        print("invalid format: Please check instruction")


def concCalculation(data):
    df = pd.DataFrame(data)
    df['Ratio'], df['Calc'] = [(df.Light / df.Heavy), ((df.Light / df.Heavy)* df.H)]
    return df
def endogenous(data):
    df = pd.DataFrame(data)
    df['Ratio'], df['Calc'] = [(df.Light / df.Heavy), ((df.Light / df.Heavy)* df.H)]
    df['Endo (ng/ug of Tear)'] = df.Calc/df.L_fm*1000
    return df