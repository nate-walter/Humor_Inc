# Lists to store data for the Promotions table
promotion_ids = list(range(1, num_records + 1))
company_ids_for_promotions = random.choices(company_ids, k=num_records)
service_ids_for_promotions = random.choices(service_ids, k=num_records)
start_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(num_records)]
end_dates = [fake.date_between(start_date=date, end_date="+1y") for date in start_dates]
discount_rates = [round(random.uniform(0.1, 0.5), 2) for _ in range(num_records)]
promotion_types = [random.choice(["Seasonal", "Clearance", "Launch"]) for _ in range(num_records)]
active_statuses = [random.choice([True, False]) for _ in range(num_records)]

# Create DataFrame for Promotions table
promotions_df = pd.DataFrame({
    "PromotionID": promotion_ids,
    "CompanyID": company_ids_for_promotions,
    "ServiceID": service_ids_for_promotions,
    "StartDate": start_dates,
    "EndDate": end_dates,
    "DiscountRate": discount_rates,
    "PromotionType": promotion_types,
    "Active": active_statuses
})

promotions_df.head()
