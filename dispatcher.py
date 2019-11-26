import json, urllib.parse , urllib.request , unittest, requests
from databaseManager import databaseManager
from redditSide import redditSide
from audioSide import audioSide
from errorHandler import *

class Dispatcher( object ):

    def __init__( self ):

        self.redditSide = redditSide()
        self.audioSide = audioSide()
        self.database = databaseManager()

    def request( self , environ ):

        # Parse environ
        dict = { }
        dict[ 'method' ] = environ[ 'REQUEST_METHOD' ]
        dict[ 'path_info' ] = environ[ 'PATH_INFO' ]
        dict[ 'query' ] = urllib.parse.parse_qs( environ[ 'QUERY_STRING' ] )
        dict[ 'length' ] = 0
        dict[ 'body'] = None
        query = dict[ 'query' ]
        path = dict[ 'path_info' ]
        path_list = path.split( "/" )
        for i in path_list:
            if len(i) == 0:
                path_list.remove(i)

        if path_list[0] != "api":
            return{'Status_code' : "400" , 'Reason' : "Invalid Path"}

        path_list.remove(path_list[0])

        if 'CONTENT_LENGTH' in environ and environ[ 'CONTENT_LENGTH' ] != "":
            dict[ 'length' ] = int( environ[ 'CONTENT_LENGTH' ] )

        if dict[ 'length' ] > 0:

            if not environ[ 'CONTENT_TYPE' ].startswith( 'application/json' ) or \
               not environ[ 'CONTENT_TYPE' ].endswith( 'utf-8' ):
               raise badParameterException

            body = environ[ 'wsgi.input' ].read( dict[ 'length' ] )
            dict[ 'body' ] = json.loads( body.decode( 'utf-8' ) )

        return self.fulflillRequest( dict[ 'method' ] , query ,
                                     dict[ 'body' ] , path_list )

    def fulflillRequest( self , method , query , body , path_list ):
        try:
            if path_list[0] == 'Trending':
                path_list.remove(path_list[0])
                return self.trendingDispatch( method , query  , body , path_list )

            elif path_list[0] == 'User':
                path_list.remove(path_list[0])
                return self.userDispatch( method , query , path_list )

            elif path_list[0] == 'Discover':
                path_list.remove(path_list[0])
                return self.discoverDispatch( method , query  , body , path_list)

        except badPathException:
            return {'Status_code': "400" , 'Reason':"Invalid Path"}
        except badParameterException:
            return {'Status_code': "400" , 'Reason':"Invalid Parameters"}
        except userNameException:
            return {'Status_code': "404" , 'Reason':"Cannot Find User"}
        except videoCannotBeUsedException:
            return {'Status_code': "204" ,
                    'Reason':"For some reason we could not use that audio"}
        except notInAudioLibraryException:
            return {'Status_code': "204" ,
                    'Reason':"Audio did not match in library"}
        except notValidRedditIdentifierException:
            return {'Status_code': "400" , 'Reason':"Not a valid reddit link/ID"}
        except noVideoException:
            return {'Status_code': "400" ,
                    'Reason':"Reddit link/ID did not have a youtube link"}

        return {'Status_code' : "400" , 'Reason' : "Invalid Path"}

    def userDispatch( self, method , query , path_list ):

        return_dict = {}
        if method == 'GET':
            if len(path_list) == 0 and 'username' in query:
                return_dict = self.database.getUserInfo( query[ 'username' ] )
                print(return_dict)
                return_dict[ 'Reason' ] = "OK"
                return_dict[ 'Status_code' ] = "200"
                return return_dict

            elif path_list[ 0 ] == 'Songs' and path_list[ 0 ] == path_list[ -1 ]\
            and 'username' in query:

                if 'limit' in query:
                    return_dict = self.database.getSongs( query[ 'username'][0] , limit=query[ 'limit' ][0])
                    return_dict[ 'Status_code' ] = "200"
                    return_dict[ 'Reason' ] = "OK"
                    return return_dict
                else:
                    return_dict = self.database.getSongs( query[ 'username'][ 0 ] )
                    return_dict[ 'Status_code' ] = "200"
                    return_dict[ 'Reason' ] = "OK"
                    return return_dict
            elif path_list[ 0 ] == 'Songs' and path_list[ -1 ] == 'Ordered' and \
            'username' in query and 'order_by' in query and 'direction' in query:
                if 'limit' in query:
                    return_dict = self.database.getSongsOrdered( query[ 'username'][ 0 ],
                                                                 query['order_by'][ 0 ],
                                                                 query['direction'][ 0 ],
                                                                limit=query[ 'limit' ][ 0 ])
                    return_dict[ 'Status_code' ] = "200"
                    return_dict[ 'Reason' ] = "OK"
                    return return_dict
                else:
                    return_dict = self.database.getSongsOrdered( query[ 'username'][ 0 ],
                                                                 query['order_by'][ 0 ],
                                                                 query['direction'][ 0 ])
                    return_dict[ 'Status_code' ] = "200"
                    return_dict[ 'Reason' ] = "OK"
                    return return_dict

        raise badPathException

    def trendingDispatch( self , method , query  , body , path_list ):

        if method == 'GET':
            if len( path_list ) == 0:
                if 'limit' in query:
                    return_dict = self.database.getTrending(limit=query[ 'limit' ])
                    return_dict[ 'Status_code' ] = "200"
                    return_dict[ 'Reason' ] = "OK"
                    return return_dict
                else:
                    return_dict = self.database.getTrending()
                    return_dict[ 'Status_code' ] = "200"
                    return_dict[ 'Reason' ] = "OK"
                    return return_dict

        raise badPathException

    def discoverDispatch( self , method , query  , body , path_list ):

        username = None
        if 'username' in body:
            username = body[ 'username' ]

        if method == 'POST':
            if path_list[ 0 ] == 'Post_ID' and path_list[ 0 ] == path_list[ -1 ] and 'Post_ID' in body:
                link = self.redditSide.getAudioByID( body['Post_ID'] )
                if self.database.checkLink( link , username ):
                    return_dict = self.database.getSong( link )
                else:
                    if 'start_time' in body and 'end_time' in body:
                        filename = self.redditSide.download_song( link , start=body['start_time'] , end=body['end_time'])
                    else:
                        filename = self.redditSide.download_song( link )
                    return_dict = self.audioSide.getSongInfo( filename )
                    return_dict[ 'link' ] = link
                    self.database.addSong( return_dict , username )
                    return_dict = self.database.getSong( link )

                return_dict[ 'Status_code' ] = "200"
                return_dict[ 'Reason' ] = "OK"
                return return_dict

            elif path_list[ 0 ] == 'link' and path_list[ 0 ] == path_list[ -1 ] and 'link' in body:
                link = self.redditSide.getAudioByLink( body['link'] )
                if self.database.checkLink( link , username ):
                    return_dict = self.database.getSong( link )
                else:
                    if 'start_time' in body and 'end_time' in body:
                        filename = self.redditSide.download_song( link , start=body['start_time'] , end=body['end_time'])
                    else:
                        filename = self.redditSide.download_song( link )
                    return_dict = self.audioSide.getSongInfo( filename )
                    return_dict[ 'link' ] = link
                    self.database.addSong( return_dict , username )
                    return_dict = self.database.getSong( link )

                return_dict[ 'Status_code' ] = "200"
                return_dict[ 'Reason' ] = "OK"
                return return_dict

        raise badPathException
