import pandas as pd

data = pd.read_csv('cwurData.csv', sep=',', index_col=0, names=['world_rank', 'institution', 'country', 'national_rank', 'quality_of_education', 'alumni_employment', 'quality_of_faculty', 'publications', 'influence', 'citations', 'broad_impact', 'patents', 'score', 'year'])
df = data.loc[data["year"] == 2015]

sum_score_country = df.groupby("country").sum()
sum_score_country = sum_score_country.sort_values(by="score", ascending=False)
print(sum_score_country[['score']])

