from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1_000_000
batch_size = 10_000  # Number of records per batch

# Initialize CSV file
csv_file = 'Employees_large.csv'
columns = ["EmployeeID", "FirstName", "LastName", "HireDate", "Department", "Office_Location", 
           "Position", "Salary", "ReportsTo", "Performance_Rating", "Email", "PhoneNumber", "Revenue_Generated"]

# Create DataFrame for Employees table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size
    # Lists to store data for the Employees table
    employee_ids = list(range(start_id, end_id + 1))
    first_names = [fake.first_name() for _ in range(batch_size)]
    last_names = [fake.last_name() for _ in range(batch_size)]
    hire_dates = [fake.date_between(start_date="-10y", end_date="today") for _ in range(batch_size)]
    departments = [random.choice(["Sales", "Engineering", "HR", "Marketing", "Finance"]) for _ in range(batch_size)]
    office_locations = [fake.city() for _ in range(batch_size)]
    positions = [random.choice(["Manager", "Developer", "Analyst", "Engineer", "Consultant"]) for _ in range(batch_size)]
    salaries = [random.randint(50_000, 150_000) for _ in range(batch_size)]
    reports_to = [random.choice([None] + list(range(1, num_records + 1))) for _ in range(batch_size)]
    performance_ratings = [round(random.uniform(1, 5), 1) for _ in range(batch_size)]
    emails = [fake.email() for _ in range(batch_size)]
    phone_numbers = [fake.phone_number() for _ in range(batch_size)]
    revenue_generated = [round(random.uniform(0, 500_000), 2) for _ in range(batch_size)]

    # Create DataFrame for Employees table
    batch_df = pd.DataFrame({
        "EmployeeID": employee_ids,
        "FirstName": first_names,
        "LastName": last_names,
        "HireDate": hire_dates,
        "Department": departments,
        "Office_Location": office_locations,
        "Position": positions,
        "Salary": salaries,
        "ReportsTo": reports_to,
        "Performance_Rating": performance_ratings,
        "Email": emails,
        "PhoneNumber": phone_numbers,
        "Revenue_Generated": revenue_generated
    })

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
