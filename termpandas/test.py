import pandas as pd
import polars as pl
from scrollable import tprint

# Load Data
df = pd.read_csv('titanic.csv')
# Create Pandas Series
series = df['Survived']
# Convert to Polars DataFrame
df2 = pl.DataFrame(df)
# Convert to Polars Series
series2 = pl.Series(series)

#######################################################################
# Pandas Tests
# Print DataFrame
# tprint(df.head(20))

# Print DataFrame with 1 Mask
# mask_1 = df['Survived'] == 1
# tprint(df.head(20), masks={'Red': mask_1})

# Print DataFrame with 2 Masks
# Male and Survived = 1
# mask_1 = df['Survived'] == 1
# mask_2 = df['Sex'] == 'male'
# tprint(df.head(20), masks={'Red': mask_1,'Blue': mask_2})

# Print First 3 Columns
# This test will be used to check the length of the highlights
# and the divider
# tprint(df.iloc[:,0:3])

# Print First 3 Columns
# This test will be used to check the length of the highlights
# and the divider
# with one mask
# df_3_cols = df.iloc[:,0:3]
# mask_1 = df['Survived'] == 1
# tprint(df.iloc[:,0:3], masks={'Red': mask_1})

# Print Pandas Series (also need to check divider length)
# tprint(series)

# Print Pandas Series with 1 Mask (check length of highlighting)
# mask_1 = df['Survived'] == 1
# tprint(series, masks={'Red': mask_1})
 
# Print Pandas Series with 2 Masks
# mask_1 = df['Survived'] == 1
# mask_2 = df['Sex'] == 'male'
# tprint(series, masks={'Red': mask_1,'Blue': mask_2})

#######################################################################
# Polars Tests
# Print DataFrame
# tprint(df2.head(20))

# Print Series
# tprint(series2)

#######################################################################
# Highlight and Return Selected Row
mask_1 = df['Survived'] == 1
mask_2 = df['Sex'] == 'male'
tprint(df,
       highlight=True,
       highlight_color='Red',
       masks={'Red': mask_1,'Blue': mask_2})
# tprint(df, highlight=False, masks={'Red': mask_1,'Blue': mask_2})
# tprint(series, highlight=True, masks={'Red': mask_1,'Blue': mask_2})
