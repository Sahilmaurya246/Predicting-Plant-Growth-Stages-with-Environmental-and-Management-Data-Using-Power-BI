import pandas as pd
import numpy as np

# 1. LOAD DATASET
input_path = r"E:\Coding\Plant_Growth_Project\Enhanced_Plant_Growth_PowerBI_Dataset.csv"
df = pd.read_csv(input_path)

print(" Dataset Loaded Successfully")
print(" Rows & Columns:", df.shape)
print(" Columns:", df.columns.tolist())

# 2. DATA CLEANING

# Handle missing values safely
df["Fertilizer_Used"] = df["Fertilizer_Used"].fillna("No")
df["Irrigation"] = df["Irrigation"].fillna("No")

# 3. FEATURE ENGINEERING

# Temperature Category
def temp_category(t):
    if t < 20:
        return "Low"
    elif t <= 30:
        return "Optimal"
    else:
        return "High"

# Humidity Category
def humidity_category(h):
    if h < 50:
        return "Low"
    elif h <= 70:
        return "Optimal"
    else:
        return "High"

# Soil Moisture Category
def moisture_category(m):
    if m < 40:
        return "Low"
    elif m <= 70:
        return "Optimal"
    else:
        return "High"

df["Temperature_Range"] = df["Temperature_C"].apply(temp_category)
df["Humidity_Range"] = df["Humidity_%"].apply(humidity_category)
df["Soil_Moisture_Range"] = df["Soil_Moisture_%"].apply(moisture_category)


# 4. GROWTH SCORE LOGIC

def growth_score(row):
    score = 0

    # Temperature
    score += 3 if row["Temperature_Range"] == "Optimal" else 1

    # Humidity
    score += 3 if row["Humidity_Range"] == "Optimal" else 1

    # Soil Moisture
    score += 3 if row["Soil_Moisture_Range"] == "Optimal" else 1

    # Fertilizer
    score += 2 if row["Fertilizer_Used"] == "Yes" else 1

    # Irrigation
    score += 2 if row["Irrigation"] == "Yes" else 1

    return score

df["Growth_Score"] = df.apply(growth_score, axis=1)

# 5. DATASET EXPANSION (150 → 1000+ ROWS)

expanded_data = []

for _ in range(7):   # 150 x 7 ≈ 1050 rows
    temp = df.copy()
    temp["Temperature_C"] += np.random.uniform(-2, 2, len(temp))
    temp["Humidity_%"] += np.random.uniform(-5, 5, len(temp))
    temp["Soil_Moisture_%"] += np.random.uniform(-4, 4, len(temp))
    expanded_data.append(temp)

final_df = pd.concat(expanded_data, ignore_index=True)

# 6. SAVE FINAL DATASET

output_path = r"E:\Coding\Plant_Growth_Project\Final_Plant_Growth_PowerBI_Dataset.csv"
final_df.to_csv(output_path, index=False)

print(" FINAL DATASET CREATED SUCCESSFULLY")
print(" File Saved At:", output_path)
print(" Total Rows:", final_df.shape[0])








