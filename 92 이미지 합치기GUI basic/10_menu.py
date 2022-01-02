from tkinter import *

root = Tk()
root.title("나도코딩 GUI")
root.geometry("640x480") # 가로 * 세로

def create_new_file():
  print("새 파일을 만듭니다.")

s_menu = Menu(root)

# File Menu
menu_file = Menu(s_menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")

menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_command(label="Exit", command=root.quit)
s_menu.add_cascade(label="File", menu=menu_file)

# Edit menu (빈 값)
s_menu.add_cascade(label="Edit")

# Language 매뉴 추가 (radio button을 통해서 택1)
menu_lang = Menu(s_menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
s_menu.add_cascade(label="Language", menu=menu_lang)

# View menu
menu_view = Menu(s_menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
s_menu.add_cascade(label="View", menu=menu_view)

root.config(menu=s_menu)



root.mainloop()
