from tkinter import *

root = Tk()
root.title("나도코딩 GUI")
root.geometry("640x480") # 가로 * 세로

chkvar = IntVar() # chkvar에 int형으로 값을 지정
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable= chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리

chkbox.pack()

chkvar2 = IntVar() # chkvar에 int형으로 값을 지정
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable= chkvar2)
chkbox2.pack()

def btncmd():
 print(chkvar.get()) # 0:체크 해제, 1: 체크 등록
 print(chkvar2.get()) # 0:체크 해제, 1: 체크 등록

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
