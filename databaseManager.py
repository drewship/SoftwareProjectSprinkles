import sqlite3, unittest , time
from sqlite3 import Error
from errorHandler import *

class databaseManager( object ):

    # Constructor, sets up empty list for the warehouse inventory
    def __init__( self ):

        self.conn = self.create_connection( "database.db" )
        self.setupUserTable()
        self.setupSongTable()
        self.setupJoinedTable()

    def create_connection( self , db_file ):

        try:
            conn = sqlite3.connect( db_file )
            return conn
        except Error as e:
            raise dbConnectionException

    def setupEventsTable( self  ):

        sql_create_table = """ CREATE TABLE IF NOT EXISTS events (
                               username text PRIMARY KEY,
                               num_searches int); """
        try:
            c = self.conn.cursor()
            c.execute( sql_create_table )
        except Error as e:
            return 2
            print(e)
