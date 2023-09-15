from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1_000_000
batch_size = 10_000  # Number of records per batch

# Read other CSV files to get the list of IDs
client_ids = pd.read_csv('Clients_large.csv', usecols=['ClientID'])['ClientID'].tolist()
service_ids = pd.read_csv('Services_large.csv', usecols=['ServiceID'])['ServiceID'].tolist()
company_ids = pd.read_csv('Companies_large.csv', usecols=['CompanyID'])['CompanyID'].tolist()

# Initialize CSV file
csv_file = 'Reviews_large.csv'
columns = ["ReviewID", "ClientID", "ServiceID", "CompanyID", "Rating", "ReviewText", 
           "ReviewDate", "HelpfulVotes", "UnhelpfulVotes"]

# Create DataFrame for Reviews table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")

    # Lists to store data for the Reviews table
    review_ids = list(range(start_id, end_id + 1))
    client_ids_for_reviews = random.choices(client_ids, k=batch_size)
    service_ids_for_reviews = random.choices(service_ids, k=batch_size)
    company_ids_for_reviews = random.choices(company_ids, k=batch_size)
    ratings_for_reviews = [round(random.uniform(1, 5), 1) for _ in range(batch_size)]
    review_texts = [fake.sentence() for _ in range(batch_size)]
    review_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(batch_size)]
    helpful_votes = [random.randint(0, 50) for _ in range(batch_size)]
    unhelpful_votes = [random.randint(0, 20) for _ in range(batch_size)]

    # Create DataFrame for Reviews table
    batch_df = pd.DataFrame({
        "ReviewID": review_ids,
        "ClientID": client_ids_for_reviews,
        "ServiceID": service_ids_for_reviews,
        "CompanyID": company_ids_for_reviews,
        "Rating": ratings_for_reviews,
        "ReviewText": review_texts,
        "ReviewDate": review_dates,
        "HelpfulVotes": helpful_votes,
        "UnhelpfulVotes": unhelpful_votes
    })

    print(f"Batch size: {batch_df.shape[0]}")

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
