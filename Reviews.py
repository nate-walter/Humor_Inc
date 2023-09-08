# Lists to store data for the Reviews table
review_ids = list(range(1, num_records + 1))
client_ids_for_reviews = random.choices(client_ids, k=num_records)
service_ids_for_reviews = random.choices(service_ids, k=num_records)
company_ids_for_reviews = random.choices(company_ids, k=num_records)
ratings_for_reviews = [round(random.uniform(1, 5), 1) for _ in range(num_records)]
review_texts = [fake.sentence() for _ in range(num_records)]
review_dates = [fake.date_between(start_date="-2y", end_date="today") for _ in range(num_records)]
helpful_votes = [random.randint(0, 50) for _ in range(num_records)]
unhelpful_votes = [random.randint(0, 20) for _ in range(num_records)]

# Create DataFrame for Reviews table
reviews_df = pd.DataFrame({
    "ReviewID": review_ids,
    "ClientID": client_ids_for_reviews,
    "ServiceID": service_ids_for_reviews,
    "CompanyID": company_ids_for_reviews,
    "Rating": ratings_for_reviews,
    "ReviewText": review_texts,
    "ReviewDate": review_dates,
    "HelpfulVotes": helpful_votes,
    "UnhelpfulVotes": unhelpful_votes
})

reviews_df.head()
