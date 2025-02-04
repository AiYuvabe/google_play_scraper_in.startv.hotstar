import pandas as pd

from google_play_scraper import Sort, reviews

result, continuation_token = reviews(    
    'in.startv.hotstar',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    # count=3, # defaults to 100
    # filter_score_with=2 # defaults to None(means all score)
)


result, _ = reviews(
    'in.startv.hotstar',
    continuation_token=continuation_token # defaults to None(load from the beginning)
)
print(result, _)

result_df = pd.DataFrame(result)
print(result_df)
# result_df.to_csv("fetch_data.csv", index=False)
result_df.to_excel("fetch_data.xlsx", index=False)

result_df = pd.read_excel("fetch_data.xlsx")

# 1. What is the distribution of ratings?

distribution = result_df['score'].value_counts().sort_index()
print(f"Distribution of ratings:\n", distribution)

# 2. What is the total number of upvotes?
upvotes_data = result_df['thumbsUpCount'].sum()
print(f"The total number of upvotes:\n", upvotes_data)

# # 3. Can you determine the male-to-female distribution?

total_users = len(result_df)
female_users = result_df[result_df['userName'].str.endswith('ri', na=False)]
total_female_user = len(female_users)
total_male_users = total_users - total_female_user

print(f"Total Users: {total_users}")
print(f"Total Female Users: {total_female_user}")
print(f"Total Male Users: {total_male_users}")

# 4. What is the longest review?
review_long = result_df.loc[result_df['content'].str.len().idxmax()]
print(f"The longest review\n", review_long['content'])


result_df['at'] = pd.to_datetime(result_df['at']).sort_index(ascending=False)
# result_df['date'] = result_df['at'].dt.date
print(result_df['at'])
review_frequency = result_df['at'].diff().mean()
print(f"Frequently do users review the app\n", review_frequency)

# # 5. How frequently do users review the app?
result_df['at'] = pd.to_datetime(result_df['at'])
result_df=result_df.sort_values(by='at')
time_between_reviews = result_df['at'].diff().mean()
print(f"Average Time Between Reviews: {time_between_reviews}")


# # 6. When are reviews most commonly submitted?
result_df['hour'] = result_df['at'].dt.hour
most_common_review_hour = result_df['hour'].mode()[0]
print(f"Reviews most commonly submitted\n", most_common_review_hour)


# 7. What is the overall sentiment of the app?

sentiment_mapping = {
    1: 'Negative',
    2: 'Negative',
    3: 'Neutral',
    4: 'Positive',
    5: 'Positive'
}
result_df['Sentiment'] = result_df['score'].map(sentiment_mapping)
# print(result_df['Sentiment'])
sentiment_distribution = result_df['Sentiment'].value_counts(normalize=True) * 100
print("\nOverall Sentiment Distribution:\n", sentiment_distribution)         
    

