import json, signal, sys, atexit
from wsgiref.simple_server import make_server
from dispatcher import Dispatcher
from errorHandler import badPathException


PORT_NUMBER = 5354

# Simple server that passes on responses from the client to the webapp and back
# use command line arg db for a relational database
# use command line arg file for a file based database
def dispatch( environ , response ):

    try:
        result = application.request( environ )

        code = result[ 'Status_code' ]
        reason = result[ 'Reason' ]

        del result [ 'Status_code' ]
        del result [ 'Reason' ]

    except dbConnectionException as e:
        print("Could not connect to Database")
        sys.exit()

    result_json = json.dumps( result )
    status = code + " " + reason
    response_headers = [ ( 'Content-Type', 'application/json; charset=utf-8' ) ]
    response( status , response_headers )

    return [ result_json.encode( 'utf-8' ) ]


application = Dispatcher()

httpd = make_server( '' , PORT_NUMBER , dispatch )
print( "Server open on " + str( PORT_NUMBER ) + "..." )
httpd.serve_forever()
