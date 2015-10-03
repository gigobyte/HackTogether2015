from system_tray_lib import *
import adb

if __name__ == '__main__':
    import itertools, glob
    device = adb.get_device_model()
    print device
    
    
    icons = itertools.cycle(glob.glob('*.ico'))
    hover_text = "Smartphone Voice"
    def hello(sysTrayIcon): print "Hello World."
    def simon(sysTrayIcon): print "Hello Simon."
    def switch_icon(sysTrayIcon):
        sysTrayIcon.icon = icons.next()
        sysTrayIcon.refresh_icon()
    menu_options = (('Say Hello', icons.next(), hello),
                    ('Switch Icon', None, switch_icon),
                    ('A sub-menu', icons.next(), (('Say Hello to Simon', icons.next(), simon),
                                                  ('Switch Icon', icons.next(), switch_icon),
                                                 ))
                   )
    def bye(sysTrayIcon): print 'Bye, then.'
    
    SysTrayIcon(icons.next(), hover_text, menu_options, on_quit=bye, default_menu_index=1)
