# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from pandas_profiling import ProfileReport as pr

# Read in the data
df = pd.read_csv("properties_2016.csv", index_col=None)
print(df.head())

# Create a report and save it to a file
## Your code here
profile = pr(df, title="Zillow Exploratory Data Analysis", explorative=True)
profile.to_file("zillow_report.html")