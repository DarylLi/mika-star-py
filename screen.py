import pyautogui
import win32api
import win32con
import time
import keyboard
pyautogui.FAILSAFE = False
num = 0
refreshCurrent = None
purchase = None
goback = None
error1 = None
error2 = None
def left_mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    # time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    # time.sleep(0.05)
def check_and_buy(curResource):
    limit = 100
    global purchase
    global goback
    global error1
    global error2
    if curResource is not None:
        pyautogui.moveTo(curResource.x, curResource.y)
        left_mouse_click()
        time.sleep(0.5)
        while True:
            if limit <=0:
                pyautogui.moveTo(goback.x, goback.y)
                left_mouse_click()
                time.sleep(0.5)
                break
            if purchase is None:
                try:
                    purchase = pyautogui.locateCenterOnScreen("buy.png", grayscale=True,confidence=0.8)
                except pyautogui.ImageNotFoundException:
                    print("我购买或返回按钮呢？")    
            if goback is None:
                try:
                    goback = pyautogui.locateCenterOnScreen("goback.png", grayscale=True,confidence=0.8)
                except pyautogui.ImageNotFoundException:
                    print("我购买或返回按钮呢？")    
            if purchase is not None:
                pyautogui.moveTo(purchase.x, purchase.y)
                left_mouse_click()
            # try:
            #     error1 = pyautogui.locateCenterOnScreen("error1.png", grayscale=True,confidence=0.8)
            #     error2 = pyautogui.locateCenterOnScreen("error2.png", grayscale=True,confidence=0.8)
            # except pyautogui.ImageNotFoundException:
            #     print("没提示就继续买入！")
            # if error1:
            #     pyautogui.moveTo(goback.x, goback.y)
            #     left_mouse_click()		
            #     time.sleep(0.5)
            #     break
            # if error2:
            #     pyautogui.moveTo(goback.x, goback.y)
            #     left_mouse_click()
            #     time.sleep(0.5)
            #     break
            limit -= 1

def load_and_init(num=1):
    imgSrc = "kuang{}.png".format(num)
    try:
        cResource = pyautogui.locateCenterOnScreen(imgSrc, grayscale=True,confidence=0.8)
        return cResource
    except pyautogui.ImageNotFoundException:
        print("矿%d没货"%num)
        return None
while True:
    # # 根据图片dishu1.png来找到屏幕上的相似的目标坐标并赋值给location_dishu
    pyautogui.useImageNotFoundException()
    if keyboard.is_pressed('esc'):
	    break;
    try:
        # 搜索点击按优先级排列：
        resource1 = None
        resource2 = None
        resource3 = None
        resource4 = None
        resource5 = None
        resource6 = None
        resource7 = None
        if refreshCurrent is None:
            refreshCurrent = pyautogui.locateCenterOnScreen("refresh2.png")
        # center = pyautogui.center(demo1)
        if refreshCurrent is not None:
			# 循环刷新
            time.sleep(0.3)
            pyautogui.click(refreshCurrent.x, refreshCurrent.y)
            left_mouse_click()
            resource1 = load_and_init(1)
            resource2 = load_and_init(2)
            resource3 = load_and_init(3)
            # resource4 = load_and_init(4)
            # resource5 = load_and_init(5)
            # resource6 = load_and_init(6)
            # resource7 = load_and_init(7)
			# 优先级买入
            # check_and_buy(resource7)           
            check_and_buy(resource1)
            check_and_buy(resource2)
            check_and_buy(resource3)
            # check_and_buy(resource4)
            # check_and_buy(resource5)
            # check_and_buy(resource6)           

    except pyautogui.ImageNotFoundException:
        print('ImageNotFoundException: image not found')
    
# im1 = pyautogui.screenshot()
# im1.save('my_screenshot.png')
# im2 = pyautogui.screenshot('my_screenshot2.png')
    