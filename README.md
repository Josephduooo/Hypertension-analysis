# Principal Component Analysis of Hypertension Based on Logistic Regression

This repository contains Python scripts and data for analyzing the impact of various factors on hypertension using Principal Component Analysis (PCA) and multiple linear regression. The study identifies significant variables contributing to hypertension and models their relationship using dimensionality reduction techniques.


# Contents

**Data**

-   `Data.xlsx`: Contains the raw dataset with independent variables (factors) and a dependent variable indicating hypertension occurrence.1. 

 **Code Files**
    
   -    `Table 1.py`: Performs direct logistic regression on the original dataset to identify significant factors.
    -   `Table 2.py`: Refines the model by selecting the four most significant factors and performs regression analysis.
    -   `Table 3.py`: Conducts Principal Component Analysis (PCA) to extract components and builds a regression model using the top 8 principal components.
    -   `Table 4.py`: Computes the factor loading matrix for original variables onto the principal components and finalizes the regression equation.

## Project Workflow

 **Data Preprocessing**

The dataset in `Data.xlsx` is loaded and standardized using `StandardScaler` to eliminate the effect of scale differences among variables.
-   **Direct Regression (Table 1 and Table 2)**
    
    -   `Table 1.py` applies logistic regression to determine significant factors affecting hypertension.
    -   `Table 2.py` focuses on the four most significant factors and models their impact more precisely.
-   **Principal Component Analysis (PCA)**
    
    -   **`Table 3.py`**:
        
        -   Conducts PCA on the standardized data and extracts the top 8 principal components based on cumulative contribution rates.
        -   A regression model is built using these components to identify their influence on the dependent variable.
    -   **`Table 4.py`**:
        
        -   Computes the factor loading matrix, showing the linear combinations of original variables contributing to each principal component.
        -   Provides the final regression equation using principal components.
-   **Final Results**
    
    -   PCA simplifies multicollinearity issues and identifies key contributing factors to hypertension.
    -   Tables for variance contribution, cumulative contribution, and factor loadings are output for detailed analysis.

## Dependencies

Ensure the following Python libraries are installed

`pip install pandas numpy scikit-learn openpyxl`
## Running the Code

-   Place `Data.xlsx` in the project directory.
    
-   Execute each script in order:
    
    -   Run `Table 1.py`:
        

        
        `python Table 1.py` 
        
    -   Run `Table 2.py`:
        
        
        `python Table 2.py` 
        
    -   Run `Table 3.py`:

        
        `python Table 3.py` 
        
    -   Run `Table 4.py`:

        
        `python Table 4.py` 
        
-   Results will be printed in the terminal and can be exported as tables.

## Results Overview

-   **Direct Logistic Regression**:
    
    -   Identifies significant factors like **alcohol consumption**, **obesity**, and **physical inactivity**.
-   **PCA Results**:
    
    -   Top 8 principal components explain over 85% of the variance in the dataset.
    -   Factor loading analysis demonstrates the contribution of original variables to each principal component.
-   **Regression Analysis**:
    
    -   The final model highlights key variables influencing hypertension and provides a more robust prediction after resolving multicollinearity.
## Acknowledgments

Special thanks to the research contributions on hypertension and multivariate analysis methodologies.
