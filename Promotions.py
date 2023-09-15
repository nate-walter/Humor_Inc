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
csv_file = 'Promotions_large.csv'
columns = ["PromotionID", "CompanyID", "ServiceID", "StartDate", "EndDate", "DiscountRate", "PromotionType", "Active"]

# Create DataFrame for Promotions table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")

    # Lists to store data for the Promotions table
    promotion_ids = list(range(start_id, end_id + 1))
    company_ids_for_promotions = random.choices(company_ids, k=batch_size)
    service_ids_for_promotions = random.choices(service_ids, k=batch_size)
    start_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(batch_size)]
    end_dates = [fake.date_between(start_date=date, end_date="+1y") for date in start_dates]
    discount_rates = [round(random.uniform(0.1, 0.5), 2) for _ in range(batch_size)]
    promotion_types = [random.choice(["Seasonal", "Clearance", "Launch"]) for _ in range(batch_size)]
    active_statuses = [random.choice([True, False]) for _ in range(batch_size)]

    # Create DataFrame for Promotions table
    batch_df = pd.DataFrame({
        "PromotionID": promotion_ids,
        "CompanyID": company_ids_for_promotions,
        "ServiceID": service_ids_for_promotions,
        "StartDate": start_dates,
        "EndDate": end_dates,
        "DiscountRate": discount_rates,
        "PromotionType": promotion_types,
        "Active": active_statuses
    })

    print(f"Batch size: {batch_df.shape[0]}")

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
