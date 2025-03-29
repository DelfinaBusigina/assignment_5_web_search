import pandas as pd
import plotly as plt
from terminal_coloring import prGreen

prGreen(" ============== Python is working! ==============")

json_data = 'Dataset/trending.json'

df = pd.read_json(json_data[1])
print(df.to_string())