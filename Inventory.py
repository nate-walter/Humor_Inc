# Lists to store data for the Inventory table
inventory_ids = list(range(1, num_records + 1))
company_ids_for_inventory = random.choices(company_ids, k=num_records)
service_ids_for_inventory = random.choices(service_ids, k=num_records)
stock_available = [random.randint(0, 100) for _ in range(num_records)]
stock_sold = [random.randint(0, 50) for _ in range(num_records)]
restock_dates = [fake.date_between(start_date="-1y", end_date="today") for _ in range(num_records)]
stock_thresholds = [random.randint(5, 20) for _ in range(num_records)]

# Create DataFrame for Inventory table
inventory_df = pd.DataFrame({
    "InventoryID": inventory_ids,
    "CompanyID": company_ids_for_inventory,
    "ServiceID": service_ids_for_inventory,
    "StockAvailable": stock_available,
    "StockSold": stock_sold,
    "RestockDate": restock_dates,
    "StockThreshold": stock_thresholds
})

inventory_df.head()
