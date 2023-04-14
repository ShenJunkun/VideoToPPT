import tkinter as tk

from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import *

def select_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    # 在entry中显示文件路径
    file_path_entry.delete(0, END)
    file_path_entry.insert(0, filename)

if __name__ == "__main__":
    win = tk.Tk()
    win.title("Video To Powerpoint")

    width = 400
    height = 400
    screenwidth = win.winfo_screenwidth()  
    screenheight = win.winfo_screenheight()
    print(screenwidth, screenheight) 
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)   
    print(alignstr)
    win.geometry(alignstr)
    win.resizable(0,0)

    instruction = tk.Label(text='输入视频网址: ', font=('楷体', 12))
    instruction.pack(padx=20, pady=10, anchor=tk.W)

    input_url = tk.Entry()
    input_url.pack(ipadx=120, ipady=6, padx=20, anchor=tk.W)
    
    frame = tk.Frame(win)
    frame.pack(side=tk.TOP)
    button_spacing =20

    button1 = tk.Button(frame, text="一键生成", font=('楷体',12))
    button1.pack(side=tk.LEFT, padx=button_spacing, pady=10,)

    button2 = tk.Button(frame, text="下载视频", font=('楷体',12))
    button2.pack(side=tk.LEFT, padx=button_spacing, pady=10)


    frame_local_generate = tk.Frame(win)
    frame_local_generate.pack(side=tk.TOP)

    spacing = 10
    # 创建entry用于显示文件路径
    file_path_entry = Entry(frame_local_generate)
    file_path_entry.pack(side=tk.LEFT, padx=spacing, ipady=6 ,pady=10)

    select_button = Button(frame_local_generate, text="选择文件", font=('楷体', 12), command=select_file)
    select_button.pack(side=tk.LEFT, padx=spacing, pady=10)

    button3 = tk.Button(frame_local_generate, text="本地生成", font=('楷体', 12))
    button3.pack(side=tk.LEFT, padx=spacing, pady=10)

    stext = ScrolledText(width=60, height=18, background='#F7F3EC')
    stext.pack(padx=20)

    win.mainloop()
