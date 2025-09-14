import pandas as pd

wine_reviews_df = pd.read_csv('winemag-data-130k-v2.csv')

SEED = 42

wine_reviews_df = wine_reviews_df[['description', 'variety']]
top_ten_varieties = wine_reviews_df['variety'].value_counts().head(10)
wine_reviews_df = wine_reviews_df[wine_reviews_df['variety'].isin(top_ten_varieties.index)]

balanced_wine_reviews = wine_reviews_df.groupby('variety').apply(lambda x: x.sample(1000, random_state=SEED), include_groups=False).reset_index().drop('level_1', axis=1)

balanced_wine_reviews.to_csv('balanced_wine_reviews.csv', index=False)