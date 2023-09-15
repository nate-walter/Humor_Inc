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
csv_file = 'SupportTickets_large.csv'
columns = ["TicketID", "ClientID", "EmployeeID", "ServiceID", "CompanyID", "IssueType",
           "Description", "Status", "Priority", "CreatedDate", "ResolvedDate"]

# Create DataFrame for SupportTickets table
df = pd.DataFrame(columns=columns)
df.to_csv(csv_file, index=False)

# Generate data in batches
for i in range(0, num_records, batch_size):
    start_id = i + 1
    end_id = i + batch_size

    print(f"Processing batch: {start_id} to {end_id}")

    # Lists to store data for the SupportTickets table
    ticket_ids = list(range(start_id, end_id + 1))
    client_ids_for_tickets = random.choices(client_ids, k=batch_size)
    employee_ids_for_tickets = random.choices(employee_ids, k=batch_size)
    service_ids_for_tickets = random.choices(service_ids, k=batch_size)
    company_ids_for_tickets = random.choices(company_ids, k=batch_size)
    issue_types = [random.choice(["Technical", "Billing", "General"]) for _ in range(batch_size)]
    descriptions = [fake.sentence() for _ in range(batch_size)]
    statuses = [random.choice(["Open", "Closed", "In Progress"]) for _ in range(batch_size)]
    priorities = [random.choice(["Low", "Medium", "High"]) for _ in range(batch_size)]
    created_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(batch_size)]
    resolved_dates = [fake.date_between(start_date=date, end_date="today") if status == "Closed" else None for date, status in zip(created_dates, statuses)]

    # Create DataFrame for batch
    batch_df = pd.DataFrame({
        "TicketID": ticket_ids,
        "ClientID": client_ids_for_tickets,
        "EmployeeID": employee_ids_for_tickets,
        "ServiceID": service_ids_for_tickets,
        "CompanyID": company_ids_for_tickets,
        "IssueType": issue_types,
        "Description": descriptions,
        "Status": statuses,
        "Priority": priorities,
        "CreatedDate": created_dates,
        "ResolvedDate": resolved_dates
    })

    print(f"Batch size: {batch_df.shape[0]}")

    # Append batch to CSV
    batch_df.to_csv(csv_file, mode='a', header=False, index=False)
