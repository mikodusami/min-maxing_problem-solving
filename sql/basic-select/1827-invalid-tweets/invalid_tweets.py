import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15]
    res = df[['tweet_id']]
    return res
