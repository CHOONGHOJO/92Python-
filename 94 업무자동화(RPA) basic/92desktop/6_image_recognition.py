import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#      print(i)
#      pyautogui.click(i, duration=0.5)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# print(checkbox)


# 속도 개선
# 1. Gray Scale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True) # 흑백으로 전환하여 비교, 정확도가 떨어질 수 있다
# pyautogui.moveTo(trash_icon)

# 2. 범위지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(x, y, width, height)) # 범위 지정(region)
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881-1488, 137)) # 빠른편
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepadqq = pyautogui.locateOnScreen("file_menu_notepadqq.png")
# if file_menu_notepadqq:
#      pyautogui.click(file_menu_notepadqq)
# else:
#      print("발견 실패")

# while file_menu_notepadqq is None:
#      file_menu_notepadqq = pyautogui.locateOnScreen("file_menu_notepadqq.png")
#      print("발견실패")

# pyautogui.click(file_menu_notepadqq)


# 2. 일정 시간 기다리기 (Timeout)
import time
import sys

timeout = 10  # 10 seconds
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#      file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepadqq.png")
#      end = time.time() # 종료 시간 설정
#      if end - start > timeout: # 지정한 시간 초과
#           print("시간 종료")
#           sys.exit()

# pyautogui.click(file_menu_notepad)

def  find_target(img_file, timeout=30):
     start = time.time()
     target = None
     while target is None:
          target = pyautogui.locateOnScreen(img_file)
          end = time.time()
          if end  - start > timeout:
               break
     return target

def  my_click(img_file, timeout=30):
     target = find_target(img_file, timeout)
     if target:
          pyautogui.click(target)
     else:
          print(f"[Timeot {timeout}s ] Target not found ({img_file}). Terminated program.")
          sys.exit()


my_click("file_menu_notepadqq.png", 5)
