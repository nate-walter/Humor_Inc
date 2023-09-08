# Lists to store data for the SupportTickets table
ticket_ids = list(range(1, num_records + 1))
client_ids_for_tickets = random.choices(client_ids, k=num_records)
employee_ids_for_tickets = random.choices(employee_ids, k=num_records)
service_ids_for_tickets = random.choices(service_ids, k=num_records)
company_ids_for_tickets = random.choices(company_ids, k=num_records)
issue_types = [random.choice(["Technical", "Billing", "General"]) for _ in range(num_records)]
descriptions = [fake.sentence() for _ in range(num_records)]
statuses = [random.choice(["Open", "Closed", "In Progress"]) for _ in range(num_records)]
priorities = [random.choice(["Low", "Medium", "High"]) for _ in range(num_records)]
created_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(num_records)]
resolved_dates = [fake.date_between(start_date=date, end_date="today") if status == "Closed" else None for date, status in zip(created_dates, statuses)]

# Create DataFrame for SupportTickets table
support_tickets_df = pd.DataFrame({
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

support_tickets_df.head()
