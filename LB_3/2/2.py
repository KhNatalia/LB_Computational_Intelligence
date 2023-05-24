import pandas as pd

data = pd.read_csv('cwurData.csv', sep=',', index_col=0, names=['world_rank', 'institution', 'country', 'national_rank', 'quality_of_education', 'alumni_employment', 'quality_of_faculty', 'publications', 'influence', 'citations', 'broad_impact', 'patents', 'score', 'year'])
df = data.loc[data["year"] == 2015]

max_score = df["score"].max()
min_score = df["score"].min()
mean_score = df["score"].mean()
print("Max score: ", max_score)
print("Min score: ", min_score)
print("Mean score: ", mean_score)
