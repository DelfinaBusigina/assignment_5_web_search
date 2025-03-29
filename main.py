import pandas as pd
import plotly as plt
import json
from terminal_coloring import prGreen

prGreen(" ============== Python is working! ==============")

json_data = 'Dataset/trending.json'

# df = pd.json_normalize(json_data)

with open(json_data, 'r', encoding='utf-8') as file:
    data = json.load(file)

# print(data)

df = pd.json_normalize(data['collector'])
print(df)

# print(df.to_string())