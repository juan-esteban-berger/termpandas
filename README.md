# termpandas
Scrollable Pandas DataFrames in the Terminal.

## Installation

```bash
pip install termpandas
```

## Usage

```python
import pandas as pd
from termpandas import tprint

df = pd.read_csv('titanic.csv')
tprint(df)
```

![tprint.gif](https://raw.githubusercontent.com/juan-esteban-berger/termpandas/main/tprint.gif)

- Key Bindings:
    - `k` or `Up Arrow Key` to scroll up
    - `j` or `Down Arrow Key` to scroll down
    - `h` or `Left Arrow Key` to scroll left
    - `l` or `Right Arrow Key` to scroll right
    - `q` to quit

## Optional Parameters

- `num_rows`: Number of rows to display at a time. Default is 10.
```python
tprint(df, num_rows=5)
```
