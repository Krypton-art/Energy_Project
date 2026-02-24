import pandas as pd

# Load original dataset
df = pd.read_csv("energy_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Extract month and year
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

# Aggregate monthly consumption
monthly = df.groupby(["year", "month"])["consumption_kwh"].sum().reset_index()

# Rename column
monthly.rename(columns={"consumption_kwh": "total_consumption"}, inplace=True)

# Save to CSV
monthly.to_csv("monthly_aggregated.csv", index=False)

print("monthly_aggregated.csv generated successfully!")