# Create login GUI page with email as user login and password to authenticate

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
	email = email_input.get()
	passwd = pass_input.get()
	
	if email == 'test@gmail.com' and passwd =='1234':
		messagebox.showinfo('Yayyy','Login successful')
	else:
		messagebox.showerror('Error','Login failed')

root = Tk()
root.title('Login form')
root.iconbitmap(r"C:\Users\Admin\OneDrive\Desktop\40-fe.ico")

# root.minsize(400,400)
# root.maxsize(600,600)
root.geometry('350x500')
root.configure(background='#0096DC')

img = Image.open(r"C:\Users\Admin\OneDrive\Desktop\40-fe.png")
resized_img = img.resize((100,100),Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

text_label = Label(root,text ='Fe cart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

# login form 
email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=40)
email_input.pack(ipady=4,pady=(1,15))

pass_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
pass_label.pack(pady=(20,5))
pass_label.config(font=('verdana',12))

pass_input = Entry(root,width=40)
pass_input.pack(ipady=4,pady=(1,15))

login_btn = Button(root,text='Login',bg='white',fg='black',width=20,height=2, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',12))

root.mainloop()