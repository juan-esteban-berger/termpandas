# termpandas
Scrollable Pandas and Polars DataFrames in the Terminal.

![tprint_demo.gif](https://raw.githubusercontent.com/juan-esteban-berger/termpandas/main/tprint_demo.gif)

## Installation

```bash
pip install termpandas
```

## Basic Usage

```python
import pandas as pd
from termpandas import tprint

df = pd.read_csv('titanic.csv')
tprint(df)
```

- Key Bindings:
    - `k` or `Up Arrow Key` to scroll up
    - `j` or `Down Arrow Key` to scroll down
    - `h` or `Left Arrow Key` to scroll left
    - `l` or `Right Arrow Key` to scroll right
    - `enter` to select a row
    - `q` to quit

## Parameters

- `num_rows`: Number of rows to display at a time. Default is 10.
```python
tprint(df, num_rows=5)
```

- `highlight`: Highlights the selected row. Default is `True`.
```python
tprint(df, highlight=True)
```

- `highlight_color`: Color of the selected row. Default is `Gray`.
```python
tprint(df, highlight=True)
```

- `masks`: Dictionary of masks to highlight rows. Default is `{}`. The keys are the colors and the values are the masks.
```python
mask_1 = df['Survived'] == 1
mask_2 = df['Sex'] == 'male'
tprint(df.head(20), masks={'Red': mask_1,'Blue': mask_2})
```

- `return_row`: Returns the selected row. Default is `False`. Press `enter` to select a row.
```python
result = tprint(df.head(20), return_row=True)
try:
    tprint(result)
except:
    print("Quit termpandas: No row selected")
```

## Available Colors

- `Red`
- `Blue`
- `Magenta`
- `Gray`
