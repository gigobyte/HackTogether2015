import Tkinter
from datetime import *
from world_time import req, GetTime, Clock
from PIL import Image, ImageTk
import sys

global second
second = 0
global t
t = GetTime(sys.argv[1])
print t

def onClosing():
	global root
	root.destroy()

def update_timeText():
    # Get the current time, note you can change the format as you wish
    	global second
	global t
	local = datetime.now()
	l_sec = local.second
	if l_sec > second or l_sec == 0 and second == 59:
		second = l_sec
		t = t + timedelta(seconds = 1)
	current = t.strftime("%H:%M:%S")
    # Update the timeText Label box with the current time
	timeText.configure(text=current, background='white')
    # Call the update_timeText() function after 1 second
	root.after(1000, update_timeText)

global root
root = Tkinter.Tk()
root.overrideredirect(1)
root.configure(background='white')
root.wm_title("World Clock")
root.geometry("170x46+1195+360")

''' SHOW EXIT ICON '''
exit_image = ImageTk.PhotoImage(file="images/exit.png")
exit_button = Tkinter.Button(root, image =exit_image, command = onClosing, background = "white", bd = 0)
exit_button.pack(anchor = "se")

# Create a timeText Label (a text box)
timeText = Tkinter.Label(root, text="", font=("Helvetica", 20))
timeText.pack()
update_timeText()
root.mainloop()
