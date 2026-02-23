import pandas as pd
import random
from datetime import datetime, timedelta

# Number of records
num_records = 30000

start_date = datetime(2023, 1, 1)

data = []

for i in range(num_records):
    meter_id = random.randint(1000, 1100)
    customer_id = random.randint(1, 200)
    region = random.choice(["North", "South", "East", "West"])
    date = start_date + timedelta(days=random.randint(0, 365))
    consumption = round(random.uniform(5, 50), 2)
    cost = round(consumption * 5, 2)

    data.append([
        meter_id,
        customer_id,
        region,
        date.date(),
        consumption,
        cost
    ])

df = pd.DataFrame(data, columns=[
    "meter_id",
    "customer_id",
    "region",
    "date",
    "consumption_kwh",
    "cost"
])

df.to_csv("energy_data.csv", index=False)

print("Dataset generated successfully!")