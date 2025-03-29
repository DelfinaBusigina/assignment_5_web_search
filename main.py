import pandas as pd
import plotly as plt
import json
from terminal_coloring import prGreen, prCyan, prLightPurple

prGreen(" ============== Python is working! ==============")

# =============================   Preparing the data   ========================================

json_data = 'Dataset/trending.json'

# prep_df = pd.json_normalize(json_data)

with open(json_data, 'r', encoding='utf-8') as file:
    data = json.load(file)

# print(data)

prep_df = pd.json_normalize(data['collector'])
# print(prep_df)

# prCyan(prep_df.columns)

# prGreen(prep_df.head()) #prints first 5 rows
# prGreen(prep_df.info()) # all columns, datatypes


new_column_names = ['id', 'description', 'time_created', 'web_video_url', 'video_url', 'video_url_no_watermark', 'likes_count', 'shared_count', 'played_count', 'comment_count', 'download_count', 'mentions', 'hashtags', 'author_id', 
                    'sucure_id', 'name', 'nick_name', 'verified', 'signature', 'avatar', 'music_id', 'music_name', 'music_author', 'music_orginal', 'play_url', 
                    'cover_thumbnail', 'cover_medium', 'cover_large', 'cover_default', 'cover_origin', 'cover_dynamic', 'video_height', 'video_width', 'video_duration']

# print(len(new_column_names))

prep_df.columns = (new_column_names)

# prCyan(prep_df.info()) # all columns, datatypes

# prLightPurple('========================================================================================================================================================================================================')
# print(prep_df)

df = prep_df[['id', 'description', 'time_created', 'likes_count', 'shared_count', 'played_count', 'comment_count', 'author_id', 'name', 'nick_name', 'verified', 'music_id', 'music_name', 'music_author', 'video_duration']]
# hash_df = pd.json_normalize(prep_df['hashtags'])

hash_df = prep_df['hashtags'].apply(lambda x: x if isinstance(x, list) else [])
hash_df = hash_df.explode('hashtags').reset_index(drop=True)
hash_df = pd.json_normalize(hash_df)


print(df)
prGreen('------------------------------------------')
print(hash_df)

# =============================   Analysing the data   ========================================

dist_crt_time = df['video_duration'].value_counts()
print(dist_crt_time)

# dist_hs = hash_df['id'].value_counts()
# prLightPurple(dist_hs)