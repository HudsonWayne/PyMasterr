from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, root):
        master.title("Calculator")
        master.geomtry('357x420+0+0')
        master.config(bg='grey')
        master.resizable(False,False)
        
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17,bg= '#fff',font=('Arial Bold'), textvariable= self.equation.place(x=0,y=0))
        
    def show(self, value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
        
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
        
    def solve(self):
        result = eval(self.entry_value)
        

root=Tk()
root.mainloop()