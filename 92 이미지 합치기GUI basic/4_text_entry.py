from tkinter import *

root = Tk()
root.title("나도코딩 GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "(여러줄의)글자를 입력하세요!")

e = Entry(root, width=40) # 한 줄 입력
e.pack()
e.insert(0, "한 줄만 입력해요~!")

def btncmd():
  # 내용 출력
  print(txt.get("1.0", END)) #1.0 : 1 -> 첫번째 line, 0 -> 0번째 column 부터 END : 끝까지
  print(e.get())

  # 내용 삭제
  txt.delete("1.0", END)
  e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
