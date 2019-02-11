''' ------------------------------------------------------------------------------------------
Description: This class parse the SQL query string and extract all the sections and fill the
             sql_sections attribute.

Date        : 2019-02-10
Author      : Arturo Alatriste Trujillo.
 ------------------------------------------------------------------------------------------
'''

import re


class Sql_parser:

    query        = ''

    # here we store the sections of the sql query after parsing it.
    sql_sections = {
        'select'            : None,
        'select_params'     : None,
        'select_columns'    : None,
        'from'              : None,
        'from_params'       : None,
        'opt'               : None,
        'where'             : None,
        'where_params'      : None,
        'group_by'          : None,
        'group_by_params'   : None,
        'order_by'          : None,
        'order_by_params'   : None
    }

    def set_patterns(self):
        # ------------------------------------------------------------------------------------------
        # patterns.
        #
        #   The strategy for parsing is first the 3 required sections from the query: select, from and opt.
        #   Next we extract the sections from the optional section.

        try:
            # The select and from patterns are required, and the others are optional.
            self.p_select     = r'(?P<select>\s*select(?P<select_params>.*)\s*){1}'
            self.p_from       = r'(?P<from>\s*from(?P<from_params>\s\w*)\s*){1}'
            self.p_opt        = r'(?P<opt>\s*(.*))?'

            # this are the optional patterns.
            self.p_where      = r'.*(?P<where>\s*where(?P<where_params>[\s\w\(\)\=\']*)\s*)'
            self.p_group_by   = r'.*(?P<group_by>\s*group by(?P<group_by_params>\s(^order)\w(\s*,\w)*))'
            self.p_order_by   = r'.*(?P<order_by>\s*order by(?P<order_by_params>.*))'



            self.pattern      = self.p_select + self.p_from + self.p_opt
            self.reg_select   = re.compile( self.pattern )

        except Exception as e:
            print('Sql_parser.set_patterns(), error: {}'.format(str(e)))
            raise

    def clean_query(self, query):
        try:
            self.query = ' '.join( query.split() )
            self.query = self.query.lower()
        except Exception as e:
            print( 'Sql_parser.clean_query(), error: {}'.format(str(e)) )
            raise

    def get_opt_sections(self):
        try:
            m   = None
            opt = self.sql_sections[ 'opt' ]

            if opt != None:
                m = re.search( self.p_order_by, opt )
            if m   != None:
                self.sql_sections[ 'order_by'        ] = m.group( 'order_by'        )
                self.sql_sections[ 'order_by_params' ] = m.group( 'order_by_params' )
                opt                                    = opt.replace( self.sql_sections['order_by'], '')

            if opt != None:
                m = re.search( self.p_group_by, opt)
            if m   != None:
                # tmp = m2.group( 'order_by' )
                self.sql_sections[ 'group_by'        ] = m.group( 'order_by'        )
                self.sql_sections[ 'group_by_params' ] = m.group( 'order_by_params' )
                opt                                    = opt.replace( self.sql_sections['group_by'], '')

            if opt != None:
                m = re.search( self.p_where, opt)
            if m != None:
                self.sql_sections[ 'where'          ] = m.group( 'where'            )
                self.sql_sections[ 'where_params'   ] = m.group( 'where_params'     )
                opt                                   = opt.replace( self.sql_sections['where'], '')

        except Exception as e:
            print('Sql_parser.get_opt_sections(), error: {}'.format(str(e)))
            raise

    def get_required_sections(self):
        try:
            m                                    = self.reg_select.search( self.query )
            self.sql_sections[ 'select'        ] = m.group( 'select'        )
            self.sql_sections[ 'select_params' ] = m.group( 'select_params' )


            a = m.group('select_params')
            a = a.replace( '\n', ' ' )
            a = a.replace( '\t', ' ')
            a = ' '.join( a.split() )
            a = a.replace( ' ', '' )
            self.sql_sections[ 'select_columns'] = a.split( ',' )

            self.sql_sections[ 'from'          ] = m.group( 'from'          )
            self.sql_sections[ 'from_params'   ] = m.group( 'from_params'   )
            self.sql_sections[ 'opt'           ] = m.group( 'opt'           )

        except Exception as e:
            print( 'Sql_parser.get_required_sections, error: {}'.format(str(e)))
            raise

    def get_sql_sections(self, query):
        try:
            self.clean_query( query )
            self.get_required_sections()
            self.get_opt_sections()
            return self.sql_sections
        except Exception as e:
            print('Sql_parser.get_sql_sections, error: {}'.format(str(e)))
            raise

    def print_sections(self):
        try:
            for k, v in self.sql_sections.items():
                print('{}  :   {}'.format(k, v))

        except Exception as e:
            print('Sql_parser.print_sections, error: {}'.format(str(e)))
            raise

    def __init__(self):
        try:
            self.set_patterns()
            self.sql_sections = {
                'select'            : '',
                'select_params'     : '',
                'from'              : '',
                'from_params'       : '',

                'where'             : '',
                'where_params'      : '',

                'group_by'          : '',
                'group_by_params'   : '',

                'order_by'          : '',
                'order_by_params'   : ''
            }

        except Exception as e:
            print( 'Sql_parser.__init__, error: {}'.format( str(e) ) )
            raise
