import tkinter as tk
import pickle
import tkinter.messagebox
class TKintermain():
    def __init__(self):
        self.window=tk.Tk()
        self.window.title('人脸识别')
        self.center_window=(self.window,800,600)
        self.canvas=tk.Canvas(self.window,width=600,height=400,bg='green')
        self.image_file=tk.PhotoImage(file='welcome.gif')
        self.image=self.canvas.create_image(100,0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')
        tk.Label(self.window,text='欢迎登陆',font=('Arial',16)).pack()
        tk.Label(self.window,text='用户名',font=('Arial',14)).place(x=150, y= 280)
        tk.Label(self.window,text='密   码',font=('Arial',14)).place(x=150, y= 320)

        self.var_usr_name=tk.StringVar()
        self.var_usr_name.set('1738312421@qq.com')
        self.entry_usr_name=tk.Entry(self.window,textvariable=self.var_usr_name,font=('Arial',14)).place(x=225,y=280)

        self.var_usr_pwd=tk.StringVar()
        self.entry_usr_pwd=tk.Entry(self.window,textvariable=self.var_usr_pwd,font=('Arial',14)).place(x=225,y=320)

        self.btn_login=tk.Button(self.window,text='登陆',command=self.usr_login).place(x=225,y=370)
        self.btn_sign_up=tk.Button(self.window,text='注册',command=self.usr_sign_up)
        self.btn_sign_up.place(x=325,y=370)
        self.window.mainloop()
    def center_window(self,root,width,height):
        # 将窗口固定在屏幕中间
        screenwidth=root.winfo_screenwidth()
        screenheight=root.winfo_screenheight()
        size='%dx%d+%d+%d'%(width,height,(screenwidth-width)/2,(screenheight-height)/2)
        return root.geometry(size)
    def usr_login(self):
        # 登录
        self.usr_name=self.var_usr_name.get()
        self.usr_pwd=self.var_usr_pwd.get()
        try:
            with open('usr_info.pickle','rb') as usr_file:
                usrs_info=pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle','wb') as usr_file:
                usrs_info={'admin':'admin'}
                pickle.dump(usrs_info,usr_file)
                usr_file.close()
        if self.usr_name in usrs_info:
            if self.usr_pwd==usrs_info[self.usr_name]:
                tkinter.messagebox.showinfo(title='welcome',message='欢迎登录'+self.usr_name+'!!!')
                self.window.deiconify()
                self.founctionSelection()
            else:
                tkinter.messagebox.showerror(message='密码错误，请重试')
        else:
            is_sign_up=tkinter.messagebox.askyesno('Welcome','找不到该用户，请先完成注册')
            if is_sign_up:
                self.usr_sign_up()
    def usr_sign_up(self):
        def sign_usr():
            np=new_pwd.get()
            npf=new_pwd_confirm.get()
            nn=new_name.get()
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
            if np!=npf:
                tk.messagebox.showerror('Error','Password and confirm password must be same')
            elif nn in exist_usr_info:
                tk.messagebox.showerror('Error','The user has already signed up')
            else:
                exist_usr_info[nn]=np
                with open('usr_info.pickle','wb') as usr_file:
                    pickle.dump(exist_usr_info,usr_file)
                tk.messagebox.showinfo('Welcome','you have successfully signed up!')
                window_sign_up.destory()
        window_sign_up = tk.Tk()
        self.center_window(window_sign_up,400,300)
        window_sign_up.title('Sign up window')
        new_name=tk.StringVar()
        tk.Label(window_sign_up,text='用户名：').place(x=10,y=10)
        entry_new_name=tk.Entry(window_sign_up,textvariable=new_name)
        entry_new_name.place(x=130,y=10)
        new_pwd=tk.StringVar()
        tk.Label(window_sign_up,text='密码：').place(x=10,y=10)
        entry_usr_pwd=tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
        entry_usr_pwd.place(x=30,y=50)
        new_pwd_confirm=tk.StringVar()
        tk.Label(window_sign_up,text='密码确认：').place(x=10,y=90)
        entry_usr_pwd_confirm=tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
        entry_usr_pwd_confirm.place(x=130,y=90)
        btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_usr)
        btn_comfirm_sign_up.place(x=180, y=120)



    def founctionSelection(self):
        pass

TKintermain()