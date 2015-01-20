#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.4.5
# In conjunction with Tcl version 8.6
#    Jan 16, 2015 06:41:20 PM
import sys
import threading 
import json
import obd
from obd_exceptions import *
from debug import debug
from datetime import datetime, timedelta

from random import randint

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import realtimegui_support
from connection_screen import Pimped_Is_Loading
import connection_screen_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, connection
    # Attempt to connect to car first
    connection = obd.OBD()
    #while not connection.is_connected():
    #    connection.connect()
        
    
    root = Tk()
    root.title('Real_time_display')
    root.geometry('1264x692+18+201')
    w = Real_time_display (root)
    realtimegui_support.init(root, w)
    root.mainloop()

w = None
jsonfile = "gui.json"

def create_Real_time_display(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('Real_time_display')
    w.geometry('1264x692+18+201')
    w_win = Real_time_display (w)
    realtimegui_support.init(w, w_win, param)
    return w_win

def destroy_Real_time_display():
    global w
    w.destroy()
    w = None
    
class Real_time_display:
    
    def __init__(self, master=None):
        global connection
        comms = obd.commands
        self.temperatures_shown = False
        self.count = 0
        self.journeyTime = 0
        self.gpsLAT = 0.0
        self.gpsLONG = 0.0
        self.mph = 0 
        self.mpg = 0
        self.revs = 0
        self.miles = 0
        self.throttle = 0
        self.load = 0
        self.engine_temp = 0
        self.air_temp = 0
        self.drive_data = {
            'time_started' : "%s" % datetime.utcnow(),
            'fuel_type' : connection.query(comms['FUEL_TYPE']).value,
            'distance_travelled' : 0,
            'events' : []
        }
        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Miriam Fixed} -size 48 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Miriam Fixed} -size 48 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font17 = "-family {Miriam Fixed} -size 120 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        master.configure(background="#ffffff")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")


        self.lblMPH = Label(master)
        self.lblMPH.place(relx=0.05, rely=0.17, height=140, width=520)
        self.lblMPH.configure(activebackground="#f9f9f9")
        self.lblMPH.configure(activeforeground="black")
        self.lblMPH.configure(background="#ffffff")
        self.lblMPH.configure(disabledforeground="#a3a3a3")
        self.lblMPH.configure(font=font17)
        self.lblMPH.configure(foreground="#000000")
        self.lblMPH.configure(highlightbackground="#d9d9d9")
        self.lblMPH.configure(highlightcolor="black")
        self.lblMPH.configure(text='''25mph''')

        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        
        self.lblNameTime = Label(master)
        self.lblNameTime.place(relx=0.02, rely=0.03, height=55, width=200)
        self.lblNameTime.configure(activebackground="#f9f9f9")
        self.lblNameTime.configure(activeforeground="black")
        self.lblNameTime.configure(background="#ffffff")
        self.lblNameTime.configure(disabledforeground="#a3a3a3")
        self.lblNameTime.configure(font=font11)
        self.lblNameTime.configure(foreground="#000000")
        self.lblNameTime.configure(highlightbackground="#d9d9d9")
        self.lblNameTime.configure(highlightcolor="black")
        self.lblNameTime.configure(text='''Time:''')

        self.lblTime = Label(master)
        self.lblTime.place(relx=0.17, rely=0.03, height=55, width=360)
        self.lblTime.configure(activebackground="#f9f9f9")
        self.lblTime.configure(activeforeground="black")
        self.lblTime.configure(background="#ffffff")
        self.lblTime.configure(disabledforeground="#a3a3a3")
        self.lblTime.configure(font=font11)
        self.lblTime.configure(foreground="#000000")
        self.lblTime.configure(highlightbackground="#d9d9d9")
        self.lblTime.configure(highlightcolor="black")
        self.lblTime.configure(text='''125m 32s''')

        self.lblNameGPS = Label(master)
        self.lblNameGPS.place(relx=0.60, rely=0.03, height=55, width=180)
        self.lblNameGPS.configure(activebackground="#f9f9f9")
        self.lblNameGPS.configure(activeforeground="black")
        self.lblNameGPS.configure(background="#ffffff")
        self.lblNameGPS.configure(disabledforeground="#a3a3a3")
        self.lblNameGPS.configure(font=font11)
        self.lblNameGPS.configure(foreground="#000000")
        self.lblNameGPS.configure(highlightbackground="#d9d9d9")
        self.lblNameGPS.configure(highlightcolor="black")
        self.lblNameGPS.configure(text='''GPS:''')
        
        self.lblGPS = Label(master)
        self.lblGPS.place(relx=0.73, rely=0.03, height=55, width=300)
        self.lblGPS.configure(activebackground="#f9f9f9")
        self.lblGPS.configure(activeforeground="black")
        self.lblGPS.configure(background="#ffffff")
        self.lblGPS.configure(disabledforeground="#a3a3a3")
        self.lblGPS.configure(font=font11)
        self.lblGPS.configure(foreground="#000000")
        self.lblGPS.configure(highlightbackground="#d9d9d9")
        self.lblGPS.configure(highlightcolor="black")
        self.lblGPS.configure(text='''25N 34E''')

        self.lblMPG = Label(master)
        self.lblMPG.place(relx=0.57, rely=0.17, height=140, width=520)
        self.lblMPG.configure(activebackground="#f9f9f9")
        self.lblMPG.configure(activeforeground="black")
        self.lblMPG.configure(background="#ffffff")
        self.lblMPG.configure(disabledforeground="#a3a3a3")
        self.lblMPG.configure(font=font17)
        self.lblMPG.configure(foreground="#000000")
        self.lblMPG.configure(highlightbackground="#d9d9d9")
        self.lblMPG.configure(highlightcolor="black")
        self.lblMPG.configure(text='''40mpg''')


        self.lblRPM = Label(master)
        self.lblRPM.place(relx=0.24, rely=0.45, height=140, width=680)
        self.lblRPM.configure(activebackground="#f9f9f9")
        self.lblRPM.configure(activeforeground="black")
        self.lblRPM.configure(background="#ffffff")
        self.lblRPM.configure(disabledforeground="#a3a3a3")
        self.lblRPM.configure(font=font17)
        self.lblRPM.configure(foreground="#000000")
        self.lblRPM.configure(highlightbackground="#d9d9d9")
        self.lblRPM.configure(highlightcolor="black")
        self.lblRPM.configure(text='''1000rpm''')

        self.lblScroller1 = Label(master)
        self.lblScroller1.place(relx=0.01, rely=0.79, height=53, width=406)
        self.lblScroller1.configure(activebackground="#f9f9f9")
        self.lblScroller1.configure(activeforeground="black")
        self.lblScroller1.configure(background="#ffffff")
        self.lblScroller1.configure(disabledforeground="#a3a3a3")
        self.lblScroller1.configure(font=font11)
        self.lblScroller1.configure(foreground="#000000")
        self.lblScroller1.configure(highlightbackground="#d9d9d9")
        self.lblScroller1.configure(highlightcolor="black")
        self.lblScroller1.configure(text='''Load''')
        
        self.lblScrollerVal1 = Label(master)
        self.lblScrollerVal1.place(relx=0.01, rely=0.88, height=73, width=406)
        self.lblScrollerVal1.configure(activebackground="#f9f9f9")
        self.lblScrollerVal1.configure(activeforeground="black")
        self.lblScrollerVal1.configure(background="#ffffff")
        self.lblScrollerVal1.configure(disabledforeground="#a3a3a3")
        self.lblScrollerVal1.configure(font=font11)
        self.lblScrollerVal1.configure(foreground="#000000")
        self.lblScrollerVal1.configure(highlightbackground="#d9d9d9")
        self.lblScrollerVal1.configure(highlightcolor="black")
        self.lblScrollerVal1.configure(text='''234''')
        
        self.lblMiles = Label(master)
        self.lblMiles.place(relx=0.34, rely=0.79, height=53, width=406)
        self.lblMiles.configure(activebackground="#f9f9f9")
        self.lblMiles.configure(activeforeground="black")
        self.lblMiles.configure(background="#ffffff")
        self.lblMiles.configure(disabledforeground="#a3a3a3")
        self.lblMiles.configure(font=font11)
        self.lblMiles.configure(foreground="#000000")
        self.lblMiles.configure(highlightbackground="#d9d9d9")
        self.lblMiles.configure(highlightcolor="black")
        self.lblMiles.configure(text='''Miles''')

        self.lblMilesVal = Label(master)
        self.lblMilesVal.place(relx=0.34, rely=0.88, height=73, width=406)
        self.lblMilesVal.configure(activebackground="#f9f9f9")
        self.lblMilesVal.configure(activeforeground="black")
        self.lblMilesVal.configure(background="#ffffff")
        self.lblMilesVal.configure(disabledforeground="#a3a3a3")
        self.lblMilesVal.configure(font=font11)
        self.lblMilesVal.configure(foreground="#000000")
        self.lblMilesVal.configure(highlightbackground="#d9d9d9")
        self.lblMilesVal.configure(highlightcolor="black")
        self.lblMilesVal.configure(text='''42''')
        
        self.lblScroller2 = Label(master)
        self.lblScroller2.place(relx=0.67, rely=0.79, height=53, width=406)
        self.lblScroller2.configure(activebackground="#f9f9f9")
        self.lblScroller2.configure(activeforeground="black")
        self.lblScroller2.configure(background="#ffffff")
        self.lblScroller2.configure(disabledforeground="#a3a3a3")
        self.lblScroller2.configure(font=font11)
        self.lblScroller2.configure(foreground="#000000")
        self.lblScroller2.configure(highlightbackground="#d9d9d9")
        self.lblScroller2.configure(highlightcolor="black")
        self.lblScroller2.configure(text='''Throttle''')

        self.lblScrollerVal2 = Label(master)
        self.lblScrollerVal2.place(relx=0.67, rely=0.88, height=73, width=406)
        self.lblScrollerVal2.configure(activebackground="#f9f9f9")
        self.lblScrollerVal2.configure(activeforeground="black")
        self.lblScrollerVal2.configure(background="#ffffff")
        self.lblScrollerVal2.configure(disabledforeground="#a3a3a3")
        self.lblScrollerVal2.configure(font=font11)
        self.lblScrollerVal2.configure(foreground="#000000")
        self.lblScrollerVal2.configure(highlightbackground="#d9d9d9")
        self.lblScrollerVal2.configure(highlightcolor="black")
        self.lblScrollerVal2.configure(text='''7''')

        self.temperatures_shown = False 
        self.timeoutRead()
        self.timeoutSwitch()
        
    def switchLabels(self):
        #global temperatures_shown
        self.temperatures_shown = not self.temperatures_shown
        self.updateView()
        self.timeoutSwitch(5.0)
        
    def randomValues(self):
#       global temperatures_shown, journeyTime, gpsLAT, gpsLONG, mph, mpg, revs, miles, throttle, load, engine_temp, air_temp, scrollVal1, scrollVal2
        self.count += 1
        if(self.count % 2 == 0):
            self.journeyTime += 1
        self.gpsLAT = randint(0.0,90.0)
        self.gpsLONG = randint(0.0,180.0)
        self.mph = randint(30,40)
        self.mpg = randint(40,50)
        self.revs = randint(2000,3000)
        self.miles += 0.1
        self.throttle += 1
        if(self.throttle > 20):
            self.throttle = 0
        self.engine_load = randint(100,200)
        self.engine_temp = randint(100,130)
        self.air_temp = randint(9,10)\
        
        
        self.updateView()
        self.timeoutRead()
        
    def readValues(self):
        global jsonfile
        global connection
        comms = obd.commands
        #currentValues = json.load(jsonfile)
        
        self.count += 1
        if(self.count % 2 == 0):
            self.journeyTime += 1
        self.gpsLAT = randint(0.0,90.0)
        self.gpsLONG = randint(0.0,180.0)
	try:
	    self.mph =  float(connection.query(comms['SPEED']).value)
	except:
	    self.mph = randint(0.0, 30.0)
			
        self.mpg = randint(40,50)
        self.revs = connection.query(comms['RPM']).value
        self.miles += 0.1
        self.throttle = connection.query(comms['THROTTLE_POS']).value
        self.engine_load = connection.query(comms['ENGINE_LOAD']).value
        self.engine_temp = connection.query(comms['COOLANT_TEMP']).value
        self.air_temp = connection.query(comms['INTAKE_TEMP']).value
        
        # From http://stackoverflow.com/questions/17170646/fuel-consumption-from-obd2-port-parameters
        # To calculate, MPG = VSS (Vehicle speed in Km/Hr) * 7.718/MAF (Air Flow Rate)
        try:
            maf = connection.query(comms['MAF']).value
            self.mpg = self.speed * 7.718/maf
        except:
            self.mpg = 0
        self.updateView()
        self.update_log_file()
        self.timeoutRead()
    
    def update_log_file(self):
	comms = obd.commands
        # Update the dictionary
        self.drive_data['distance_travelled'] = self.miles
        temp_data = {
           'timestamp' : "%s" % datetime.utcnow(),
            'engine_rpm' : self.revs,
            'speed' : self.mph,
            'engine_cooland_temperature' : self.engine_temp,
            'engine_load_value' : self.engine_load,
            'throttle_position' : self.throttle,
            'ambient_air_temperature' : self.air_temp,
            'latitude' : self.gpsLAT,
            'longitude' : self.gpsLONG,
            'consumption' : self.mpg
        }
        
        self.drive_data['events'].append(temp_data)
        
        outfile = open("log.json", "w")
        json.dump(self.drive_data, outfile, indent=4)
        outfile.close()
        
    def updateView(self):
        #global temperatures_shown, journeyTime, gpsLAT, gpsLONG, mph, mpg, revs, miles, throttle, load, engine_temp, air_temp
        sec = timedelta(seconds=int(self.journeyTime))
        d = datetime(1,1,1) + sec
    
        self.lblTime.configure(text=str(d.hour) + "h " + str(d.minute) + "m " + str(d.second) + "s")
        self.lblGPS.configure(text=str(self.gpsLAT) + "N" + str(self.gpsLONG) + "E")
        self.lblMilesVal.configure(text=str(self.miles) + "m")
        self.lblMPH.configure(text=str(self.mph) + "mph")
        self.lblMPG.configure(text=str(self.mpg) + "mpg")
        self.lblRPM.configure(text=str(self.revs) + "rpm")
        if(self.temperatures_shown):
            self.lblScroller1.configure(text='''Engine''')
            self.lblScrollerVal1.configure(text=str(self.engine_temp) + u"\u00B0" + "C")
            self.lblScroller2.configure(text='''Air''')
            self.lblScrollerVal2.configure(text=str(self.air_temp) + u"\u00B0" + "C")
        else:
            self.lblScroller1.configure(text='''Load''')
            self.lblScrollerVal1.configure(text=str(self.engine_load))
            self.lblScroller2.configure(text='''Throttle''')
            self.lblScrollerVal2.configure(text=str(self.throttle) + "%")
        
    def timeoutSwitch(self):
        threading.Timer(5.0, self.switchLabels).start()
            
    def timeoutRead(self):

        threading.Timer(0.5, self.readValues).start()
        
if __name__ == '__main__':
    vp_start_gui()



