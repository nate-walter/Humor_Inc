from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1_000_000
batch_size = 10_000  # Number of records per batch

# Initialize CSV file
csv_file = 'Clients_large.csv'
columns = ["ClientID", "FirstName", "LastName", "BirthDate", "ZipCode", "PhoneNumber", 
           "Email", "Occupation", "Client_Type", "Last_Purchase_Date", "Credit_Score", "Total_Spent"]

# Create DataFrame for Clients table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")

    # Lists to store data for the Clients table
    client_ids = list(range(start_id, end_id + 1))
    first_names = [fake.first_name() for _ in range(batch_size)]
    last_names = [fake.last_name() for _ in range(batch_size)]
    birth_dates = [fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(batch_size)]
    zip_codes = [fake.zipcode() for _ in range(batch_size)]
    phone_numbers = [fake.phone_number() for _ in range(batch_size)]
    emails = [fake.email() for _ in range(batch_size)]
    occupations = [fake.job() for _ in range(batch_size)]
    client_types = [random.choice(["Individual", "Corporate"]) for _ in range(batch_size)]
    last_purchase_dates = [fake.date_between(start_date="-5y", end_date="today") for _ in range(batch_size)]
    credit_scores = [random.randint(300, 850) for _ in range(batch_size)]
    total_spent = [round(random.uniform(100, 10000), 2) for _ in range(batch_size)]

    # Create DataFrame for batch
    batch_df = pd.DataFrame({
        "ClientID": client_ids,
        "FirstName": first_names,
        "LastName": last_names,
        "BirthDate": birth_dates,
        "ZipCode": zip_codes,
        "PhoneNumber": phone_numbers,
        "Email": emails,
        "Occupation": occupations,
        "Client_Type": client_types,
        "Last_Purchase_Date": last_purchase_dates,
        "Credit_Score": credit_scores,
        "Total_Spent": total_spent
    })

    print(f"Batch size: {batch_df.shape[0]}")

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
