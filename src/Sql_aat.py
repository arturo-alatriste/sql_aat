'''
-------------------------------------------------------------------------------
Description : This project is a useful library to run SQL queries on pandas dataframes.
              We can just give a query in plain Text and it can be executed. For example:

              import pandas as pd
              from Sql_aat import Sql_aat

              sql_aat = Sql_aat()
              result  = sql_aat.exec( query, df )

Date        : 2019-02-10
Author      : Arturo Alatriste Trujillo.
-------------------------------------------------------------------------------
'''
import pandas as pd

from Sql_parser  import  Sql_parser
from Sql_command import  Sql_command

class Sql_aat:

    # this two objects to the main work, parse a string sql query and execute it on a collection.
    sql_parser   = Sql_parser()
    sql_command  = Sql_command()

    df           = None

    def exec(self, query, df ):
        try:
            sql_sections = self.sql_parser.get_sql_sections( query )
            #self.sql_parser.print_sections()

            result = self.sql_command.exec( sql_sections, df )
            return result
        except Exception as e:
            print( 'Sql_aat.exec, error: {}'.format(str(e)))
            raise

    def __init__(self):
        pass