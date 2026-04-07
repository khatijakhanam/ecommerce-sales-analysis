import pandas as pd

# Load dataset
df = pd.read_csv(
    r"C:\Users\lenovo\Downloads\archive\Amazon Sale Report.csv",
    low_memory=False
)

# Clean column names (remove spaces)
df.columns = df.columns.str.strip()

print("Columns:", df.columns)

# Remove duplicates
df.drop_duplicates(subset='Order ID', inplace=True)

# Convert Date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Rename columns (for consistency)
df.rename(columns={
    'Order ID': 'order_id',
    'Date': 'order_date',
    'Qty': 'quantity',
    'Amount': 'revenue',
    'Category': 'category',
    'ship-city': 'city',
    'ship-state': 'state'
}, inplace=True)

# Remove missing important values
df.dropna(subset=['order_id', 'order_date', 'revenue'], inplace=True)

# Remove invalid values
df = df[df['quantity'] > 0]
df = df[df['revenue'] > 0]

# Create new features
df['month'] = df['order_date'].dt.to_period('M')
df['year'] = df['order_date'].dt.year

# Save cleaned dataset
df.to_csv('data/cleaned_ecommerce_data.csv', index=False)

print("✅ Cleaned data saved successfully!")
print(df.head())