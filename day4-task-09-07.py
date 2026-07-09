import pandas as pd

# 1. IMPORTING THE DATASET

# We load the dataset using standard pandas read_csv.
file_path = "climate_change_impact_on_agriculture_2024.csv"
df = pd.read_csv(file_path)

print(" DATASET SUCCESSFULLY IMPORTED ")


# 2. GENERALIZATIONS & BASIC DATA ANALYSIS

"""
GENERALIZATIONS NOTICED ABOUT THE DATASET STRUCTURE:
- Shape of Data: The dataset contains 10,000 rows and 15 columns.
- Categorical Variables: Column features like 'Country', 'Region', 'Crop_Type', 
  and 'Adaptation_Strategies' help segregate regional agricultural practices.
- Diverse Range of Crops: Crops include staples like Wheat, Corn, Rice, 
  and high-value items like Coffee and Fruits evenly distributed.
- Geographic Scope: Covers multiple major global nations including India, China, 
  USA, Australia, France, Canada, and Brazil.
"""

# Displaying basic shape and information
print(f"Data Dimensions: {df.shape[0]} rows, {df.shape[1]} columns\n")
print("Data Types & Structure Summary:")
print(df.info())



# 3. HANDLING NULL / MISSING VALUES

# We check if there are any null values present across the data.
null_summary = df.isnull().sum()
print("\n NULL VALUE SUMMARY ")
print(null_summary)

# Handling process using Pandas methods if any nulls were to exist:
# - Numeric columns are filled with their respective column median to protect against outliers.
# - Categorical columns are filled with the mode value (most frequent value).
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values checked and handled successfully.")


# 4. RELATIONSHIP ANALYSIS (CORRELATION)

# We extract only the numeric features to calculate the correlation matrix via pandas.
numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()

print("\nLINEAR CORRELATION MATRIX ")
print(correlation_matrix.round(3))

"""
RELATIONSHIPS NOTICED BETWEEN THE VARIABLES:

1. Crop Yield vs Economic Impact (Strong Positive Connection: ~0.726):
   - There is a significant positive relationship between 'Crop_Yield_MT_per_HA' 
     and 'Economic_Impact_Million_USD'. As crop yield efficiency increases, 
     the overall economic returns grow proportionally.

2. Average Temperature vs Crop Yield (Moderate Positive Connection: ~0.264):
   - 'Average_Temperature_C' displays a mild positive trend with crop yield. 
     This suggests that, across the dataset profile, a temperature rise within certain 
     bounds might be associated with higher yields or relates to specific warm-season crops.

3. Average Temperature vs Economic Impact (Mild Positive Connection: ~0.196):
   - Correlating back to crop yield, an increase in average temperature shows 
     a secondary positive link to economic outcomes.

4. CO2 Emissions vs Crop Yield (Weak Negative Connection: ~ -0.090):
   - Higher 'CO2_Emissions_MT' values show a slight negative relationship with 
     'Crop_Yield_MT_per_HA', signaling a potential adverse environmental byproduct effect.

5. Weak/Negligible Correlations:
   - Elements like 'Extreme_Weather_Events', 'Soil_Health_Index', and 'Precipitation' 
     show near-zero direct linear correlation to individual variables. 
     This indicates their effects are likely non-linear or dependent on combinations of crop types.
"""

# Printing a simplified overview of key statistical data boundaries
print("\n STATISTICAL BOUNDARIES OVERVIEW ")
print(df.describe().loc[['min', 'mean', 'max']])