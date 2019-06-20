import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


#print screen size
screenWidth, screenHeight = pyautogui.size()
print screenWidth, screenHeight


#get the current location of mouse
print pyautogui.position()

#check if coordiantes onscreen or not
print pyautogui.onScreen(-1,-1)

pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right')
"""
for i in range(5):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
      i=i+1
"""