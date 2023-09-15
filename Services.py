from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1_000_000
batch_size = 10_000  # Number of records per batch

# Read Services.csv to get the list of Service IDs

company_ids = pd.read_csv('Companies_large.csv', usecols=['CompanyID'])['CompanyID'].tolist()


# Initialize CSV file
csv_file = 'Services_large.csv'
columns = ["ServiceID", "CompanyID", "ServiceName", "Price", "Subscription_Model", "Rating", 
           "Discount", "Availability_Area", "LaunchDate", "Category"]

# Create DataFrame for Services table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")
    
    # Lists to store data for the Services table
    service_ids = list(range(start_id, end_id + 1))
    company_ids_for_services = random.choices(company_ids, k=batch_size)  # company_ids needs to be defined or read from Companies_large.csv
    service_names = [fake.bs() + " " + random.choice(["Pro", "Lite", "Plus", "Advanced"]) for _ in range(batch_size)]
    prices = [round(random.uniform(5, 200), 2) for _ in range(batch_size)]
    subscription_models = [random.choice(["One-time", "Monthly", "Yearly"]) for _ in range(batch_size)]
    ratings = [round(random.uniform(1, 5), 1) for _ in range(batch_size)]
    discounts = [round(random.uniform(0, 0.5), 2) for _ in range(batch_size)]
    availability_areas = [random.choice(["Local", "National", "Global"]) for _ in range(batch_size)]
    launch_dates = [fake.date_between(start_date="-10y", end_date="today") for _ in range(batch_size)]
    categories = [random.choice(["Software", "Hardware", "Food", "Entertainment", "Utilities"]) for _ in range(batch_size)]
    
    # Create DataFrame for batch
    batch_df = pd.DataFrame({
        "ServiceID": service_ids,
        "CompanyID": company_ids_for_services,
        "ServiceName": service_names,
        "Price": prices,
        "Subscription_Model": subscription_models,
        "Rating": ratings,
        "Discount": discounts,
        "Availability_Area": availability_areas,
        "LaunchDate": launch_dates,
        "Category": categories
    })

    print(f"Batch size: {batch_df.shape[0]}")
    
    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)