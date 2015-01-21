import sys
import threading 
import json
import obd
from obd_exceptions import *
from debug import debug
from datetime import datetime, timedelta

from random import randint
connection = obd.OBD()

while not connection.is_connected():
    connection.connect()

comms = obd.commands
while True:
        maf = connection.query(comms['FUEL_TYPE']).value
        temp = ((connection.query(comms['COOLANT_TEMP']).value - 32) * 5) /9
        print("maf: %s" % maf)
        print("temp: %s" % temp)
