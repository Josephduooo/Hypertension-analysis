from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

pca_full = PCA(n_components=10)
principal_components_full = pca_full.fit_transform(standardized_data)

table_3_full = pd.DataFrame({
    "Principal Component": [f"Z{i+1}" for i in range(pca_full.n_components_)],
    "√λ (Square Root of Eigenvalue)": pca_full.singular_values_,
    "Variance Contribution Rate": pca_full.explained_variance_ratio_,
    "Cumulative Contribution Rate": pca_full.explained_variance_ratio_.cumsum()
})

print(table_3_full)

from sklearn.linear_model import LinearRegression
import numpy as np

pca_8_components = PCA(n_components=8)
principal_components_8 = pca_8_components.fit_transform(standardized_data)

y = data.iloc[:, -1].values
reg_model = LinearRegression()
reg_model.fit(principal_components_8, y)

coefficients = reg_model.coef_
intercept = reg_model.intercept_

regression_equation = f"y = {intercept:.3f} "
for i, coef in enumerate(coefficients):
    regression_equation += f"+ {coef:.3f} * Z{i+1} "

print("Regression Equation", regression_equation)