#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.4.5
# In conjunction with Tcl version 8.6
#    Jan 16, 2015 03:19:29 PM
import sys

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

import real-time-gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Real_Time_Display')
    root.geometry('1265x692+2+83')
    w = Real_Time_Display (root)
    real-time-gui_support.init(root, w)
    root.mainloop()

w = None
def create_Real_Time_Display(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('Real_Time_Display')
    w.geometry('1265x692+2+83')
    w_win = Real_Time_Display (w)
    real-time-gui_support.init(w, w_win, param)
    return w_win

def destroy_Real_Time_Display():
    global w
    w.destroy()
    w = None


class Real_Time_Display:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Miriam Fixed} -size 48 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Miriam Fixed} -size 36 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Miriam Fixed} -size 20 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font17 = "-family {Miriam Fixed} -size 72 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        master.configure(background="#ffffff")


        self.lblSpeed = Label(master)
        self.lblSpeed.place(relx=0.18, rely=0.29, height=101, width=301)
        self.lblSpeed.configure(background="#ffffff")
        self.lblSpeed.configure(disabledforeground="#a3a3a3")
        self.lblSpeed.configure(font=font17)
        self.lblSpeed.configure(foreground="#000000")
        self.lblSpeed.configure(text='''25MPH''')

        self.lblinfo1 = Label(master)
        self.lblinfo1.place(relx=0.2, rely=0.42, height=33, width=276)
        self.lblinfo1.configure(activebackground="#f9f9f9")
        self.lblinfo1.configure(activeforeground="black")
        self.lblinfo1.configure(background="#ffffff")
        self.lblinfo1.configure(disabledforeground="#a3a3a3")
        self.lblinfo1.configure(font=font16)
        self.lblinfo1.configure(foreground="#000000")
        self.lblinfo1.configure(highlightbackground="#d9d9d9")
        self.lblinfo1.configure(highlightcolor="black")
        self.lblinfo1.configure(text='''speed''')
        self.lblinfo1.configure(width=276)

        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)



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
        self.lblScrollerVal1.configure(width=406)

        self.Label7 = Label(master)
        self.Label7.place(relx=0.72, rely=0.03, height=53, width=126)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font13)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''GPS:''')

        self.lblMPG = Label(master)
        self.lblMPG.place(relx=0.57, rely=0.29, height=101, width=301)
        self.lblMPG.configure(activebackground="#f9f9f9")
        self.lblMPG.configure(activeforeground="black")
        self.lblMPG.configure(background="#ffffff")
        self.lblMPG.configure(disabledforeground="#a3a3a3")
        self.lblMPG.configure(font=font17)
        self.lblMPG.configure(foreground="#000000")
        self.lblMPG.configure(highlightbackground="#d9d9d9")
        self.lblMPG.configure(highlightcolor="black")
        self.lblMPG.configure(text='''40MPG''')

        self.lblinfo2 = Label(master)
        self.lblinfo2.place(relx=0.58, rely=0.42, height=33, width=282)
        self.lblinfo2.configure(activebackground="#f9f9f9")
        self.lblinfo2.configure(activeforeground="black")
        self.lblinfo2.configure(background="#ffffff")
        self.lblinfo2.configure(disabledforeground="#a3a3a3")
        self.lblinfo2.configure(font=font16)
        self.lblinfo2.configure(foreground="#000000")
        self.lblinfo2.configure(highlightbackground="#d9d9d9")
        self.lblinfo2.configure(highlightcolor="black")
        self.lblinfo2.configure(text='''consumption''')
        self.lblinfo2.configure(width=282)

        self.Label8 = Label(master)
        self.Label8.place(relx=0.02, rely=0.03, height=53, width=156)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font13)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Time:''')

        self.lblGPS = Label(master)
        self.lblGPS.place(relx=0.81, rely=0.03, height=53, width=216)
        self.lblGPS.configure(activebackground="#f9f9f9")
        self.lblGPS.configure(activeforeground="black")
        self.lblGPS.configure(background="#ffffff")
        self.lblGPS.configure(disabledforeground="#a3a3a3")
        self.lblGPS.configure(font=font13)
        self.lblGPS.configure(foreground="#000000")
        self.lblGPS.configure(highlightbackground="#d9d9d9")
        self.lblGPS.configure(highlightcolor="black")
        self.lblGPS.configure(text='''25N 34E''')

        self.lblTime = Label(master)
        self.lblTime.place(relx=0.13, rely=0.03, height=53, width=336)
        self.lblTime.configure(activebackground="#f9f9f9")
        self.lblTime.configure(activeforeground="black")
        self.lblTime.configure(background="#ffffff")
        self.lblTime.configure(disabledforeground="#a3a3a3")
        self.lblTime.configure(font=font13)
        self.lblTime.configure(foreground="#000000")
        self.lblTime.configure(highlightbackground="#d9d9d9")
        self.lblTime.configure(highlightcolor="black")
        self.lblTime.configure(text='''25min 32sec''')

        self.lblRPM = Label(master)
        self.lblRPM.place(relx=0.32, rely=0.53, height=101, width=419)
        self.lblRPM.configure(activebackground="#f9f9f9")
        self.lblRPM.configure(activeforeground="black")
        self.lblRPM.configure(background="#ffffff")
        self.lblRPM.configure(disabledforeground="#a3a3a3")
        self.lblRPM.configure(font=font17)
        self.lblRPM.configure(foreground="#000000")
        self.lblRPM.configure(highlightbackground="#d9d9d9")
        self.lblRPM.configure(highlightcolor="black")
        self.lblRPM.configure(text='''1000RPM''')

        self.lblinfo3 = Label(master)
        self.lblinfo3.place(relx=0.35, rely=0.66, height=33, width=380)
        self.lblinfo3.configure(activebackground="#f9f9f9")
        self.lblinfo3.configure(activeforeground="black")
        self.lblinfo3.configure(background="#ffffff")
        self.lblinfo3.configure(disabledforeground="#a3a3a3")
        self.lblinfo3.configure(font=font16)
        self.lblinfo3.configure(foreground="#000000")
        self.lblinfo3.configure(highlightbackground="#d9d9d9")
        self.lblinfo3.configure(highlightcolor="black")
        self.lblinfo3.configure(text='''revs''')
        self.lblinfo3.configure(width=380)

        self.lblScroller2 = Label(master)
        self.lblScroller2.place(relx=0.67, rely=0.79, height=53, width=406)
        self.lblScroller2.configure(activebackground="#f9f9f9")
        self.lblScroller2.configure(activeforeground="black")
        self.lblScroller2.configure(background="#ffffff")
        self.lblScroller2.configure(disabledforeground="#a3a3a3")
        self.lblScroller2.configure(font=font13)
        self.lblScroller2.configure(foreground="#000000")
        self.lblScroller2.configure(highlightbackground="#d9d9d9")
        self.lblScroller2.configure(highlightcolor="black")
        self.lblScroller2.configure(text='''Throttle''')
        self.lblScroller2.configure(width=406)

        self.lblScroller1 = Label(master)
        self.lblScroller1.place(relx=0.01, rely=0.79, height=53, width=406)
        self.lblScroller1.configure(activebackground="#f9f9f9")
        self.lblScroller1.configure(activeforeground="black")
        self.lblScroller1.configure(background="#ffffff")
        self.lblScroller1.configure(disabledforeground="#a3a3a3")
        self.lblScroller1.configure(font=font13)
        self.lblScroller1.configure(foreground="#000000")
        self.lblScroller1.configure(highlightbackground="#d9d9d9")
        self.lblScroller1.configure(highlightcolor="black")
        self.lblScroller1.configure(text='''Load''')
        self.lblScroller1.configure(width=406)

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
        self.lblScrollerVal2.configure(width=406)

        self.lblMiles = Label(master)
        self.lblMiles.place(relx=0.34, rely=0.79, height=53, width=406)
        self.lblMiles.configure(activebackground="#f9f9f9")
        self.lblMiles.configure(activeforeground="black")
        self.lblMiles.configure(background="#ffffff")
        self.lblMiles.configure(disabledforeground="#a3a3a3")
        self.lblMiles.configure(font=font13)
        self.lblMiles.configure(foreground="#000000")
        self.lblMiles.configure(highlightbackground="#d9d9d9")
        self.lblMiles.configure(highlightcolor="black")
        self.lblMiles.configure(text='''Miles''')
        self.lblMiles.configure(width=406)

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
        self.lblMilesVal.configure(width=406)






if __name__ == '__main__':
    vp_start_gui()



