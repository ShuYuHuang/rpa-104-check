import pyautogui as gui
import time
from datetime import datetime

def press():
    # Vol Down
    gui.press(['volumedown']*10)

    # Change key-in language if needed
    loc = gui.locateCenterOnScreen('ber.png') # returns x,y of matching region
    if loc:  
        gui.moveTo(loc[0]+2, loc[1]+2)
        gui.click(button='left')
        time.sleep(0.5)
        loc2 = gui.locateCenterOnScreen('eng_key.png')
        if loc2:
            gui.moveTo(loc2[0]+2, loc2[1]+2)
            gui.click(button='left')
    
    # Enter Search
    gui.hotkey('win', 's')

    # Search
    time.sleep(1)
    gui.write('edge')
    gui.press('enter')
    time.sleep(1)
    
    # Tune Window size
    with gui.hold('win'):
        for i in range(3):
            gui.press('up')  # zoom to fit
            time.sleep(0.2)
    gui.moveTo(50, 50)
    gui.click(button='left')
    time.sleep(1)
    
    # Enter page
    gui.hotkey('ctrl', 'l')  # to url block
    gui.write('https://pro.104.com.tw/psc2/m4/f0400')
    gui.press('enter')
    time.sleep(2)
    
    # Login if needed
    loc = gui.locateCenterOnScreen('login_btn.png') # returns x,y of matching region
    if not loc:
        loc = gui.locateCenterOnScreen('login_btn2.png')
    if loc:  
        gui.moveTo(loc[0], loc[1])
        gui.click(button='left')
    time.sleep(5)
    
    # Press
    loc = gui.locateCenterOnScreen('option.png') # returns x,y of matching region
    if not loc:
        loc = gui.locateCenterOnScreen('option2.png')
    if loc:
        gui.moveTo(loc[0], loc[1]+140)
        gui.click(button='left')
        print("check",datetime.now())
    else:
        print("option not found")
    
    time.sleep(5)    
    gui.hotkey('alt', 'f4')   
    time.sleep(1) 


# Improve the efficiency of the `locateCenterOnScreen()` function
def locateCenterOnScreen(image_path):
    try:
        return gui.locateCenterOnScreen(image_path)
    except:
        return None


# Improve the readability of the code
def check_login_button():
    loc = locateCenterOnScreen('login_btn.png')
    if not loc:
        loc = locateCenterOnScreen('login_btn2.png')
    return loc is not None


# Improve the error handling of the code
def press_button(image_path):
    loc = locateCenterOnScreen(image_path)
    if loc is not None:
        gui.moveTo(loc[0], loc[1])
        gui.click(button='left')
        print("check",datetime.now())
    else:
        print("button not found")


if __name__ == "__main__":
    press()