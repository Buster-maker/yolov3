import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title('my window')
window.geometry('400x400')

def hit_me():
    #tk.messagebox.showinfo(title='Hi',message='hahahaha')
    #tk.messagebox.showwarning(title='Hi',message='nonono')
    #tk.messagebox.showerror(title='Hi',message='No!! never')
    #tk.messagebox.askquestion(title='Hi',message='hahahaha')  # return yes or no

    #tk.messagebox.askyesno(title='Hi',message='hahahaha')  # return True or Flase
    # tk.messagebox.askokcancel(title='Hi',message='hahahaha')
    tk.messagebox.askretrycancel(title='Hi',message='hahahaha')

tk.Button(window,text='hit me',command=hit_me).pack()
window.mainloop()