import tkinter as tk
import tkinter.filedialog as fdialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_menu()
        #self.NewFile()

    def create_menu(self):
        self.open_file = tk.Button(self)
        self.open_file["text"] = "Open"
        self.open_file["command"] = self.OpenFile
        self.open_file.pack(side="top")

        self.quit = tk.Button(self, text="Exit", fg="red", command=root.destroy)
        self.quit.pack(side="top")

    def OpenFile(self):
        inputFile = fdialog.askopenfile()
        with open(inputFile.name, 'r+') as f:
            data = f.read()
            text.insert(0.0,data)

    def SaveFile(self):
        pass


root = tk.Tk()
app = Application(master=root)
app.master.title("Text Editor")
app.master.geometry("500x500")
text = tk.Text(root, width=500, height=500)
text.pack()
app.mainloop()
