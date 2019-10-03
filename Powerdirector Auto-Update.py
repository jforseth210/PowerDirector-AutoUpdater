import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import easygui
import pyautogui

path = easygui.diropenbox()
print(path)
class MyHandler():
    def dispatch(self, event):
        filemodified=event.event_type=='modified'
        ispds='.pds' in event.src_path
        if filemodified and not event.is_directory and ispds:
            x,y=pyautogui.locateCenterOnScreen('filebutton.png')
            origx,origy=pyautogui.position()
            pyautogui.click(x,y)
            keypresses=[]
            for i in range(19):
                keypresses.append('down')
            pyautogui.press(keypresses)
            pyautogui.press('enter')
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.click(origx,origy)
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()