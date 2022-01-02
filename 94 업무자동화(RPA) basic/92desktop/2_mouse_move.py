import pyautogui

# 절대 좌표로 마우스 이동
# pyautogui.moveTo(960, 540) # 지정한 위치(가로:y, 세로:x)로 마우를 이동
pyautogui.moveTo(960, 540, duration=0.5) # 지정한 위치(가로:x, 세로:y)로 0.5동안 마우를 이동

# 상대 좌표로 마우스 이동
# pyautogui.move(110, 110, duration=0.5) #
# print(pyautogui.position()) # Point(x,y)
# pyautogui.move(100, 200, duration=0.5) # 110,510 기준으로  +100, +200 => 310, 710
# print(pyautogui.position()) # Point(x,y)
# pyautogui.move(200, 200, duration=0.5) # 310,710 기쥰으로  +300, +400 => 610, 1110
# print(pyautogui.position()) # Point(x,y)


p = pyautogui.position()
print(p[0], p[1]) # x, y)
print(p.x, p.y) # x, y)
