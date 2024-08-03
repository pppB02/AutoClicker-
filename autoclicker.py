from tkinter import *
from tkinter import ttk, messagebox
import keyboard
import time
import pyautogui
import threading


BACKGROUND = "#f5f5f5"
BORDER = "#dedad9"
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 360
HOTKEY = "F6"
NEW_HOTKEY = ""
LOCATION = "CURRENT"
POSITION = (0,0)

new_win_open = False
stop_event = threading.Event()

def main(hours, mins, secs, millisecs, c_button, c_type, c_repeat, c_repeatus, c_repeattimes):
    endTime = waitTime()
    if LOCATION == "CURRENT":
        if not endTime == None:
            time.sleep(int(waitTime()))
            if hours.isnumeric() and mins.isnumeric() and secs.isnumeric() and millisecs.isnumeric():
                fHours = (int(hours) * 60) * 60
                fMin = int(mins) * 60
                fSec = int(secs)
                fMillisec = int(millisecs) / 1000
                rTime = fHours + fMin + fSec + fMillisec
                c_button = c_button.lower()

                if c_type == "Single":
                    c_type = 1
                else:
                    c_type = 2

                if c_repeat == 1:
                    if c_repeattimes.isnumeric():
                        stop_event.clear()
                        keyboard.remove_hotkey(HOTKEY)
                        start["state"] = "disabled"
                        stop["state"] = "normal"
                        threading.Thread(target=clikerR, args=(rTime, c_button, c_type, c_repeattimes)).start()
                    else:
                        messagebox.showerror(title="Error", message="incorrect repetition number")
                else:
                    stop_event.clear()
                    keyboard.remove_hotkey(HOTKEY)
                    start["state"] = "disabled"
                    stop["state"] = "normal"
                    threading.Thread(target=clickerRUS, args=(rTime, c_button, c_type)).start()
            else:
                messagebox.showerror(message="incorrect time duration", title="Error")
        else:
            pass
    else:
        if not endTime == None:
            time.sleep(int(waitTime()))
            if hours.isnumeric() and mins.isnumeric() and secs.isnumeric() and millisecs.isnumeric():
                fHours = (int(hours) * 60) * 60
                fMin = int(mins) * 60
                fSec = int(secs)
                fMillisec = int(millisecs) / 1000
                rTime = fHours + fMin + fSec + fMillisec
                c_button = c_button.lower()

                if c_type == "Single":
                    c_type = 1
                else:
                    c_type = 2

                if c_repeat == 1:
                    if c_repeattimes.isnumeric():
                        stop_event.clear()
                        keyboard.remove_hotkey(HOTKEY)
                        start["state"] = "disabled"
                        stop["state"] = "normal"
                        threading.Thread(target=clikerRloc, args=(rTime, c_button, c_type, c_repeattimes)).start()
                    else:
                        messagebox.showerror(title="Error", message="incorrect repetition number")
                else:
                    stop_event.clear()
                    keyboard.remove_hotkey(HOTKEY)
                    start["state"] = "disabled"
                    stop["state"] = "normal"
                    threading.Thread(target=clickerRUSloc, args=(rTime, c_button, c_type)).start()
            else:
                messagebox.showerror(message="incorrect time duration", title="Error")
        else:
            pass

def waitTime():
    if waitEntHours.get().isnumeric() and waitEntMin.get().isnumeric() and waitEntSec.get().isnumeric() and waitEntMilsec.get().isnumeric():
        wHours = int(waitEntHours.get()) * 60
        wMins = int(waitEntMin.get()) * 60
        wSecs = int(waitEntSec.get())
        wMillisec = int(waitEntMilsec.get()) / 1000
        endTime = wHours + wMins + wSecs + wMillisec
        return endTime
    else:
        messagebox.showerror(message="incorrect time interval",title="Error")
def hotkey_handler():
    main(entHours.get(), entMin.get(), entSec.get(), entMilsec.get(), mouseButtonMenu.get(), clickTypeMenu.get(),
         intVarR.get(), intVarUS.get(), repeatNumber.get(),)
def disableBox(box, box_value):
    if box == "repeatBox":
        if box_value == 0:
            intVarUS.set(1)
        else:
            intVarUS.set(0)
    if box == "repeatBoxUS":
        if box_value == 0:
            intVarR.set(1)
        else:
            intVarR.set(0)
def clikerR(rtime, c_button, c_type,c_repeattimes):
    c_repeattimes = int(c_repeattimes)
    def on_hotkey_press():
        stop_event.set()
        start["state"] = "normal"
        stop["state"] = "disabled"

    keyboard.add_hotkey(HOTKEY, on_hotkey_press)

    for i in range(c_repeattimes):
        if not stop_event.is_set():
            time.sleep(rtime)
            pyautogui.click(button=c_button, clicks=c_type)
        else:
            break

    on_hotkey_press()
    keyboard.remove_hotkey(HOTKEY)
    keyboard.add_hotkey(HOTKEY, main, args=(
        entHours.get(), entMin.get(), entSec.get(), entMilsec.get(), mouseButtonMenu.get(), clickTypeMenu.get(),
        intVarR.get(), intVarUS.get(), repeatNumber.get()))

def clikerRloc(rtime, c_button, c_type,c_repeattimes):
    x, y = POSITION
    c_repeattimes = int(c_repeattimes)
    def on_hotkey_press():
        stop_event.set()
        start["state"] = "normal"
        stop["state"] = "disabled"

    keyboard.add_hotkey(HOTKEY, on_hotkey_press)

    for i in range(c_repeattimes):
        if not stop_event.is_set():
            time.sleep(rtime)
            pyautogui.click(x=x,y=y,button=c_button, clicks=c_type)
        else:
            break

    on_hotkey_press()
    keyboard.remove_hotkey(HOTKEY)
    keyboard.add_hotkey(HOTKEY, main, args=(
        entHours.get(), entMin.get(), entSec.get(), entMilsec.get(), mouseButtonMenu.get(), clickTypeMenu.get(),
        intVarR.get(), intVarUS.get(), repeatNumber.get()))
def clickerRUS(rtime, c_button, c_type):
    def on_hotkey_press():
        stop_event.set()
        start["state"] = "normal"
        stop["state"] = "disabled"

    keyboard.add_hotkey(HOTKEY, on_hotkey_press)

    while not stop_event.is_set():
        time.sleep(rtime)
        pyautogui.click(button=c_button, clicks=c_type)

    keyboard.remove_hotkey(HOTKEY)
    keyboard.add_hotkey(HOTKEY, main, args=(
    entHours.get(), entMin.get(), entSec.get(), entMilsec.get(), mouseButtonMenu.get(), clickTypeMenu.get(),
    intVarR.get(), intVarUS.get(), repeatNumber.get()))

def clickerRUSloc(rtime, c_button, c_type):
    x, y = POSITION
    def on_hotkey_press():
        stop_event.set()
        start["state"] = "normal"
        stop["state"] = "disabled"

    keyboard.add_hotkey(HOTKEY, on_hotkey_press)

    while not stop_event.is_set():
        time.sleep(rtime)
        pyautogui.click(x=x,y=y,button=c_button, clicks=c_type)

    keyboard.remove_hotkey(HOTKEY)
    keyboard.add_hotkey(HOTKEY, main, args=(
    entHours.get(), entMin.get(), entSec.get(), entMilsec.get(), mouseButtonMenu.get(), clickTypeMenu.get(),
    intVarR.get(), intVarUS.get(), repeatNumber.get()))

def stopClick():
    start["state"] = "normal"
    stop["state"] = "disabled"
    stop_event.set()

def new_window():
    global new_win_open
    if new_win_open:
        return
    NEW_WIDTH = 220
    NEW_HIGHT = 100

    new_x = int((SCREEN_WIDTH / 2) - (NEW_WIDTH / 2))
    new_y = int((SCREEN_HEIGHT / 2) - (NEW_HIGHT / 2))

    def quit():
        new_win.destroy()
    def save():
        global NEW_HOTKEY, HOTKEY
        if NEW_HOTKEY == "":
            NEW_HOTKEY = HOTKEY
        else:
            keyboard.remove_hotkey(HOTKEY)
            HOTKEY = NEW_HOTKEY
            keyboard.add_hotkey(HOTKEY, hotkey_handler)
            stop.config(text=f"Stop({HOTKEY})")
            start.config(text=f"Start({HOTKEY})")
            new_win.destroy()

    def listener():
        new_key = keyboard.read_key().upper()
        global NEW_HOTKEY
        NEW_HOTKEY = new_key.upper()
        hotkeyLabel.config(text=NEW_HOTKEY)

    new_win = Toplevel(window)
    new_win.resizable(False,False)
    new_win.geometry(f"{NEW_WIDTH}x{NEW_HIGHT}+{new_x}+{new_y}")
    new_win.config(background=BACKGROUND)
    new_win.title("Hotkey")
    new_win.iconphoto(False, PhotoImage(file="icon.png"))
    #new_win.focus_set()
    #new_win.grab_set()

    ssButton = Button(new_win,text="Start/Stop",width=10,height=1,font=("Console",10),command=listener)
    ssButton.place(x=15,y=16)

    hotkeyLabel = Label(new_win,width=6,font=("Console",17),justify=CENTER,text=HOTKEY,highlightbackground="black",highlightcolor="black",highlightthickness=1)
    hotkeyLabel.place(x=120,y=15)

    okButton = Button(new_win,text="Ok",command=save,width=9,font=("Console",9))
    okButton.place(x=30,y=65)

    cancelButton = Button(new_win,text="Cancel",command=quit,width=9,font=("Console",9))
    cancelButton.place(x=120,y=65)

    new_win.mainloop()
def location():
    global LOCATION
    LOCATION = "CURRENT"
    def picking():
        window.state('iconic')
        loc_window.state("iconic")
        messagebox.showinfo(message="press ESC to pick",title="INFO")
        while True:
            if keyboard.is_pressed("ESC"):
                global POSITION
                POSITION = pyautogui.position()[0:2]
                pickXent.delete(0,END)
                pickYent.delete(0,END)

                pickXent.insert(0,str(POSITION[0]))
                pickYent.insert(0,str(POSITION[1]))

                window.grab_set()
                window.state('normal')
                loc_window.grab_set()
                loc_window.state("normal")

                global LOCATION
                LOCATION = "PICKED"

                break
    def pickL():
        global LOCATION
        LOCATION = "PICKED"

        global POSITION
        POSITION = (int(pickXent.get()),int(pickYent.get()))

    def currentL():
        global LOCATION
        LOCATION = "CURRENT"

    def disableBoxLoc(box, box_value):
        if box == "currentBox":
            if box_value == 0:
                pickL()
                pickVar.set(1)
            else:
                currentL()
                pickVar.set(0)
        if box == "pickBox":
            if box_value == 0:
                currentL()
                currentVar.set(1)
            else:
                pickL()
                currentVar.set(0)

    loc_window = Toplevel(window)
    NEW_WIDTH = 450
    NEW_HIGHT = 140

    new_x = int((SCREEN_WIDTH / 2) - (NEW_WIDTH / 2))
    new_y = int((SCREEN_HEIGHT / 2) - (NEW_HIGHT / 2))

    loc_window.title("location")
    loc_window.resizable(False,False)
    loc_window.geometry(f"{NEW_WIDTH}x{NEW_HIGHT}+{new_x}+{new_y}")
    loc_window.config(background=BACKGROUND)
    loc_window.iconphoto(False, PhotoImage(file="icon.png"))

    # * Set time area *
    # Grey border
    cursorBorder = Label(loc_window,highlightcolor=BORDER, highlightbackground=BORDER, highlightthickness=1, width=60, height=7,
                       bg=BACKGROUND)
    cursorBorder.place(x=10, y=13)

    # "Click interval" text
    cursorLocation = Label(loc_window, text="Cursor position", font=("Console", 10), bg=BACKGROUND)
    cursorLocation.place(x=22, y=3)

    currentVar = IntVar()
    currentVar.set(1)
    currentBox = Checkbutton(loc_window,onvalue=1,offvalue=0,bg=BACKGROUND,activebackground=BACKGROUND,variable=currentVar,command=lambda:disableBoxLoc("currentBox",currentVar.get()))
    currentBox.place(x=20, y=28)

    currentLabel = Label(loc_window,text="Current location",font=("Console",10),bg=BACKGROUND)
    currentLabel.place(x=40,y=28)


    pickVar = IntVar()
    pickBox = Checkbutton(loc_window,onvalue=1,offvalue=0,bg=BACKGROUND,activebackground=BACKGROUND,variable=pickVar,command=lambda:disableBoxLoc("pickBox",pickVar.get()))
    pickBox.place(x=170, y=28)

    pickButton = Button(loc_window,text="Pick location",command=picking)
    pickButton.place(x=190, y=28)

    pickX = Label(loc_window,text="X",font=("Console",10),bg=BACKGROUND)
    pickX.place(x=280, y=28)

    pickXent = Entry(loc_window,font=("Console",10),width=5,justify=RIGHT)
    pickXent.place(x=295, y=30)
    pickXent.insert(0,"0")

    pickY = Label(loc_window,text="Y",font=("Console",10),bg=BACKGROUND)
    pickY.place(x=345, y=28)

    pickYent = Entry(loc_window,font=("Console",10),width=5,justify=RIGHT)
    pickYent.place(x=360, y=30)
    pickYent.insert(0,"0")
    loc_window.mainloop()



window = Tk()
window.config(bg=BACKGROUND)
window.title("Auto Clicker 1.0")
window.resizable(False, False)

SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()

x = int((SCREEN_WIDTH / 2) - (WINDOW_WIDTH / 2))
y = int((SCREEN_HEIGHT / 2) - (WINDOW_HEIGHT / 2))

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

window.iconphoto(False, PhotoImage(file="icon.png"))


#Set time area
timeBorder = Label(window,highlightcolor=BORDER, highlightbackground=BORDER, highlightthickness=1, width=60, height=3, bg=BACKGROUND)
timeBorder.place(x=10, y=10)

clickInterval = Label(window, text="Click interval", font=("Console", 10),bg=BACKGROUND)
clickInterval.place(x=22, y=0)


#Click options area
option = Label(window,highlightcolor=BORDER, highlightbackground=BORDER, highlightthickness=1, width=30, height=5, bg=BACKGROUND)
option.place(x=10, y=80)

clickOptions = Label(window, text="Click options", font=("Console", 10),bg=BACKGROUND)
clickOptions.place(x=22, y=70)

mouseButtonMenu = ttk.Combobox(window, values=["Left", "Right", "Middle"], state="readonly", width=10, background="black")
mouseButtonMenu.current(0)
mouseButtonMenu.place(x=125, y=100)

mouseButton = Label(window, text="Mouse button:", font=("Console", 9),bg=BACKGROUND)
mouseButton.place(x=25, y=100)

clickType = Label(window, text="Click type:", font=("Console", 9),bg=BACKGROUND)
clickType.place(x=25, y=130) # "Click type" text

clickTypeMenu = ttk.Combobox(window, values=["Single", "Double"], state="readonly", width=10, background="black")
clickTypeMenu.current(0)
clickTypeMenu.place(x=125, y=130)


#Click repeat area
option = Label(window,highlightcolor=BORDER, highlightbackground=BORDER, highlightthickness=1, width=27, height=5, bg=BACKGROUND)
option.place(x=241, y=80) # Grey border

clickRepeat = Label(window, text="Click repeat", font=("Console", 10),bg=BACKGROUND)
clickRepeat.place(x=263, y=70) # "Click repeat" text

intVarR = IntVar() # repeatBox variable
intVarUS = IntVar() # repeatBoxUS variable

repeatBox = Checkbutton(window, onvalue=1, offvalue=0, variable=intVarR,bg=BACKGROUND,activebackground=BACKGROUND,command=lambda:disableBox("repeatBox",intVarR.get()))
repeatBox.place(x=250, y=100) # "Repeat" checkbutton

repeatBoxUS = Checkbutton(window, onvalue=1, offvalue=0, variable=intVarUS,activebackground=BACKGROUND,bg=BACKGROUND,command=lambda:disableBox("repeatBoxUS",intVarUS.get()))
repeatBoxUS.select()
repeatBoxUS.place(x=250, y=130) # "repeat Until Stopped" checkbutton

repeat = Label(window, text="Repeat", font=("Console", 9),bg=BACKGROUND)
repeat.place(x=270, y=100) # "Repeat" text


repeatUS = Label(window, text="Repeat until stopped", font=("Console", 9),bg=BACKGROUND)
repeatUS.place(x=270, y=130) # "Repeat until stopped" text

repeatNumber = Spinbox(window, width=7, from_=1, to=999, justify=CENTER, bd=1)
repeatNumber.place(x=350, y=100) # Repeat spinbox

#"Wait before start" area
waitStart = Label(window,highlightcolor=BORDER, highlightbackground=BORDER, highlightthickness=1, width=60, height=3, bg=BACKGROUND)
waitStart.place(x=10, y=180)

waitStartLabel = Label(window, text="Wait before start", font=("Console", 10),bg=BACKGROUND)
waitStartLabel.place(x=22, y=170)

waitEntHours = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
waitEntHours.insert(0, "0")
waitEntHours.place(x=20, y=195)

waithours = Label(window, text="hours", font=("Console", 8),bg=BACKGROUND)
waithours.place(x=60, y=195)

waitEntMin = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
waitEntMin.insert(0, "0")
waitEntMin.place(x=120, y=195)

waitmins = Label(window, text="mins", font=("Console", 8),bg=BACKGROUND)
waitmins.place(x=160, y=195)

waitEntSec = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
waitEntSec.insert(0, "0")
waitEntSec.place(x=220, y=195)

waitsecs = Label(window, text="secs", font=("Console", 8), bg=BACKGROUND)
waitsecs.place(x=260, y=195)

waitEntMilsec = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
waitEntMilsec.insert(0, "0")
waitEntMilsec.place(x=320, y=195)

waitmilliseconds = Label(window, text="milliseconds", font=("Console", 8), bg=BACKGROUND)
waitmilliseconds.place(x=360, y=195)

#"Click interval" area
entHours = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
entHours.insert(0, "0")
entHours.place(x=20, y=25)

hours = Label(window, text="hours", font=("Console", 8),bg=BACKGROUND)
hours.place(x=60, y=25)

entMin = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
entMin.insert(0, "0")
entMin.place(x=120, y=25)

mins = Label(window, text="mins", font=("Console", 8),bg=BACKGROUND)
mins.place(x=160, y=25)

entSec = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
entSec.insert(0, "0")
entSec.place(x=220, y=25)

secs = Label(window, text="secs", font=("Console", 8), bg=BACKGROUND)
secs.place(x=260, y=25)

entMilsec = Entry(window, width=5, font=("Console", 10),justify=RIGHT)
entMilsec.insert(0, "100")
entMilsec.place(x=320, y=25)

milliseconds = Label(window, text="milliseconds", font=("Console", 8), bg=BACKGROUND)
milliseconds.place(x=360, y=25)

start = Button(window, text=f"Start({HOTKEY})", width=25, height=2, command=lambda: main(entHours.get(), entMin.get(), entSec.get(), entMilsec.get(), mouseButtonMenu.get(), clickTypeMenu.get(), intVarR.get(), intVarUS.get(), repeatNumber.get()))
start.place(x=20, y=260)

stop = Button(window, text=f"Stop({HOTKEY})", width=25, height=2, command=stopClick)
stop.place(x=245, y=260)
stop["state"] = "disabled"

hotkey = Button(window, text="Hotkey setting", width=25, height=2, command=new_window)
hotkey.place(x=20, y=310)

locationButton = Button(window, text="Location", width=25, height=2, command=location)
locationButton.place(x=245, y=310)

keyboard.add_hotkey(HOTKEY,hotkey_handler)

window.mainloop()

# TODO: record button


