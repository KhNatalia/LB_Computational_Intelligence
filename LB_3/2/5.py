import pandas as pd

data = pd.read_csv('cwurData.csv', encoding='utf-8', sep=',', index_col=0, names=['world_rank', 'institution', 'country', 'national_rank', 'quality_of_education', 'alumni_employment', 'quality_of_faculty', 'publications', 'influence', 'citations', 'broad_impact', 'patents', 'score', 'year'])
df = data.loc[data["year"] == 2015]

max_score_country = df.loc[df.groupby(["country"])['score'].idxmax()]
max_score_country = max_score_country.sort_values(by=["score"], ascending=False)
pd.set_option('display.width', None)
print(max_score_country[['institution', 'country', 'score']])
