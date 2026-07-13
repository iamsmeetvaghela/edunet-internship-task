# ==========================================
# 1. IMPORTS
# ==========================================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from datetime import date
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report

# ==========================================
# 2. LOAD DATASETS
# ==========================================
# Replace with your local file paths if necessary
df_climate = pd.read_csv("climate_change_impact_on_agriculture_2024.csv")
df_dc = pd.read_csv("data_center_hybrid.csv")

# ==========================================
# 3. HANDLING NULL VALUES & FEATURE ENGINEERING
# ==========================================
def clean_and_engineer(df, dataset_name="climate"):
    """
    Fills null values: Numerical with median (robust to outliers), Categorical with mode.
    Engineers target features for classification/regression if needed.
    """
    df_clean = df.copy()
    
    # Handle Nulls
    for col in df_clean.columns:
        if df_clean[col].dtype == 'object':
            df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
        else:
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
            
    # Feature Engineering
    if dataset_name == "climate":
        # Create a binary classification target: 1 if yield is above median, else 0
        median_yield = df_clean['Crop_Yield_MT_per_HA'].median()
        df_clean['High_Yield_Class'] = (df_clean['Crop_Yield_MT_per_HA'] > median_yield).astype(int)
        
        # Interaction feature: Total chemical usage
        if 'Pesticide_Use_KG_per_HA' in df_clean.columns and 'Fertilizer_Use_KG_per_HA' in df_clean.columns:
            df_clean['Total_Chemical_Usage'] = df_clean['Pesticide_Use_KG_per_HA'] + df_clean['Fertilizer_Use_KG_per_HA']
            
    elif dataset_name == "dc":
        # Interaction feature: Total Energy footprint proxy
        if 'Estimated_Capacity_MW' in df_clean.columns and 'PUE' in df_clean.columns:
            df_clean['Estimated_Grid_Load'] = df_clean['Estimated_Capacity_MW'] * df_clean['PUE']
            
    return df_clean

df_climate_clean = clean_and_engineer(df_climate, "climate")
df_dc_clean = clean_and_engineer(df_dc, "dc")

# ==========================================
# 4. EXPLORATORY DATA ANALYSIS (SEABORN)
# ==========================================
def plot_eda(df, dataset_name):
    """
    Generates a correlation heatmap for numerical variables to spot relationships,
    and a histogram for the primary regression target.
    """
    plt.figure(figsize=(10, 6))
    # Select only numerical columns for correlation
    num_cols = df.select_dtypes(include=[np.number])
    
    sns.heatmap(num_cols.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title(f"Correlation Heatmap: {dataset_name.capitalize()} Dataset")
    plt.show()

# Visualizing both datasets
# Note: In a Jupyter Notebook, these will display inline.
plot_eda(df_climate_clean, "Climate")
plot_eda(df_dc_clean, "Data Center")

# ==========================================
# 5. PREPROCESSING: SCALING & ENCODING
# ==========================================
def preprocess_for_ml(df, target_col):
    """
    Applies pd.get_dummies for categorical variables.
    Applies StandardScaler for numerical variables.
    Splits data into X and y.
    """
    # Separate features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Separate numerical and categorical columns
    num_cols = X.select_dtypes(include=[np.number]).columns
    cat_cols = X.select_dtypes(include=['object']).columns
    
    # 1. Encoding Categorical Data
    # We use pd.get_dummies to prevent ordinal assumptions on nominal data
    X_encoded = pd.get_dummies(X, columns=cat_cols, drop_first=True)
    
    # 2. Train-Test Split (80/20 standard)
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
    
    # 3. Scaling Numerical Data
    # Applied AFTER splitting to prevent data leakage from the test set into the training phase
    scaler = StandardScaler()
    
    # Ensure num_cols exist in X_train (since get_dummies might have added columns, we only scale original num_cols)
    cols_to_scale = [col for col in num_cols if col in X_train.columns]
    
    X_train[cols_to_scale] = scaler.fit_transform(X_train[cols_to_scale])
    X_test[cols_to_scale] = scaler.transform(X_test[cols_to_scale])
    
    return X_train, X_test, y_train, y_test

# --- Setting up Climate Dataset for Regression ---
X_train_reg, X_test_reg, y_train_reg, y_test_reg = preprocess_for_ml(
    df_climate_clean.drop(columns=['High_Yield_Class']), # Drop classification target to avoid leakage
    target_col='Economic_Impact_Million_USD'
)

# --- Setting up Data Center Dataset for Classification ---
# Encode the categorical target variable using LabelEncoder
le = LabelEncoder()
df_dc_clean['Surrounding_Water_Stress_Tier'] = le.fit_transform(df_dc_clean['Surrounding_Water_Stress_Tier'])

X_train_clf, X_test_clf, y_train_clf, y_test_clf = preprocess_for_ml(
    df_dc_clean.drop(columns=['Facility_ID', 'Facility_Name']), # Drop IDs/Names as they act as noise
    target_col='Surrounding_Water_Stress_Tier'
)

# ==========================================
# 6. MODEL TRAINING & EVALUATION
# ==========================================

# A. Linear Regression (Climate Dataset)
print("--- Linear Regression Evaluation ---")
lin_reg = LinearRegression()
lin_reg.fit(X_train_reg, y_train_reg)
y_pred_reg = lin_reg.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.4f}\n")

# B. Logistic Regression (Data Center Dataset)
print("--- Logistic Regression Evaluation ---")
# Using max_iter=1000 to ensure convergence on complex data
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train_clf, y_train_clf)
y_pred_clf = log_reg.predict(X_test_clf)

accuracy = accuracy_score(y_test_clf, y_pred_clf)
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(classification_report(y_test_clf, y_pred_clf))

# ==========================================
# 7. EXPORTING MODELS
# ==========================================
today_str = date.today().strftime("%Y-%m-%d")

reg_filename = f"linear_regression_{today_str}.pkl"
clf_filename = f"logistic_regression_{today_str}.pkl"

joblib.dump(lin_reg, reg_filename)
joblib.dump(log_reg, clf_filename)

print(f"Models successfully saved as '{reg_filename}' and '{clf_filename}'.")