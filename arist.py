from tkinter.filedialog import *
import tkinter as tk


canvas = tk.Tk()
canvas.iconbitmap('xyz.ico')
canvas.geometry("400x600")
canvas.title("Aristotle")
canvas.config(bg = "White")
top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('C++ file', '.cpp'), ('Python file', '.py'), ('C# file', 'cs'), ('Javascript file', '.js')])
    if new_file is None:
        return
    text = str(entry.get(1.0, tk.END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(tk.INSERT, content)

def clearFile():
    entry.delete(1.0, tk.END)


b1 = tk.Button(canvas, text="Open", bg = "White", command = openFile)
b1.pack(in_ = top, side=tk.LEFT, )

b2 = tk.Button(canvas, text="Save", bg = "White", command = saveFile)
b2.pack(in_ = top, side=tk.LEFT, )

b3 = tk.Button(canvas, text="Clear", bg = "White", command = clearFile)
b3.pack(in_ = top, side=tk.LEFT, )

entry = tk.Text(canvas, wrap = tk.WORD, bg = "#006666", fg = "White", font = ("Agency FB", 21))
entry.pack(padx = 10, pady = 5, expand = True, fill = tk.BOTH)

canvas.mainloop()
