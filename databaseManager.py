import sqlite3, unittest , time
from sqlite3 import Error
from errorHandler import *

class databaseManager( object ):

    # Constructor, sets up empty list for the warehouse inventory
    def __init__( self ):

        self.conn = self.create_connection( "realDatabase.db" )
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
                               Event_ID INTEGER NOT NULL PRIMARY KEY,
                               Student_ID INTEGER NOT NUll FOREIGN KEY
                               Event_Name TEXT NOT NULL,
                               Event_Location TEXT NOT NULL,
                               Event_Description TEXT,
                               Event_Date TEXT NOT NULL,
                               Event_Start TEXT NOT NULL,
                               Event_End TEXT,
                               Tags TEXT,
                               CCSGA_Approved INTEGER NOT NULL); """
        try:
            c = self.conn.cursor()
            c.execute( sql_create_table )
        except Error as e:
            print(e)

    def setupCreatorsTable( self  ):

        sql_create_table = """ CREATE TABLE IF NOT EXISTS creators (
                               Student_ID INTEGER NOT NULL PRIMARY KEY); """
        try:
            c = self.conn.cursor()
            c.execute( sql_create_table )
        except Error as e:
            print(e)

    def setupTagsTable( self  ):

        sql_create_table = """ CREATE TABLE IF NOT EXISTS tags (
                               Student_ID INTEGER NOT NULL PRIMARY KEY); """
        try:
            c = self.conn.cursor()
            c.execute( sql_create_table )
        except Error as e:
            print(e)
