
from tkinter import *
from tkinter import messagebox
import ast


parent = Tk()
parent.title('Login')
parent.geometry('1025x500+500+200')
parent.configure(bg="#f5f5f5")
parent.resizable(False, False)


def signin():
    username = user.get()
    passwords = password.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and passwords == r[username]:
        screen = Toplevel(parent)
        screen.title('App')
        screen.geometry('1025x500+500+200')
        screen.configure(bg="#f5f5f5")
        Label(screen, text="Hello User", bg='white', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'Invalid username or password')


def signup_command():
    window = Toplevel(parent)
    window.title('Sign-Up')
    window.geometry('1025x500+500+200')
    window.configure(bg="#f5f5f5")
    window.resizable(False, False)

    
    def signup():
        username= user.get()
        passwords= password.get()
        conpasswords = conpassword.get()
        if passwords==conpasswords:
            try:
                file = open('datasheet.txt', 'r+')
                d= file.read()
                r=ast.literal_eval(d)

                dict2 = {username:passwords}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w= file.write(str(r))
                messagebox.showinfo('SignUp', 'Successfully signed up')
            except:
                file = open('datasheet.txt', 'w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', 'Both Password and Confirm Password should match')     

    def sign():
       window.destroy()

    img = PhotoImage(file='login.png')
    Label(window,image=img, bg='white').place(x=50,y=80)

    frame = Frame(window, width="350", height="390", bg="white")
    frame.place(x=480,y=50)

    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame,width="25",fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        name=password.get()
        if name == '':
            password.insert(0, 'Password')

    password = Entry(frame,width="25",fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    password.place(x=30,y=150)
    password.insert(0,'Password')
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    def on_enter(e):
        conpassword.delete(0, 'end')

    def on_leave(e):
        name=conpassword.get()
        if name == '':
            conpassword.insert(0, 'Confirm Password')

    conpassword = Entry(frame,width="25",fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    conpassword.place(x=30,y=220)
    conpassword.insert(0,'Confirm Password')
    conpassword.bind('<FocusIn>', on_enter)
    conpassword.bind('<FocusOut>', on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    Button(frame,width=39,pady=7, text="Sign Up",bg='#8612f4',fg='white',border=0, command=signup).place(x=35,y=280)
    label = Label(frame, text="I have an account",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    sign_in= Button(frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=sign)
    sign_in.place(x=200,y=340)

    window.mainloop()


img = PhotoImage(file='login.png')
Label(parent, image=img, bg='white').place(x=50, y=80)

frame = Frame(parent, width="350", height="350", bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width="25", fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


def on_enter(e):
    password.delete(0, 'end')


def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')


password = Entry(frame, width="25", fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign In", bg='#8612f4',fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=215, y=270)


parent.mainloop()
