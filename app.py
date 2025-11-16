import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import scipy
from helper import medal_tally, fetch_medal_tally, year_country_list, best_athlete

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title('Olympic Analysis')
st.sidebar.image('https://vignette.wikia.nocookie.net/future/images/4/48/The_5_rings.jpg/revision/latest?cb=20140217135026')

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

#st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years,country = helper.year_country_list(df)

    selected_year = st.sidebar.selectbox('Select Year',years)
    selected_country = st.sidebar.selectbox('Select Country', country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    #st.header('Overall Analysis')
    editions = df['Year'].unique().shape[0] - 1
    city = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    country = df['region'].unique().shape[0]

    st.title("Top statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('City')
        st.title(city)
    with col3:
        st.header('Events')
        st.title(events)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Sports')
        st.title(sports)
    with col2:
        st.header('Country')
        st.title(country)
    with col3:
        st.header('Athlete')
        st.title(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time,x='Year',y='count')
    st.title('Participating Nations Over Years')
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time,x='Year',y='count')
    st.title('Events Conducted Over Years')
    st.plotly_chart(fig)

    st.title('Events Over Time for each Sports')
    fig , ax = plt.subplots(figsize = (20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)

    st.title('Best Athletes')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"overall")

    select_sports = st.selectbox('Select Sport',sport_list)
    x = helper.best_athlete(df,select_sports)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country Wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    country = st.sidebar.selectbox('Select Country',country_list)
    country_medal_tally =  helper.country_wise_medal_tally(df,country)
    fig = px.line(country_medal_tally, x='Year', y='Medal')
    st.title(country + ' Medal Tally Over Year')
    st.plotly_chart(fig)

    st.title(country + ' Best Sport Analysis')
    pt = helper.heat_map_country(df,country)
    fig , ax = plt.subplots(figsize = (20,20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title(country + ' Best Athletes')
    good_athlete = helper.country_best_athlete(df,country)
    st.table(good_athlete)

if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall age', 'Gold', 'Silver', 'Bronze'], show_hist=False,show_rug=False)
    fig.update_layout(autosize=True, width=1000, height=600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    men_df = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    female_df = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final_df = men_df.merge(female_df, on='Year')
    final_df = final_df.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'})
    fig = px.line(final_df, x='Year', y=['Male', 'Female'])

    st.title('Participation of Male and Female over the Years')
    st.plotly_chart(fig)