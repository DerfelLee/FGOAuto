import cv2
import pyautogui
import numpy as np
import random
import time

# 基本信息
def BasicInf(Servants):
    skills = [[0]*3 for i in range(3)]
    S_img = [[0] for i in range(3)]
    S_np = [[0] for i in range(3)]

    for i in range(3):
        for j in range(3):
            skills[i][j] = 'images/Servants/'+Servants[i]+'/Skill'+str(j+1)+'.png'

    for i in range(3):
        S_img[i] = 'images/Servants/'+Servants[i]+'/Battle.png'
        S_np[i] = 'images/Servants/'+Servants[i]+'/NP.png'

    S = FindServant(Servants[0])
    C = FindCards(S)
        
    return skills, S_img, S_np, S, C


# 点按按钮
def Press(dir, roi=(0, 0, 1920, 1080)):
    img = cv2.imread(dir)
    x = pyautogui.locateCenterOnScreen(img, confidence=0.8, region=roi)
    if x:
        pyautogui.click(x)
        print('Pressed on ' + str(x))
    else:
        print('No such image on screen, nothing pressed')
    return x

# 寻找从者
def FindServant(servant):
    roi = {}
    img_dir = 'images/Servants/' + servant + '/BattlePanel.png'
    img = cv2.imread(img_dir)
    x = pyautogui.locateOnScreen(img, confidence=0.9)
    top = x.top - 3*x.height
    height = x.height*4
    roi[0] = (x.left, top, x.width, height)

    left2 = x.left + int(1.15*x.width)
    roi[1] = (left2, top, x.width, height)

    left3 = left2 + int(1.15*x.width)
    roi[2] = (left3, top, x.width, height)

    return roi

# 获取指令卡
def FindCards(S):
    S = S[0]
    left = S[0]
    top = S[1]
    width = S[2]
    height = S[3]

    cards = {}
    cards[0] = [left + int(0.4*width), top]
    cards[1] = [left + int(1.2*width), top]
    cards[2] = [left + int(2.2*width), top]
    cards[3] = [left + int(3.0*width), top]
    cards[4] = [left + int(4.2*width), top]

    return cards

def PressRandomCards(Cards, CNumber):
    randcard = random.sample(range(0,4), CNumber)
    for i in range(CNumber):
        pyautogui.click(Cards[randcard[i]]); time.sleep(3)
        print('Pressed Card '+str(randcard[i]))
    return

def ChangeServantLocations(S):
    S = S[0]
    left = S[0]
    top = S[1]
    width = S[2]
    height = S[3]

    servs = {}
    servs[0] = [left + int(0.4*width), top]
    servs[1] = [left + int(1.0*width), top]
    servs[2] = [left + int(1.8*width), top]
    servs[3] = [left + int(2.5*width), top]
    servs[4] = [left + int(3.2*width), top]
    servs[5] = [left + int(4.0*width), top]
    return servs


# 换人
def ChangeServant(S1, S2, S):
    masterskills = 'images/Master/MasterSkills.png'
    x = pyautogui.locateCenterOnScreen(masterskills, confidence=0.8)
    pyautogui.click(x); time.sleep(3)
    changeskill = 'images/Master/ChangeServant.png'
    x = pyautogui.locateCenterOnScreen(changeskill, confidence=0.8)
    pyautogui.click(x); time.sleep(3)

    # 确定换人界面从者位置
    servantchanges = ChangeServantLocations(S)

    # 换人
    pyautogui.click(servantchanges[S1-1]); time.sleep(3)
    pyautogui.click(servantchanges[S2-1]); time.sleep(3)

    # 确认更替
    changeconfirm = 'images/Master/ChangeConfirm.png'
    x = pyautogui.locateCenterOnScreen(changeconfirm, confidence=0.8)
    pyautogui.click(x); time.sleep(8)

    return
