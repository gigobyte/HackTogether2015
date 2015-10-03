from system_tray_lib import *
import Tkinter
from Tkinter import *
from PIL import Image, ImageTk
import urllib
import adb
import requests

def on_closing():
    top.destroy()
    icons = itertools.cycle(glob.glob('*.ico'))
    hover_text = "Smartphone Voice"
    menu_options = (('Start', None, main),)
    SysTrayIcon(icons.next(), hover_text, menu_options, on_quit=None, default_menu_index=1)

def showSmartphone():
    x = 0
    y = 0
    image = Image.open('phone.jpg')
    image_size = image.size
    photoImage = ImageTk.PhotoImage(image)
    label = Label(image=photoImage)
    label.image = photoImage
    label.place(x=x, y=y)

def showText(width, height, device):
    set_width = (((width - 130)/2)/2)
    print set_width
    connect_to_string = "Connected to " + device + ":"
    connect_to = Label(text=connect_to_string)
    connect_to.text = connect_to_string
    connect_to.place(x=set_width, y=height)
    

def gui(device):
    flag = 0;
    top.title("Smartphone Voice")
    top.wm_iconbitmap('voice15.ico')
    image = Image.open('phone.jpg')
    image_size = image.size
    top.resizable(width=FALSE, height=FALSE)
    top.geometry('{}x{}'.format(image_size[0], image_size[1]+40))
    if (flag == 0):
        showText(image_size[1], image_size[1], device)
        showSmartphone()
        flag = 1
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.mainloop()

def main():
    device = adb.get_device_model()
    print device
    url = "http://www.gsmarena.com/results.php3?sQuickSearch=yes&sName=" + device
    scraped_page = requests.get(url).text
    scraped_page = scraped_page.split("http://cdn2.gsmarena.com/vv/bigpic/")[1].split("alt=")[0].split(";")[0]
    scraped_gsm_image = scraped_page[:-1]
    global top
    top = Tkinter.Tk()
    urllib.urlretrieve("http://cdn2.gsmarena.com/vv/bigpic/%s" % scraped_gsm_image, "phone.jpg")
    gui(device)
    

if __name__ == '__main__':
    import itertools, glob
    main()
