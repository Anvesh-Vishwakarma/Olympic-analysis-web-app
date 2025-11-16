import pandas as pd

def preprocess(df,region_df):

    # filtering for summer
    df = df[df['Season']=='Summer']
    # merger the region_df
    df = df.merge(region_df, on='NOC', how='left')
    # drop duplicates
    df.drop_duplicates(inplace=True)
    # one-hot encoding
    df = pd.concat([df,pd.get_dummies(df['Medal'],dtype=float)],axis=1)
    return df
