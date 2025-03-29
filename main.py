import pandas as pd
import plotly as plt
import json
from terminal_coloring import prGreen, prCyan, prLightPurple

prGreen(" ============== Python is working! ==============")

# =============================   Preparing the data   ========================================

json_data = 'Dataset/trending.json'

# df = pd.json_normalize(json_data)

with open(json_data, 'r', encoding='utf-8') as file:
    data = json.load(file)

# print(data)

df = pd.json_normalize(data['collector'])
# print(df)

# prCyan(df.columns)

# prGreen(df.head()) #prints first 5 rows
# prGreen(df.info()) # all columns, datatypes


new_column_names = ['id', 'description', 'time_created', 'web_video_url', 'video_url', 'video_url_no_watermark', 'likes_count', 'shared_count', 'played_count', 'comment_count', 'download_count', 'mentions', 'hashtags', 'author_id', 
                    'sucure_id', 'name', 'nick_name', 'verified', 'signature', 'avatar', 'music_id', 'music_name', 'music_author', 'music_orginal', 'play_url', 
                    'cover_thumbnail', 'cover_medium', 'cover_large', 'cover_default', 'cover_origin', 'cover_dynamic', 'video_height', 'video_width', 'video_duration']

# print(len(new_column_names))

df.columns = (new_column_names)

# prCyan(df.info()) # all columns, datatypes

prLightPurple('========================================================================================================================================================================================================')
print(df)