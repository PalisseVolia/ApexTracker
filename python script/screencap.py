import pyautogui
import time

left = 880
top = 507
width = 600
height = 40
RightScrollx= 2220
RightScrolly = 1145
LeftScrollx = 830
LeftScrolly = 970
Buttonx = 630
Buttony = 525

weekStart = 1
weekEnd = 11

def captureScreen(newtop, n) :
    region = (left, newtop, width, height)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('images\\{}.png'.format(n))
    print('Screenshot saved as {}.png'.format(n))

def GetWeek():
    
    time.sleep(2)
    
    newtop = top
    newButtonx = Buttonx
    newButtony = Buttony
    for j in range(0, 5):
        pyautogui.click(newButtonx, newButtony+j*75)
        pyautogui.click(newButtonx+10, newButtony+j*75)
        time.sleep(1)
        if j >= weekStart-1 and j < weekEnd:
            for i in range(0, 4):
                captureScreen(newtop+i*94, i+1+(j+1)*100)
            time.sleep(1)
            pyautogui.click(RightScrollx, RightScrolly)
            pyautogui.click(RightScrollx, RightScrolly)
            time.sleep(1)
            for i in range(0, 7):
                captureScreen(newtop+i*94, i+5+(j+1)*100)
            time.sleep(1)
            pyautogui.click(RightScrollx, RightScrolly-600)
            pyautogui.click(RightScrollx+5, RightScrolly-600)
            time.sleep(1)
    
    newButtonx = Buttonx
    newButtony = Buttony
    
    pyautogui.click(LeftScrollx, LeftScrolly)
    pyautogui.click(LeftScrollx, LeftScrolly+10)
    pyautogui.click(LeftScrollx, LeftScrolly-10)
    pyautogui.click(LeftScrollx-100, LeftScrolly+10)
    pyautogui.click(LeftScrollx-100, LeftScrolly-10)
    time.sleep(2)
    
    for j in range(0, 7):
        pyautogui.click(newButtonx, newButtony+j*75)
        pyautogui.click(newButtonx+10, newButtony+j*75)
        time.sleep(1)
        if j+5 >= weekStart-1 and j+5 < weekEnd:
            for i in range(0, 4):
                captureScreen(newtop+i*94, i+1+(j+6)*100)
            time.sleep(1)
            pyautogui.click(RightScrollx, RightScrolly)
            pyautogui.click(RightScrollx, RightScrolly)
            time.sleep(1)
            newtop = top
            for i in range(0, 7):
                captureScreen(newtop+i*94, i+5+(j+6)*100)
            time.sleep(1)
            pyautogui.click(RightScrollx, RightScrolly-600)
            pyautogui.click(RightScrollx+5, RightScrolly-600)
            time.sleep(1)
        
    time.sleep(2)

GetWeek()