from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate (this is a small sample; you can scale this up on your machine)
num_records = 100

# Lists to store data
company_ids = list(range(1, num_records + 1))
names = [fake.company() + " " + random.choice(["Unlimited", "LLC", "Corp", "GmbH", "Limited", "Inc."]) for _ in range(num_records)]
descriptions = [fake.catch_phrase() for _ in range(num_records)]
industries = [random.choice(["Technology", "Healthcare", "Finance", "Retail", "Food & Beverage", "Entertainment"]) for _ in range(num_records)]
founded_dates = [fake.date_between(start_date="-50y", end_date="today") for _ in range(num_records)]
headquarters = [fake.city() for _ in range(num_records)]
ceo_names = [fake.name() for _ in range(num_records)]
revenue_mil = [round(random.uniform(10, 500), 2) for _ in range(num_records)]
stock_symbols = [fake.lexify(text="????", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(num_records)]
employee_count = [random.randint(50, 5000) for _ in range(num_records)]
market_cap_bil = [round(random.uniform(1, 50), 2) for _ in range(num_records)]
hq_countries = [fake.country() for _ in range(num_records)]

# Create DataFrame
companies_df = pd.DataFrame({
    "CompanyID": company_ids,
    "Name": names,
    "Description": descriptions,
    "Industry": industries,
    "FoundedDate": founded_dates,
    "Headquarters": headquarters,
    "CEO_Name": ceo_names,
    "Revenue_Mil": revenue_mil,
    "Stock_Symbol": stock_symbols,
    "Employee_Count": employee_count,
    "Market_Cap_Bil": market_cap_bil,
    "HQ_Country": hq_countries
})

companies_df.head()