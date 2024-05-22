import pandas as pd
import polars as pl
from scrollable import tprint
from blessings import Terminal
from curtsies import Input

#######################################################################
# Initialize the terminal
t = Terminal()

#######################################################################
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
print(t.width*'-')
print("Test #1")
print("Printing of Pandas DataFrame")
print(t.width*'-')
tprint(df.head(20))
print(t.width*'-')
print()

print(t.width*'-')
print("Test #2")
print("Printing of Pandas DataFrame without highlight")
print(t.width*'-')
tprint(df.head(20), highlight=False)
print(t.width*'-')
print()

print(t.width*'-')
print("Test #3")
print("Printing of Pandas DataFrame with one mask and without highlight")
print(t.width*'-')
mask_1 = df['Survived'] == 1
tprint(df.head(20), highlight = False, masks={'Red': mask_1})
print(t.width*'-')
print()

print(t.width*'-')
print("Test #4")
print("Printing of Pandas DataFrame with two masks")
print(t.width*'-')
mask_1 = df['Survived'] == 1
mask_2 = df['Sex'] == 'male'
tprint(df.head(20), masks={'Red': mask_1,'Blue': mask_2})
print(t.width*'-')
print()

print(t.width*'-')
print("Test #5")
print("Printing of Pandas DataFrame with only three columns")
print(t.width*'-')
tprint(df.iloc[:,0:3])
print(t.width*'-')
print()

print(t.width*'-')
print("Test #6")
print("Printing of Pandas DataFrame with only three columns and one mask")
print(t.width*'-')
df_3_cols = df.iloc[:,0:3]
mask_1 = df['Survived'] == 1
tprint(df.iloc[:,0:3], masks={'Red': mask_1})
print(t.width*'-')
print()

print(t.width*'-')
print("Test #7")
print("Printing of Pandas Series")
print(t.width*'-')
tprint(series)
print(t.width*'-')
print()

print(t.width*'-')
print("Test #8")
print("Printing of Pandas Series with one mask")
print(t.width*'-')
mask_1 = df['Survived'] == 1
tprint(series, masks={'Red': mask_1})
print(t.width*'-')
print()
 
print(t.width*'-')
print("Test #9")
print("Printing of Pandas Series with two masks")
print(t.width*'-')
mask_1 = df['Survived'] == 1
mask_2 = df['Sex'] == 'male'
tprint(series, masks={'Red': mask_1,'Blue': mask_2})
print(t.width*'-')
print()

print(t.width*'-')
print("Test #10")
print("Returning the selected row")
print(t.width*'-')
result = tprint(df.head(20), highlight=True, return_row=True)
try:
    tprint(result)
except:
    print("Quit termpandas: No row selected")
print(t.width*'-')
print()

#######################################################################
# Polars Tests
print(t.width*'-')
print("Test #11")
print("Printing of Polars DataFrame")
print(t.width*'-')
tprint(df2.head(20))
print(t.width*'-')
print()

print(t.width*'-')
print("Test #12")
print("Printing of Polars Series")
print(t.width*'-')
tprint(series2)
print(t.width*'-')
print()
