# %% loading packages
import turicreate as tc

# %% read the tables
songs = tc.SFrame.read_csv(
    "../data/raw/million-song-data-set-subset/song_data.csv")

usage_data = tc.SFrame.read_csv("../data/raw/million-song-data-set-subset/10000.txt",
                                header=False,
                                delimiter='\t',
                                column_type_hints={'X3': int})

# %%
print("# Show the data: songs\n")
print(songs)
# print(songs.head(5))

# %%
print("# Show the data: usage_data\n")
print(usage_data)
# print(usage_data.head(5))


# %% rename the usage_data column name
usage_data = usage_data.rename(
    {'X1': 'user_id', 'X2': 'song_id', 'X3': 'listen_count'})
print("# Show the data: usage_data with new names\n")
print(usage_data.head(5))

# %% save the data
songs.save('../data/processed/music_songs.sframe')
usage_data.save('../data/processed/music_usage_data.sframe')

# %% reload the data
same_songs = tc.load_sframe('../data/processed/music_songs.sframe')
same_usage_data = tc.load_sframe('../data/processed/music_usage_data.sframe')

print("# Show the reloaded data: songs")
print(same_songs.head(5))

print("# Show the reloaded data: usage_data ")
print(usage_data.head(5))
# %%
print("PASS")
