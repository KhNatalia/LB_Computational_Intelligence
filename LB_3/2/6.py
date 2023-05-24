import pandas as pd

data = pd.read_csv('cwurData.csv', encoding='utf-8', sep=',', index_col=0, names=['world_rank', 'institution', 'country', 'national_rank', 'quality_of_education', 'alumni_employment', 'quality_of_faculty', 'publications', 'influence', 'citations', 'broad_impact', 'patents', 'score', 'year'])
df = data.loc[data["year"] == 2015]

print(df['year'].corr(df['score'], method='pearson'))
print(df.corr())
