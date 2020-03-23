# %% Loading the data: songs and usage_data
import turicreate as tc
songs = tc.SFrame.read_csv(
    "../data/raw/million-song-data-set-subset/song_data.csv")
usage_data = tc.SFrame.read_csv("../data/raw/million-song-data-set-subset/10000.txt",
                                header=False,
                                delimiter='\t',
                                column_type_hints={'X3': int})

# %%
songs

# %%
usage_data

# %%
usage_data.rename({'X1': 'user_id', 'X2': 'song_id', 'X3': 'listen_count'})

# %% save the data
usage_data.save('../data/processed/music_usage_data.sframe')

# %% reload the data
same_usage_data = tc.load_sframe('../data/processed/music_usage_data.sframe')

# %%
