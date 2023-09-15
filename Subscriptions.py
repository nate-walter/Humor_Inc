from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1_000_000
batch_size = 10_000  # Number of records per batch

# Read necessary CSV files to get lists of IDs
clients_df = pd.read_csv('Clients_large.csv')
client_ids = clients_df['ClientID'].tolist()

services_df = pd.read_csv('Services_large.csv')
service_ids = services_df['ServiceID'].tolist()

companies_df = pd.read_csv('Companies_large.csv')
company_ids = companies_df['CompanyID'].tolist()

# Initialize CSV file
csv_file = 'Subscriptions_large.csv'
columns = ["SubscriptionID", "ClientID", "ServiceID", "CompanyID", "StartDate", "EndDate", 
           "AutoRenew", "PaymentMethod", "Amount", "Status"]

# Create DataFrame for Subscriptions table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")

    # Lists to store data for the Subscriptions table
    subscription_ids = list(range(start_id, end_id + 1))
    client_ids_for_subscriptions = random.choices(client_ids, k=batch_size)
    service_ids_for_subscriptions = random.choices(service_ids, k=batch_size)
    company_ids_for_subscriptions = random.choices(company_ids, k=batch_size)
    start_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(batch_size)]
    end_dates = [fake.date_between(start_date=date, end_date="+1y") for date in start_dates]
    auto_renews = [random.choice([True, False]) for _ in range(batch_size)]
    payment_methods = [random.choice(["Credit Card", "PayPal", "Bank Transfer"]) for _ in range(batch_size)]
    amounts = [round(random.uniform(10, 100), 2) for _ in range(batch_size)]
    statuses = [random.choice(["Active", "Cancelled", "Expired"]) for _ in range(batch_size)]

    # Create DataFrame for batch
    batch_df = pd.DataFrame({
        "SubscriptionID": subscription_ids,
        "ClientID": client_ids_for_subscriptions,
        "ServiceID": service_ids_for_subscriptions,
        "CompanyID": company_ids_for_subscriptions,
        "StartDate": start_dates,
        "EndDate": end_dates,
        "AutoRenew": auto_renews,
        "PaymentMethod": payment_methods,
        "Amount": amounts,
        "Status": statuses
    })

    print(f"Batch size: {batch_df.shape[0]}")

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
