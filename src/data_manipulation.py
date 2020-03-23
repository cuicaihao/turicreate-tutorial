# %% loading packages.
import turicreate as tc

# %% reload the data.
songs = tc.load_sframe('../data/processed/music_songs.sframe')
usage_data = tc.load_sframe('../data/processed/music_usage_data.sframe')

# %% replace those zeroes with missing values.
songs['year'] = songs['year'].apply(lambda x: None if x == 0 else x)
songs.head(5)

# %% add a column of the number of times the word 'love' is used in the title and artist column:
songs['love_count'] = songs[['title', 'artist_name']].apply(
    lambda row: sum(x.lower().split(' ').count('love') for x in row.values()))
songs.topk('love_count', k=5)

# %% select columns based on types. For instance, this extracts all the columns containing strings.
songs[str]

# %% To quickly get a summary of the column.
songs['year'].summary()

# %% To view a histogram of the SArray
songs['year'].show()
# at this stage there are a lot of null in the years.

# %% an SFrame with only dated songs.
# #This basic filter operation
dated_songs = songs[songs['year'] != None]
songs['year'].summary()
dated_songs

# %%
len(dated_songs)

# %%
songs['year'] != None

# %%
reasonable_usage = usage_data[(usage_data['listen_count'] >= 10) & (
    usage_data['listen_count'] <= 500)]

len(reasonable_usage)

# %% Joins and Aggregation
songs.show()

# %% filter those duplicates like this
other_cols = songs.column_names()
other_cols.remove('song_id')
agg_list = [tc.aggregate.SELECT_ONE(i) for i in other_cols]
unique_songs = songs.groupby('song_id', dict(zip(other_cols, agg_list)))

#  %%
usage_groups = usage_data.groupby(['song_id'], {'total_listens': tc.aggregate.SUM('listen_count'),
                                                'num_unique_users': tc.aggregate.COUNT('user_id')})
usage_groups.join(songs, ['song_id']).topk('total_listens')


# %%
