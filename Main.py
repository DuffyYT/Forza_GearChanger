import mouse
import keyboard

toggle = False

def gearUp():
    if toggle:        
        keyboard.press_and_release('e')

def gearDown():
    if toggle:        
        keyboard.press_and_release('q')

def switch():
    global toggle
    toggle = not toggle

mouse.on_click(lambda:gearUp())
mouse.on_right_click(lambda:gearDown())

keyboard.on_press_key('/',lambda _:switch())

a = input("press '/' key to toggle on and off\nClick enter to while in focus to turn off script")