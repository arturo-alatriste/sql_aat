'''
-------------------------------------------------------------------------------
Description : This class is used to execute the SQL query on the pandas dataframe

Date        : 2019-02-10
Author      : Arturo Alatriste Trujillo.
-------------------------------------------------------------------------------
'''
import re

class Sql_command:
    sql_sections = {}

    df = None

    def select_columns(self, df):
        try:
            #print( 'select_columns... begin' )
            #sections = self.sql_sections
            #a = self.sql_sections[ 'select_columns' ]
            #print( a )
            #print( 'getting columns from data frame' )
            result = df[ self.sql_sections[ 'select_columns' ] ]
            return result
        except Exception as e:
            print('Sql_command.select_columns, error: {}'.format(str(e)))
            raise

    def get_where_py_conditions(self, conditions ):
        try:
            pattern = r'[^<]=[^>]'
            regex   = re.compile(pattern)
            found   = regex.findall( conditions )

            for i in found:
                c = i.replace('=', ' = ')
                conditions = conditions.replace(i, c)
                print(i)

            return conditions
        except Exception as e:
            print('Sql_command.filter_where, error: {}'.format(str(e)))
            raise

    def filter_where(self, df):
        try:
            conditions = self.sql_sections[ 'where_params' ]

            for col in self.sql_sections[ 'select_columns' ]:
                if col in conditions:
                    conditions = conditions.replace( col, 'df.'+ col  )

            # todo: we only handle a very simple where condition using equal. We want more complex conditions.
            conditions = self.get_where_py_conditions( conditions )
            conditions = conditions.replace( ' = ', ' == ' )

            s = 'df.loc[ {} ]'.format( conditions )
            result = eval( s )
            return result

        except Exception as e:
            print('Sql_command.filter_where, error: {}'.format(str(e)))
            raise


    def exec(self, sql_sections, df ):
        try:
            self.sql_sections = sql_sections
            self.df = df

            result = self.select_columns( self.df )
            result = self.filter_where( result )
            return result

        except Exception as e:
            print('Sql_command.exec(), error: {}'.format(str(e)))
            raise

    def __init__(self):
        try:
            print( 'Sql_comand.__init__(), instance created.' )
        except Exception as e:
            print('Sql_command.__init__(), error: {}'.format(str(e)))
            raise
