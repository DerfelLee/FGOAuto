import fgoauto
import matplotlib.pyplot as plt
import time

# Input your servants
Servants = ['Ishtar', 'C_Author', 'C_Author']


# Basic panels
Atk = 'images\Panel\Atk.png'
skills, S_img, S_np, S, C = fgoauto.BasicInf(Servants)

# Start
time.sleep(10)
print('Battle Start')

# 第一面
# 技能
fgoauto.Press(skills[0][0], S[0]); time.sleep(4)
fgoauto.Press(skills[1][0], S[1]); time.sleep(4)

fgoauto.Press(skills[1][1], S[1]); time.sleep(2)
fgoauto.Press(S_img[0]); time.sleep(3)
fgoauto.Press(skills[1][2], S[1]); time.sleep(2)
fgoauto.Press(S_img[0]); time.sleep(3)
fgoauto.Press(skills[2][2], S[2]); time.sleep(4)
fgoauto.Press(S_img[0]); time.sleep(3)
#选卡
fgoauto.Press(Atk); time.sleep(3)
fgoauto.Press(S_np[0]); time.sleep(3) # 宝具
fgoauto.PressRandomCards(C, 2)
time.sleep(30)

# 第二面
# 技能
fgoauto.Press(skills[2][0], S[2]); time.sleep(3)
fgoauto.Press(skills[2][1], S[2]); time.sleep(3)
fgoauto.Press(S_img[0]); time.sleep(3)
# 换人
fgoauto.ChangeServant(3, 4, S)
Servants = ['Ishtar', 'C_Author', 'Kongming']
print('Now the Servants are: '+str(Servants))
skills, S_img, S_np, S, C = fgoauto.BasicInf(Servants)
# 技能
fgoauto.Press(skills[2][2], S[2]); time.sleep(3)
#选卡
fgoauto.Press(Atk); time.sleep(3)
fgoauto.Press(S_np[0]); time.sleep(3) # 宝具
fgoauto.PressRandomCards(C, 2)
time.sleep(30)

# 第三面
# 技能
fgoauto.Press(skills[0][2], S[0]); time.sleep(4)
fgoauto.Press(skills[2][0], S[2]); time.sleep(3)
fgoauto.Press(S_img[0]); time.sleep(3)
# 选卡
fgoauto.Press(Atk); time.sleep(3)
fgoauto.Press(S_np[0]); time.sleep(3) # 宝具
fgoauto.PressRandomCards(C, 2)
time.sleep(30)