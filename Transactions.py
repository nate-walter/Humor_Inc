# Lists to store data for the Transactions table
transaction_ids = list(range(1, num_records + 1))
client_ids_for_transactions = random.choices(client_ids, k=num_records)
service_ids_for_transactions = random.choices(service_ids, k=num_records)
company_ids_for_transactions = random.choices(company_ids, k=num_records)
employee_ids_for_transactions = random.choices(employee_ids, k=num_records)
transaction_dates = [fake.date_between(start_date="-5y", end_date="today") for _ in range(num_records)]
amounts = [round(random.uniform(20, 500), 2) for _ in range(num_records)]
payment_methods = [random.choice(["Credit Card", "Cash", "PayPal", "Bank Transfer"]) for _ in range(num_records)]
discounts_applied = [round(random.uniform(0, 0.5), 2) for _ in range(num_records)]
final_amounts = [round(amount * (1 - discount), 2) for amount, discount in zip(amounts, discounts_applied)]

# Create DataFrame for Transactions table
transactions_df = pd.DataFrame({
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

transactions_df.head()
