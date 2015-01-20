import obd
from obd_exceptions import *
from debug import debug

# Connect to OBD
connection = obd.OBD()
while not connection.is_connected():
	connection.connect()
	
for command in connection.supportedCommands:
    print str(command)                      # prints the command name
    #response = connection.query(command)    # sends the command, and returns the decoded response
    #print response.value, response.unit     # prints the data and units returned from the car