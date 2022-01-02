import pyautogui

# fw = pyautogui.getActivewindow() # 현재 활성화된 창 (VSCode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 width, height
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20)

# 모든 window
# for w in pyautogui.getAllWindows():
#      print(w) # 모든 윈도우 가져오기

# 어떤 제목을 가지는 window
# for w in pyautogui.getWindowWithTitle("제목없음"):
#      print(w)

# for w in pyautogui.getWindowWithTitle("제목없음"):
#      print(w)

w = pyautogui.getWindowWithTitle("제목없음")[0]
print(w)

if w.isActive == False: # 활성화 안된 상태
     w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False: # 최대화 안된 상태
     w.maximize() # 최대화

if w.isMinimize == False: # 최소화 안된 상태
     w.minimize() # 최소화

pyautogui.sleep(1)
w.restore() # 화면 원상태로 복귀
w.close() # window 닫기
