import pyautogui
# 화면 스트린샷 찍기

# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 28, 18 34, 167, 242 #22A7F2

pixel = pyautogui.pixel(28, 18)
print(pixel)

print(pyautogui.pixelMatchesColor(28, 18, (34,167,242)))
print(pyautogui.pixelMatchesColor(28, 18, pixel))
