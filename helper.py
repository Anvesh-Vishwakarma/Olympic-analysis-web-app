import numpy as np

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x

def year_country_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years, country

def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    medal_tally['Gold'] = medal_tally['Gold'].astype(int)
    medal_tally['Silver'] = medal_tally['Silver'].astype(int)
    medal_tally['Bronze'] = medal_tally['Bronze'].astype(int)
    medal_tally['Total'] = medal_tally['Total'].astype(int)
    
    return medal_tally

def data_over_time(df,col):
    data_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    return data_over_time

def best_athlete(df, Sport):
    temp_df = df.dropna(subset=['Medal'])

    if Sport != 'overall':
        temp_df = temp_df[temp_df['Sport'] == Sport]

    athlete_counts = temp_df['Name'].value_counts().reset_index()
    athlete_counts.columns = ['Name', 'Medal_Count']

    # merge back to get details (region, sport, etc.)
    result = athlete_counts.merge(df.drop_duplicates('Name'), on='Name', how='left')

    return result[['Name', 'Medal_Count', 'Sport', 'region']].head(10)

def country_wise_medal_tally(df,country):
    df = df.dropna(subset=["Medal"])
    medal_tally_2 = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    new_df = medal_tally_2[medal_tally_2['region'] == country]
    new_df = new_df.groupby('Year').count()['Medal'].reset_index()

    return new_df

def heat_map_country(df,country):

    df = df.dropna(subset=["Medal"])
    medal_tally_2 = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    new_df = medal_tally_2[medal_tally_2['region'] == country]
    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0).astype(int)

    return pt


def country_best_athlete(df, country):
    temp_df = df.dropna(subset=['Medal'])

    temp_df = temp_df[temp_df['region'] == country]

    athlete_counts = temp_df['Name'].value_counts().reset_index()
    athlete_counts.columns = ['Name', 'Medal_Count']

    # merge back to get details (region, sport, etc.)
    result = athlete_counts.merge(df.drop_duplicates('Name'), on='Name', how='left')

    return result[['Name', 'Medal_Count', 'Sport', 'region']].head(10)