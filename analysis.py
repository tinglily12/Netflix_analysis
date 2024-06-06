# import the necessary libraries
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os

# loading the dataset
nf_titles = 'Netflix.csv'

if os.path.exists(nf_titles):
    netflix: DataFrame = pd.read_csv(nf_titles)
    print(netflix)
    netflix.head(10)
else:
    print(f"{nf_titles} not found.")
    quit()

# Missing data
for i in netflix.columns:
    null_rate = netflix[i].isna().sum() / len(netflix) * 100
    if null_rate > 0 :
        print("{} null rate: {}%".format(i,round(null_rate,2)))

# dropping any duplicates
netflix.dropna(inplace= True)
netflix.info()
netflix.reset_index(drop=True)

# edit the date_added column
netflix['date_added'] = pd.to_datetime(netflix['date_added'], errors='coerce')
netflix.info()

# type column
types = netflix['type'].value_counts().reset_index()
print(types)

# director column
directors = netflix['director'].value_counts().reset_index()
print(directors)

# director and type columns
directors = netflix.groupby(['director', 'type'])['director'].value_counts().reset_index()
print(directors)

# top 10 directors
top_10_directors = netflix.groupby(['director', 'type'])['director'].value_counts().sort_values(ascending=False).iloc[2:12]
print(top_10_directors)

# country column
countries = netflix.groupby(['country', 'type'])['country'].value_counts().reset_index()
print(countries)
top_10_countries = netflix.groupby(['country', 'type'])['country'].value_counts().sort_values(ascending = False).iloc[0:10]
print(top_10_countries)
top_10_TV_Show_countries = countries[countries['type'] == 'TV Show'].sort_values(by='count', ascending=False).iloc[0:10]
print(top_10_TV_Show_countries)
top_10_movie_countries = countries[countries['type'] == 'Movie'].sort_values(by='count', ascending=False).iloc[0:10]
print(top_10_movie_countries)

# release_year column
release_years = netflix.groupby(['release_year', 'type'])['release_year'].value_counts().reset_index()
print(release_years)
top_10_movies_years = release_years[release_years['type'] == 'Movie'].sort_values(by= 'count', ascending=False).iloc[0:10]
print(top_10_movies_years)
top_10_TV_show_years = release_years[release_years['type'] == 'TV show'].sort_values(by= 'count', ascending=False).iloc[0:10]
print(top_10_TV_show_years)

# duration column
durations = netflix.groupby(['duration','type'])['duration'].value_counts().reset_index()
print(durations)
top_10_movie_durations = durations[durations['type'] == 'Movie'].sort_values(by='count', ascending=False).iloc[0:10]
print(top_10_movie_durations)
top_10_TV_Show_durations = durations[durations['type'] == 'TV Show'].sort_values(by='count', ascending=False).iloc[0:10]
print(top_10_TV_Show_durations)

# listed_in column
listed_in = netflix.groupby(['listed_in', 'type'])['listed_in'].value_counts().reset_index()
print(listed_in)
top_10_listed_in_movie = listed_in[listed_in['type'] == 'Movie'].sort_values(by='count', ascending=False).iloc[0:10]
print(top_10_listed_in_movie)
top_10_listed_in_TV_Show = listed_in[listed_in['type'] == 'TV Show'].sort_values(by='count', ascending=False).iloc[0:10]
print(top_10_listed_in_TV_Show)

# Save the edited DataFrame to CSV

netflix.to_csv("Netflix_edited.csv")

# Data visualisation
# 1 First plot: (Movies VS TV Shows distribution)
types.set_index('type', inplace=True)
types.plot.pie(y='count', autopct='%.2f%%', legend='type')
plt.title("Movies VS TV Shows distribution")
plt.show()

# 2 Second plot: (Top 10 Countries)
top_10_countries.plot(x='country', y='count', kind='bar')
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# 3 third Plot: (Distribution of release  years)
netflix['release_year'].plot(kind='hist', bins=30)
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()


# Preparing a sub plot for #4 and #5 - Plotting those diagrams on one page
fig, axes = plt.subplots(1, 2, figsize=(13, 7))  # 1 rows, 2 columns

# 4 forth Plot: (Top 10 movie Durations)
top_10_movie_durations.plot(x='duration', y='count', kind='bar', ax= axes[0])
axes[0].set_title('Top 10 Movie Durations')
axes[0].set_xlabel('Duration')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=45)

# 5 Fifth Plot: (Top 10 tv shows durations)
top_10_TV_Show_durations.plot(x='duration', y='count', kind='bar', ax=axes[1])
axes[1].set_title('Top 10 TV Shows Durations')
axes[1].set_xlabel('Duration')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=45)
plt.show()

# 6 Sixth Plot: (Top 10 listed genres for shows)
top_10_listed_in_TV_Show.plot(x='listed_in', y='count', kind='bar')
plt.title('Top 10 Listed Genres for TV Shows')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# 7 Seventh Plot: (Top 10 listed genres for movies)
top_10_listed_in_movie.plot(x='listed_in', y='count', kind='bar')
plt.title('Top 10 Listed Genres for Movies')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()
