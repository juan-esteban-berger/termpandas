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
mask_1 = df['Survived'] == 1
# tprint(df.head(20), masks={'Red': mask_1})

# Print DataFrame with 2 Masks
# Male and Survived = 1
mask_1 = df['Survived'] == 1
mask_2 = df['Sex'] == 'male'
# tprint(df.head(20), masks={'Red': mask_1,'Blue': mask_2})

# Print Pandas Series
# tprint(series)

# Print Pandas Series with 1 Mask
mask_1 = df['Survived'] == 1
tprint(series, masks={'Red': mask_1})

# Print Pandas Series with 2 Masks
mask_1 = df['Survived'] == 1
mask_2 = df['Sex'] == 'male'
# tprint(series, masks={'Red': mask_1,'Blue': mask_2})

#######################################################################
# Polars Tests
# Print DataFrame
# tprint(df2.head(20))

# Print Series
# tprint(series2)
