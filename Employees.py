# Lists to store data for the Employees table
employee_ids = list(range(1, num_records + 1))
first_names = [fake.first_name() for _ in range(num_records)]
last_names = [fake.last_name() for _ in range(num_records)]
hire_dates = [fake.date_between(start_date="-10y", end_date="today") for _ in range(num_records)]
departments = [random.choice(["Sales", "Engineering", "HR", "Marketing", "Finance"]) for _ in range(num_records)]
office_locations = [fake.city() for _ in range(num_records)]
positions = [random.choice(["Manager", "Developer", "Analyst", "Engineer", "Consultant"]) for _ in range(num_records)]
salaries = [random.randint(50000, 150000) for _ in range(num_records)]
reports_to = [random.choice([None] + list(range(1, num_records + 1))) for _ in range(num_records)]
performance_ratings = [round(random.uniform(1, 5), 1) for _ in range(num_records)]
emails = [fake.email() for _ in range(num_records)]
phone_numbers = [fake.phone_number() for _ in range(num_records)]
revenue_generated = [round(random.uniform(0, 500000), 2) for _ in range(num_records)]

# Create DataFrame for Employees table
employees_df = pd.DataFrame({
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

employees_df.head()
