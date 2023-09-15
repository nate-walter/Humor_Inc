from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1_000_000
batch_size = 10_000  # Number of records per batch

# Read Companies.csv and Services.csv to get the list of Company and Service IDs
company_ids = pd.read_csv('Companies_large.csv', usecols=['CompanyID'])['CompanyID'].tolist()
service_ids = pd.read_csv('Services_large.csv', usecols=['ServiceID'])['ServiceID'].tolist()

# Initialize CSV file
csv_file = 'Inventory_large.csv'
columns = ["InventoryID", "CompanyID", "ServiceID", "StockAvailable", "StockSold", "RestockDate", "StockThreshold"]

# Create DataFrame for Inventory table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")

    # Lists to store data for the Inventory table
    inventory_ids = list(range(start_id, end_id + 1))
    company_ids_for_inventory = random.choices(company_ids, k=batch_size)
    service_ids_for_inventory = random.choices(service_ids, k=batch_size)
    stock_available = [random.randint(0, 100) for _ in range(batch_size)]
    stock_sold = [random.randint(0, 50) for _ in range(batch_size)]
    restock_dates = [fake.date_between(start_date="-1y", end_date="today") for _ in range(batch_size)]
    stock_thresholds = [random.randint(5, 20) for _ in range(batch_size)]

    # Create DataFrame for Inventory table
    batch_df = pd.DataFrame({
        "InventoryID": inventory_ids,
        "CompanyID": company_ids_for_inventory,
        "ServiceID": service_ids_for_inventory,
        "StockAvailable": stock_available,
        "StockSold": stock_sold,
        "RestockDate": restock_dates,
        "StockThreshold": stock_thresholds
    })

    print(f"Batch size: {batch_df.shape[0]}")

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
