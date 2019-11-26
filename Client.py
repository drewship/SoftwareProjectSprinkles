import http.client, pprint, json , urllib , ssl , sys
import unittest
import requests

ENCODING_TYPE = "utf-8"
expected_ctype = "application/json; charset=" + ENCODING_TYPE
PORT_NUMBER = '5354'

def checkResponse( response ):

    if response.status_code != 200:
        print( " HTTP call failed: " + response.reason )
        return False
    return True

def getTrending( limit=None ):

    headers = { 'Content-type' : 'application/json; charset=utf-8' }
    response = requests.get('http://localhost:' + PORT_NUMBER + "/api/Trending",
                            params={'limit': limit },
                            headers=headers)
    json_response = response.json()
    checkResponse( response )
    return json_response




def setup():
    print("hi")
    ## todo 


class TestWarehouse( unittest.TestCase ):

    def setUp ( self ):
        pass
    def test_PostByLink( self ):
        link = "https://www.reddit.com/r/listentothis/comments/d4ry98/the_layrite_boys_if_my_luck_ran_out_vintage/"
        user = 'drewship'
        postByLink( link , user )

    def test_PostByID( self ):
        ID = "1"
        user = "drewship"
        postByID( ID , user )

    def test_PostByIDTrimmed( self ):
        ID = "d4oidi"
        user = "drewship"
        postByIDTrimmed( ID , 11 , 32 , user )

    def test_Trending( self ):

        getTrending( limit=2 )

    def test_getUserInfo( self ):

        user = "drewship"
        result = getUserInfo( user )

    def test_getUserSongs( self ):

        user = "drewship"
        result = getUserSongs( user , limit=2)

    def test_getUserSongsOrdered( self ):

        user = "drewship"
        result = getUserSongsOrdered( user ,'length', 'ASC' , limit=2)


if __name__=="__main__":
    setup()
    unittest.main()
