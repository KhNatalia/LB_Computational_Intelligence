import pandas as pd
import numpy as np

data = pd.read_csv('cwurData.csv', sep=',', index_col=0, names=['world_rank', 'institution', 'country', 'national_rank', 'quality_of_education', 'alumni_employment', 'quality_of_faculty', 'publications', 'influence', 'citations', 'broad_impact', 'patents', 'score', 'year'])
df = data.loc[data["year"] == 2015]

pd.set_option('display.width', None)
corr_mat = np.abs(df[['national_rank', 'quality_of_education', 'alumni_employment', 'quality_of_faculty', 'publications', 'influence', 'citations', 'broad_impact', 'patents']].corrwith(df['score']))

print(corr_mat)
