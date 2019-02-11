# sql_aat
This python scripts allow us to execute SQL Queries in plain Text on pandas dataframes.

look at this sample

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


:punch:

Arturo Alatriste Trujillo.
