# Re-initialize necessary variables and libraries

from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate (this is a small sample; you can scale this up on your machine)
num_records = 100

# Lists to store data for the Services table
service_ids = list(range(1, num_records + 1))
company_ids = list(range(1, num_records + 1))  # Re-initialize company IDs for foreign key reference
company_ids_for_services = random.choices(company_ids, k=num_records)
service_names = [fake.bs() + " " + random.choice(["Pro", "Lite", "Plus", "Advanced"]) for _ in range(num_records)]
prices = [round(random.uniform(5, 200), 2) for _ in range(num_records)]
subscription_models = [random.choice(["One-time", "Monthly", "Yearly"]) for _ in range(num_records)]
ratings = [round(random.uniform(1, 5), 1) for _ in range(num_records)]
discounts = [round(random.uniform(0, 0.5), 2) for _ in range(num_records)]
availability_areas = [random.choice(["Local", "National", "Global"]) for _ in range(num_records)]
launch_dates = [fake.date_between(start_date="-10y", end_date="today") for _ in range(num_records)]
categories = [random.choice(["Software", "Hardware", "Food", "Entertainment", "Utilities"]) for _ in range(num_records)]

# Create DataFrame for Services table
services_df = pd.DataFrame({
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

services_df.head()
