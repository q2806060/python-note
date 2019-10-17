from tkinter import * 
 


tk = Tk()

def tony():
    print("abc")


#按钮，绑定事件
btn = Button(tk,command=tony,text="one button")
et = Entry(tk)
cv = Canvas(tk,bg="yellow")
cv.create_rectangle

#显示
btn.pack()
et.pack()
cv.pack()


tk.mainloop()



























