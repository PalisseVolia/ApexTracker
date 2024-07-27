import pyautogui
import time

monitorWidth, monitorHeight = pyautogui.size()

left = 0.345*monitorWidth
top = 0.355*monitorHeight
width = 0.32*monitorWidth
height = 0.05*monitorHeight

WeekOneX = 0.2*monitorWidth
WeekOneY = 0.525*monitorHeight

def captureScreen(newtop, n) :
    region = (int(left), int(newtop), int(width), int(height))
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('images\\{}.png'.format(n))
    print('Screenshot saved as {}.png'.format(n))

def captureChallenges(week, n) :
    for i in range(4 if n>4 else 0, n+4 if n>4 else n) :
        captureScreen(top+(i-4 if n>4 else i)*0.066*monitorHeight, i+1+(week)*100)
        
def rightScrollUP() :
    pyautogui.doubleClick(0.865*monitorWidth, 0.38*monitorHeight)

def selectWeekOne() :
    for i in range(0, 2):
        pyautogui.click(WeekOneX+0.125*monitorWidth, WeekOneY)
    for i in range(0, 3):
        pyautogui.click(WeekOneX+i*10, WeekOneY)
    time.sleep(1)

def nextWeek():
    pyautogui.press('down')
    time.sleep(1)

def captureFirstFour() :
    selectWeekOne()
    for i in range(1, 13):
        captureChallenges(i, 4)
        time.sleep(1)
        nextWeek()

# TODO: captureLastSeven
def captureLastSeven() :
    selectWeekOne()
    for i in range(1, 13):
        captureChallenges(i, 11)
        time.sleep(1)
        nextWeek()
time.sleep(3)

rightScrollUP()
