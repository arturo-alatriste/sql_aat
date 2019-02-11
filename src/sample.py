'''
-------------------------------------------------------------------------------
Description : In this sample we show how easy we can execte SQL queries written in plain Text
                on pandas dataframes.

Date        : 2019-02-10
Author      : Arturo Alatriste Trujillo.
-------------------------------------------------------------------------------
'''

import pandas as pd
from Sql_aat import Sql_aat

# load data in a pandas dataframe
df = pd.read_csv('people.csv' )
print( '\n\n sample.py, original data from people.csv: ' )
print(df.head(10))

# create query
query = '''select   name,  age, sex  
from    my_friends 
where sex    = 'f'
order by   age'''
print( '\n\nSQL query :\n{}'.format( query ) )

# run SQL query to our dataframe
sql_aat = Sql_aat()
result  = sql_aat.exec( query, df )

# print result dataframe
print( '\n\nsample.py, result from executing query: \n' )
print( result.head( 10 ) )
