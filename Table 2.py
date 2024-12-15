import pandas as pd
import statsmodels.api as sm

file_path = r"C:\Users\29403\Desktop\数据.xlsx"
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

variables_to_fit = ['Diabetes', 'Alcohol', 'Obesity', 'Physical Inactivity']
X_subset = df[variables_to_fit]
y = df['Hypertension']


X_subset = sm.add_constant(X_subset)


logit_model_subset = sm.Logit(y, X_subset).fit()


results_table_subset = logit_model_subset.summary2().tables[1]


formatted_table_subset = results_table_subset.reset_index().rename(
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

formatted_table_subset['Significance'] = formatted_table_subset['Pr(>Chi)'].apply(significance_marker)


print(formatted_table_subset)
