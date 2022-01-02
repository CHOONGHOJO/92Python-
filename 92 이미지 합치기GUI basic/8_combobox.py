import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("나도코딩 GUI")
root.geometry("640x480") # 가로 * 세로

values = [str(i) + "일" for i in range(1, 32)] # 1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 설정, 버튼 클릭을 통한 값 살정도 가능

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 읽기 전용
readonly_combobox.current(0) # 0번째 index값 선택
readonly_combobox.pack()

def btncmd():
 print(combobox.get()) # 선택된 값 표시
 print(readonly_combobox.get()) # 선택된 값 표시

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
