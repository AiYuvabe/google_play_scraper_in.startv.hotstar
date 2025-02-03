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

distribution = result_df['score'].value_counts().sort_index()
print(f"distributiondistribution)

upvotes_data = result_df['thumbsUpCount'].sum()
print(upvotes_data)

# gender_distribution = result_df['gender'].value_counts()

# filter_name = result_df[result_df['userName'].str.startswith(('pri', 'raje', 'sanjana'), na=False)]
# print(filter_name[['userName']])

review_long = result_df.loc[result_df['content'].str.len().idxmax()]
print(review_long['content'])

result_df['at'] = pd.to_datetime(result_df['at'])
# print(result_df['at'])
review_frequency = result_df['at'].diff().mean()
print(review_frequency)

result_df['hour'] = result_df['at'].dt.hour
most_common_review_hour = result_df['hour'].mode()[0]
print(most_common_review_hour)


sentiment_mapping = {
    1: 'Negative',
    2: 'Negative',
    3: 'Neutral',
    4: 'Positive',
    5: 'Positive'
}
result_df['Sentiment'] = result_df['score'].map(sentiment_mapping)
sentiment_distribution = result_df['Sentiment'].value_counts(normalize=True) * 100
print("\nOverall Sentiment Distribution:\n", sentiment_distribution)









# 1. What is the distribution of ratings?
# 2. What is the total number of upvotes?
# 3. Can you determine the male-to-female distribution?
# 4. What is the longest review?
# 5. How frequently do users review the app?
# 6. When are reviews most commonly submitted?
# 7. What is the overall sentiment of the app?


