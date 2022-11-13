import fgoauto
import pyautogui
import matplotlib.pyplot as plt
import cv2
import time

# Input your servants
Servants = ['Ishtar', 'C_Author', 'C_Author']


# Basic panels
# Atk = 'images\Panel\Atk.png'
# skills = [[0]*3 for i in range(3)]
# S_img = [[0] for i in range(3)]
# S_np = [[0] for i in range(3)]

# for i in range(3):
#     for j in range(3):
#         skills[i][j] = 'images/Servants/'+Servants[i]+'/Skill'+str(j+1)+'.png'

# for i in range(3):
#     S_img[i] = 'images/Servants/'+Servants[i]+'/Battle.png'
#     S_np[i] = 'images/Servants/'+Servants[i]+'/NP.png'

time.sleep(10)
print('Battle Start')

# S = fgoauto.FindServant(Servants[0])
# C = fgoauto.FindCards(S)
# testregion1 = pyautogui.screenshot(region=S[0])
# testregion2 = pyautogui.screenshot(region=S[1])
# testregion3 = pyautogui.screenshot(region=S[2])
# plt.imshow(testregion1)
# plt.show()
# plt.imshow(testregion2)
# plt.show()
# plt.imshow(testregion3)
# plt.show()


# fgoauto.Press(skills[0][0], S[0]); time.sleep(3)
# fgoauto.Press(skills[1][0], S[1]); time.sleep(3)

# fgoauto.Press(skills[1][1], S[1]); time.sleep(3)
# fgoauto.Press(S_img[0]); time.sleep(3)
# fgoauto.Press(skills[1][2], S[1]); time.sleep(3)
# fgoauto.Press(S_img[0]); time.sleep(3)
# fgoauto.Press(skills[2][2], S[2]); time.sleep(3)
# fgoauto.Press(S_img[0]); time.sleep(3)
# fgoauto.Press(Atk); time.sleep(3)

# fgoauto.Press(S_np[0])

# fgoauto.ChangeServant(3, 4, S)

fgoauto.ChooseAssistant('C_Author')




print('End')