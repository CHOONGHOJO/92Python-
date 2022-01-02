import pyautogui
# w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 뛰운 산태에서 가져옴

# w.activate()

# pyautogui.write("12345", interval=0.25)

# pyautogui.write(["t", 'e', 's', 't','left','left','right','l','a','enter'], interval=0.25)
# # t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 한 번, l a 순서개로 적고, enter 입력

# 특수문자
# shift 4 -> $
# pyautogui.keyDown('shift') # shift key를 누른 상태에서
# pyautogui.press('4') # 숫자 4를 입력하고
# pyautogui.keyUp('shift') # shift key를 땐다

# 조합key (Hot key)
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('a')
# pyautogui.keyUp('a') # press('a)
# pyautogui.keyUp('ctrl') # Ctrl + A

# 간편한 조합키
# pyautogui.hokey('ctrl', 'alt', 'shift', 'a')
# Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 떼고
# pyautogui.hotkey('ctrl', 'a')

# 한글입력
# pip3 install pyperclip
import pyperclip
# pyperclip.copy('나도코딩') # 글자를 클립보드에 저장
# pyautogui.hotkey('ctrl', 'v') # clipborad에 있는 내용 붙이기

def my_write(etxt):
    pyperclip.copy('나도코딩')
    pyautogui.hotkey('ctrl', 'v')

my_write("나도코딩")

# 자동화 program 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q








