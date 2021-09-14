from tkinter import Button,Tk,Text
from file import gen_image

root = Tk()
root.title("nft")
root.geometry("250x150")

inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
inputtxt.pack()
btn = Button(text="Generating", background="#555", foreground="#ccc",
             padx="20", pady="15", font="16", command=lambda:gen_image(int(inputtxt.get("1.0", "end-1c"))))
btn.pack()
root.mainloop()