import pandas as pd


def df_sum(df):
    summ = 0
    for j in range(len(df)):
        for i in df.loc[j]:
            if type(i) != str:
                summ += i
    return summ


d_f = pd.DataFrame([[1, 'str'], [2, 3], [4, 5], ['str', 'STR']])
print(d_f)
print(df_sum(d_f))
