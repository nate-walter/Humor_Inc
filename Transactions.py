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

employees_df = pd.read_csv('Employees_large.csv')
employee_ids = employees_df['EmployeeID'].tolist()

services_df = pd.read_csv('Services_large.csv')
service_ids = services_df['ServiceID'].tolist()

companies_df = pd.read_csv('Companies_large.csv')
company_ids = companies_df['CompanyID'].tolist()

# Initialize CSV file
csv_file = 'Transactions_large.csv'
columns = ["TransactionID", "ClientID", "ServiceID", "CompanyID", "EmployeeID", 
           "TransactionDate", "Amount", "PaymentMethod", "DiscountApplied", "FinalAmount"]

# Create DataFrame for Transactions table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")

    # Lists to store data for the Transactions table
    transaction_ids = list(range(start_id, end_id + 1))
    client_ids_for_transactions = random.choices(client_ids, k=batch_size)
    service_ids_for_transactions = random.choices(service_ids, k=batch_size)
    company_ids_for_transactions = random.choices(company_ids, k=batch_size)
    employee_ids_for_transactions = random.choices(employee_ids, k=batch_size)
    transaction_dates = [fake.date_between(start_date="-5y", end_date="today") for _ in range(batch_size)]
    amounts = [round(random.uniform(20, 500), 2) for _ in range(batch_size)]
    payment_methods = [random.choice(["Credit Card", "Cash", "PayPal", "Bank Transfer"]) for _ in range(batch_size)]
    discounts_applied = [round(random.uniform(0, 0.5), 2) for _ in range(batch_size)]
    final_amounts = [round(amount * (1 - discount), 2) for amount, discount in zip(amounts, discounts_applied)]

    # Create DataFrame for batch
    batch_df = pd.DataFrame({
        "TransactionID": transaction_ids,
        "ClientID": client_ids_for_transactions,
        "ServiceID": service_ids_for_transactions,
        "CompanyID": company_ids_for_transactions,
        "EmployeeID": employee_ids_for_transactions,
        "TransactionDate": transaction_dates,
        "Amount": amounts,
        "PaymentMethod": payment_methods,
        "DiscountApplied": discounts_applied,
        "FinalAmount": final_amounts
    })

    print(f"Batch size: {batch_df.shape[0]}")

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
