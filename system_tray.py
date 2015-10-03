from system_tray_lib import *
import Tkinter
import sys
from Tkinter import *
from PIL import Image, ImageTk
import urllib
import adb
import requests
import threading

def startSystemTray():
    global device
    icons = itertools.cycle(glob.glob('images/*.ico'))
    hover_text = "Smartphone Voice"
    menu_options = (('Stop', None, microphoneAction),)
    SysTrayIcon(icons.next(), hover_text, menu_options, on_quit=onClosing, default_menu_index=1)

def onClosing():
    sys.exit()
    

def showSmartphone():
    image = Image.open('phone.jpg')
    image_size = image.size
    photoImage = ImageTk.PhotoImage(image)
    label = Label(image=photoImage, background = 'white')
    label.image = photoImage
    label.place(x=0, y=0)

def showText(width, height, device):
    set_width = (((width - 130)/2)/2)
    print set_width
    connect_to_string = "Connected to " + device + ":"
    connect_to = Label(text=connect_to_string, background = 'white')
    connect_to.text = connect_to_string
    connect_to.place(x=set_width, y=height)

def microphoneAction():
    global microphone_check
    print microphone_check
    global device
    microphone_check = not microphone_check
    gui(device)

def gui(device):
    global top
    global microphone_check
    flag = 0
    top.overrideredirect(1)
    top.title("Smartphone Voice")
    top.wm_iconbitmap('images/voice15.ico')
    top.configure(background='white')
    image = Image.open('phone.jpg')
    
    image_size = image.size
    width = image_size[0]
    global height
    height = image_size[1]
    global set_width
    set_width = width - 125
    
    top.resizable(width=FALSE, height=FALSE)
    ws = top.winfo_screenwidth() # width of the screen
    hs = top.winfo_screenheight() # height of the screen
    x = (ws/1.2) - (width/2)
    y = (hs/1.5) - (height/2)
    top.geometry('%dx%d+%d+%d' % (width, height+92, x, y))
    
    microphone_image = ImageTk.PhotoImage(file="images/mic_on.png")
    if (microphone_check == 0):
        microphone_image = ImageTk.PhotoImage(file="images/mic_on.png")
    else:
        microphone_image = ImageTk.PhotoImage(file="images/mic_off.png")
    microphone = Tkinter.Button(top, image =microphone_image, command = microphoneAction)
    microphone.place(x=set_width, y=(height+20))
        
    if (flag == 0):
        showText(width, height, device)
        showSmartphone()
        flag = 1
    
    top.protocol("WM_DELETE_WINDOW", onClosing)
    
    top.mainloop()

def main():
    global device
    device = adb.get_device_model()
    print device
    url = "http://www.gsmarena.com/results.php3?sQuickSearch=yes&sName=" + device
    scraped_page = requests.get(url).text
    scraped_page = scraped_page.split("http://cdn2.gsmarena.com/vv/bigpic/")[1].split("alt=")[0].split(";")[0]
    scraped_gsm_image = scraped_page[:-1]
    global top
    global microphone_check
    microphone_check = 0
    top = Tkinter.Tk()
    urllib.urlretrieve("http://cdn2.gsmarena.com/vv/bigpic/%s" % scraped_gsm_image, "phone.jpg")
    t = threading.Thread(target=startSystemTray)
    t.daemon = True
    t.start()
    gui(device)
    

if __name__ == '__main__':
    import itertools, glob
    main()
