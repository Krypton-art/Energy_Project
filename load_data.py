import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv("energy_data.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="energy_dw",
    user="postgres",
    password="your password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Insert unique customers
customers = df[["customer_id", "region"]].drop_duplicates()

for _, row in customers.iterrows():
    cur.execute("""
        INSERT INTO dim_customer (customer_id, customer_name, region)
        VALUES (%s, %s, %s)
        ON CONFLICT (customer_id) DO NOTHING
    """, (int(row["customer_id"]), f"Customer_{int(row['customer_id'])}", row["region"]))

# Insert unique locations
locations = df[["region"]].drop_duplicates()

for _, row in locations.iterrows():
    cur.execute("""
        INSERT INTO dim_location (region, city)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
    """, (row["region"], row["region"] + "_City"))

# Insert unique dates
dates = df[["date"]].drop_duplicates()

for _, row in dates.iterrows():
    date_value = pd.to_datetime(row["date"])
    cur.execute("""
        INSERT INTO dim_time (date, month, year)
        VALUES (%s, %s, %s)
        ON CONFLICT DO NOTHING
    """, (date_value.date(), date_value.month, date_value.year))

conn.commit()

# Insert fact data
for _, row in df.iterrows():

    # Get time_id
    cur.execute("SELECT time_id FROM dim_time WHERE date = %s", (row["date"],))
    time_id = cur.fetchone()[0]

    # Get location_id
    cur.execute("SELECT location_id FROM dim_location WHERE region = %s", (row["region"],))
    location_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO fact_energy_usage
        (meter_id, customer_id, time_id, location_id, consumption_kwh, cost)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        int(row["meter_id"]),
        int(row["customer_id"]),
        time_id,
        location_id,
        float(row["consumption_kwh"]),
        float(row["cost"])
    ))

conn.commit()
cur.close()
conn.close()

print("Data loaded successfully!")