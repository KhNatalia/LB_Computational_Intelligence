import pandas as pd

data = pd.read_csv('cwurData.csv', sep=',', index_col=0, names=['world_rank', 'institution', 'country', 'national_rank', 'quality_of_education', 'alumni_employment', 'quality_of_faculty', 'publications', 'influence', 'citations', 'broad_impact', 'patents', 'score', 'year'])
df = data.loc[data["year"] == 2015]

df = df.sort_values(by=['alumni_employment'], ascending=False)
pd.set_option('display.width', None)
print(df[['institution', 'alumni_employment', 'country', 'national_rank']].head(5))
