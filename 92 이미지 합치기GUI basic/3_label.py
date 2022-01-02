from tkinter import *

root = Tk()
root.title("나도코딩 GUI")
root.geometry("640x480") # 가로 * 세로

label1 = Label(root, text="안녕하세요?")
label1.pack()

photo = PhotoImage(file="/home/cjoe731/Desktop/python(NadoCoding)/무료 강의 (활용편2:이미지 합치기GUI)basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
  label1.config(text="반갑습니다!")

  global photo2
  photo2 = PhotoImage(file="/home/cjoe731/Desktop/python(NadoCoding)/무료 강의 (활용편2:이미지 합치기GUI)basic/img2.png")
  label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()
