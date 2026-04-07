import pandas as pd
import numpy as np

# Read CSV (fix warning too)
df = pd.read_csv(
    r"C:\Users\lenovo\Downloads\archive\Amazon Sale Report.csv",
    low_memory=False
)

print("Shape:", df.shape)
print(df.head())

# ✅ STEP 1: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("Cleaned Columns:", df.columns)

# ✅ STEP 2: Now this will work
df.dropna(subset=['order_id', 'amount'], inplace=True)

# ✅ STEP 3: Fix date column name (important)
df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Save cleaned file
df.to_csv(r"C:\end to end project\cleaned_data.csv", index=False)

print("✅ Cleaned! Rows:", len(df))