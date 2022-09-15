import os
import psycopg2
import psycopg2.extras


def establish_connection():
    """
    Create a database connection based on the :connection_data: parameter

    :connection_data: Connection string attributes

    :returns: psycopg2.connection
    """
    try:
        connect_str = "dbname={} user={} host={} password={}".format('cc_series',
                                                                     'postgres',
                                                                     'localhost',
                                                                     'kop17b')
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn









def execute_script_file(file_path):
    """
    Execute script file based on the given file path.
    Print the result of the execution to console.

    Example:
    > execute_script_file('db_schema/01_create_schema.sql')

    :file_path: Relative path of the file to be executed.
    """
    package_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(package_directory, file_path)
    with open(full_path) as script_file:
        with establish_connection() as conn, \
                conn.cursor() as cursor:
            try:
                sql_to_run = script_file.read()
                cursor.execute(sql_to_run)
                print("{} script executed successfully.".format(file_path))
            except Exception as ex:
                print("Execution of {} failed".format(file_path))
                print(ex.args)


def execute_select(statement, variables=None, fetchall=True):
    """
    Execute SELECT statement optionally parameterized.
    Use fetchall=False to get back one value (fetchone)

    Example:
    > execute_select('SELECT %(title)s; FROM shows', variables={'title': 'Codecool'})

    statement: SELECT statement

    variables:  optional parameter dict, optional parameter fetchall"""
    result_set = []
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set


def execute_dml_statement(statement, variables=None):
    """
    Execute data manipulation query statement (optionally parameterized)

    :statment: SQL statement

    :variables:  optional parameter dict"""
    result = None
    with establish_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(statement, variables)
            try:
                result = cursor.fetchone()
            except psycopg2.ProgrammingError as pe:
                pass
    return result
