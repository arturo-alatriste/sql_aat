# Readme

Open the sample to see how easy we can run queres written in plain Text on pandas dataframes.

```
import pandas as pd
from Sql_aat import Sql_aat

# load data in a pandas dataframe
df = pd.read_csv('people.csv' )

# create query
query = '''select   name,  age, sex  from    my_friends where sex    = 'f' order by   age'''

# run SQL query to our dataframe
sql_aat = Sql_aat()
result  = sql_aat.exec( query, df )

# print result dataframe
print( result.head( 10 ) )
```
We are starting, and we want to run any SQL query on dataframes.
:)

Arturo.
