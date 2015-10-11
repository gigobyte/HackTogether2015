import Tkinter as tk
from datetime import *
from world_time import req, GetTime, Clock

global second
second = 0
global t
t = GetTime('London')
print t

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

root = tk.Tk()
root.overrideredirect(1)
root.configure(background='white')
root.wm_title("World Clock")
root.geometry("110x50+1120+300")

# Create a timeText Label (a text box)
timeText = tk.Label(root, text="", font=("Helvetica", 20))
timeText.pack()
update_timeText()
root.mainloop()
