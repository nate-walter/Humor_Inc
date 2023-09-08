# Lists to store data for the Subscriptions table
subscription_ids = list(range(1, num_records + 1))
client_ids_for_subscriptions = random.choices(client_ids, k=num_records)
service_ids_for_subscriptions = random.choices(service_ids, k=num_records)
company_ids_for_subscriptions = random.choices(company_ids, k=num_records)
start_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(num_records)]
end_dates = [fake.date_between(start_date=date, end_date="+1y") for date in start_dates]
auto_renews = [random.choice([True, False]) for _ in range(num_records)]
payment_methods = [random.choice(["Credit Card", "PayPal", "Bank Transfer"]) for _ in range(num_records)]
amounts = [round(random.uniform(10, 100), 2) for _ in range(num_records)]
statuses = [random.choice(["Active", "Cancelled", "Expired"]) for _ in range(num_records)]

# Create DataFrame for Subscriptions table
subscriptions_df = pd.DataFrame({
    "SubscriptionID": subscription_ids,
    "ClientID": client_ids_for_subscriptions,
    "ServiceID": service_ids_for_subscriptions,
    "CompanyID": company_ids_for_subscriptions,
    "StartDate": start_dates,
    "EndDate": end_dates,
    "AutoRenew": auto_renews,
    "PaymentMethod": payment_methods,
    "Amount": amounts,
    "Status": statuses
})

subscriptions_df.head()
