import pandas as pd

file_path = r"C:\Users\29403\Desktop\数据.xlsx"

df = pd.read_excel(file_path)

print(df.head())

import statsmodels.api as sm

X = df.drop(columns=['Hypertension'])  # 提取自变量
y = df['Hypertension']  # 提取因变量

X = sm.add_constant(X)

logit_model = sm.Logit(y, X).fit()

results_table = logit_model.summary2().tables[1]

formatted_table = results_table.reset_index().rename(
    columns={
        'index': 'Variable',
        'Coef.': 'Estimate',
        'Std.Err.': 'Std. Error',
        'z': 'Z value',
        'P>|z|': 'Pr(>Chi)'
    }
)


def significance_marker(p_value):
    if p_value < 0.001:
        return '***'
    elif p_value < 0.01:
        return '**'
    elif p_value < 0.05:
        return '*'
    else:
        return ''

formatted_table['Significance'] = formatted_table['Pr(>Chi)'].apply(significance_marker)

print(formatted_table)
