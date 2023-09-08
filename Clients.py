# Lists to store data for the Clients table
client_ids = list(range(1, num_records + 1))
first_names = [fake.first_name() for _ in range(num_records)]
last_names = [fake.last_name() for _ in range(num_records)]
birth_dates = [fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(num_records)]
zip_codes = [fake.zipcode() for _ in range(num_records)]
phone_numbers = [fake.phone_number() for _ in range(num_records)]
emails = [fake.email() for _ in range(num_records)]
occupations = [fake.job() for _ in range(num_records)]
client_types = [random.choice(["Individual", "Corporate"]) for _ in range(num_records)]
last_purchase_dates = [fake.date_between(start_date="-5y", end_date="today") for _ in range(num_records)]
credit_scores = [random.randint(300, 850) for _ in range(num_records)]
total_spent = [round(random.uniform(100, 10000), 2) for _ in range(num_records)]

# Create DataFrame for Clients table
clients_df = pd.DataFrame({
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

clients_df.head()
