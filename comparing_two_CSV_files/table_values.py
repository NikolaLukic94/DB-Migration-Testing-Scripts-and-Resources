'''
df.head(n) | First n rows of the DataFrame
df.tail(n) | Last n rows of the DataFrame
df.shape | Number of rows and columns
df.info() | Index, Datatype and Memory information
df.describe() | Summary statistics for numerical columns
s.value_counts(dropna=False) | View unique values and counts
df.apply(pd.Series.value_counts) | Unique values and counts for all columns


Selection
df[col] | Returns column with label col as Series
df[[col1, col2]] | Returns columns as a new DataFrame
s.iloc[0] | Selection by position
s.loc['index_one'] | Selection by index
df.iloc[0,:] | First row
df.iloc[0,0] | First element of first column

Data Cleaning
df.columns = ['a','b','c'] | Rename columns
pd.isnull() | Checks for null Values, Returns Boolean Arrray
pd.notnull() | Opposite of pd.isnull()
df.dropna() | Drop all rows that contain null values
df.dropna(axis=1) | Drop all columns that contain null values
df.dropna(axis=1,thresh=n) | Drop all rows have have less than n non null values
df.fillna(x) | Replace all null values with x
s.fillna(s.mean()) | Replace all null values with the mean (mean can be replaced with almost any function from the statistics module)
s.astype(float) | Convert the datatype of the series to float
s.replace(1,'one') | Replace all values equal to 1 with 'one'
s.replace([1,3],['one','three']) | Replace all 1 with 'one' and 3 with 'three'
df.rename(columns=lambda x: x + 1) | Mass renaming of columns
df.rename(columns={'old_name': 'new_ name'}) | Selective renaming
df.set_index('column_one') | Change the index
df.rename(index=lambda x: x + 1) | Mass renaming of index

Join/Combine
df1.append(df2) | Add the rows in df1 to the end of df2 (columns should be identical)
pd.concat([df1, df2],axis=1) | Add the columns in df1 to the end of df2 (rows should be identical)
df1.join(df2,on=col1,how='inner') | SQL-style join the columns in df1 with the columns on df2 where the rows for
col have identical values. 'how' can be one of 'left', 'right', 'outer', 'inner'

Statistics
These can all be applied to a series as well.
df.describe() | Summary statistics for numerical columns
df.mean() | Returns the mean of all columns
df.corr() | Returns the correlation between columns in a DataFrame
df.count() | Returns the number of non-null values in each DataFrame column
df.max() | Returns the highest value in each column
df.min() | Returns the lowest value in each column
df.median() | Returns the median of each column
df.std() | Returns the standard deviation of each column


select_dtypes
If data preprocessing has to be done in Python, then this command would save you some time. After reading in a table, the default data types for each column could be bool, int64, float64, object, category, timedelta64, or datetime64. You can first check the distribution by
df.dtypes.value_counts()
to know all possible data types of your dataframe, then do
df.select_dtypes(include=['float64', 'int64'])
to select a sub-dataframe with only numerical features.

number of missing values
When building models, you might want to exclude the row with too many missing values / the rows with all missing values. You can use .isnull() and .sum() to count the number of missing values within the specified columns.
import pandas as pd
import numpy as np
df = pd.DataFrame({ 'id': [1,2,3], 'c1':[0,0,np.nan], 'c2': [np.nan,1,1]})
df = df[['id', 'c1', 'c2']]
df['num_nulls'] = df[['c1', 'c2']].isnull().sum(axis=1)
df.head(

select rows with specific IDs
In SQL we can do this using SELECT * FROM … WHERE ID in (‘A001’, ‘C022’, …) to get records with specific IDs. If you want to do the same thing with pandas, you can do
df_filter = df['ID'].isin(['A001','C022',...])
df[df_filter]
'''
