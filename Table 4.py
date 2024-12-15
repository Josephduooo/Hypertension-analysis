from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

data_independent = data.iloc[:, :-1]

scaler = StandardScaler()
standardized_data_independent = scaler.fit_transform(data_independent)

pca_independent = PCA(n_components=10)
principal_components_independent = pca_independent.fit_transform(standardized_data_independent)

factor_loadings_independent = pca_independent.components_.T * np.sqrt(pca_independent.explained_variance_)

table_4_independent = pd.DataFrame(
    factor_loadings_independent,
    columns=[f"Z{i+1}" for i in range(pca_independent.n_components_)],
    index=[f"x{i+1}" for i in range(data_independent.shape[1])]
)

print(table_4_independent)

from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

scaler = StandardScaler()
standardized_data_independent = scaler.fit_transform(data.iloc[:, :-1])

y_dependent = data.iloc[:, -1].values

pca_full_independent = PCA(n_components=10)
principal_components_independent_full = pca_full_independent.fit_transform(standardized_data_independent)

reg_model_full = LinearRegression()
reg_model_full.fit(principal_components_independent_full, y_dependent)

coefficients_full = reg_model_full.coef_
intercept_full = reg_model_full.intercept_

regression_equation_full = f"y = {intercept_full:.3f} "
for i, coef in enumerate(coefficients_full):
    regression_equation_full += f"+ {coef:.3f} * Z{i+1} "

print("Regression Equation:", regression_equation_full)