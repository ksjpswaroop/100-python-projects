import tkinter as tk
import tkinter.filedialog as fdialog

def OpenFile():
    global filename
    text.delete(0.0, tk.END)
    inputFile = fdialog.askopenfile()
    filename = inputFile.name
    with open(filename, 'r+') as f:
        data = f.read()
        text.insert(0.0,data)

def SaveFile():
    global filename
    savedText = text.get(0.0, tk.END)
    with open(filename, 'w') as f:
        data = f.write(savedText)

def SaveAs():
    global filename
    filename = fdialog.asksaveasfile().name
    savedText = text.get(0.0, tk.END)
    with open(filename, 'w') as f:
        data = f.write(savedText)


root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

text = tk.Text(root, width=800, height=600)
text.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
menubar.add_command(label="Open", command=OpenFile)
menubar.add_command(label="Save", command=SaveFile)
menubar.add_command(label="Save as", command=SaveAs)
menubar.add_command(label="Exit", command=root.destroy)
root.config(menu=menubar)

root.mainloop()
