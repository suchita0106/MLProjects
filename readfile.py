#!/usr/bin/env python3
import pandas as pd

# Read the CSV file
df = pd.read_csv('dating-full.csv')

# Print the column headers
print(df.columns.tolist())