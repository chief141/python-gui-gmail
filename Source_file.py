import smtplib
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font
from tkinter import messagebox
from os import path 
import json
import imghdr

###### DATA   #########
sender_email = ""
password = ""
reciever_mail = ""
dir_ = path.join(path.dirname(__file__),"Data")
file = path.join(dir_,"data.json")
##############################


####### FUNCTIONS   ###########
def send():
	global sender_email, password, reciever_mail 
	sender_email = gmail_entry.get()
	password = pass_entry.get()
	reciever_mail = recv_gmail_entry.get()
	subject = subject_entry.get('1.0',END)
	body = body_entry.get('1.0',END)

	#CHECKING FOR INFO
	if len(sender_email)<=0 or len(reciever_mail) <= 0 or len(password) <= 0:
		messagebox.showerror(title="Error",message="Please fill important fields")
	else:
		sure_send = messagebox.askquestion("Send","Are you sure you want to send gmail?")
		if sure_send=="yes":
			send_btn['state'] = DISABLED
			save_btn['state'] = DISABLED
			clear_btn['state'] = DISABLED
			gmail_entry['state'] = DISABLED
			pass_entry['state'] = DISABLED
			recv_gmail_entry['state'] = DISABLED
			subject_entry['state'] = DISABLED
			body_entry['state'] = DISABLED


			try:
				with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				#with smtplib.SMTP('localhost',1025) as smtp:  ## FOR TESTING ON LOCAL SERVICE
					smtp.ehlo()
					smtp.starttls() ## Comment out this when testing
					smtp.ehlo()
					smtp.login(sender_email,password)  ## Comment out this when testing
					msg = f"Subject: {subject}\n\n{body}"
					smtp.sendmail(sender_email, reciever_mail , msg)
					messagebox.showinfo(title="Success",message="Your mail was sent successfully!")
			
			except:
				messagebox.showerror(title="Error",message="There was an error in connecting to server.")

			send_btn['state'] = NORMAL
			save_btn['state'] = NORMAL
			clear_btn['state'] = NORMAL
			gmail_entry['state'] = NORMAL
			pass_entry['state'] = NORMAL
			recv_gmail_entry['state'] = NORMAL
			subject_entry['state'] = NORMAL
			body_entry['state'] = NORMAL



password_hid = True
def show_pass():
	global password_hid
	messagebox.showinfo(title="Success",message="Your mail was sent successfully!")
	if password_hid:
		show_pass_btn['image'] = show_pass_btn_icon2
		pass_entry.config(show="")
		password_hid = False
	else:
		show_pass_btn['image'] = show_pass_btn_icon
		pass_entry.config(show="*")
		password_hid = True

def clear():
	clear_prompt = messagebox.askquestion ('Clear all','Are you sure you want to clear all fields?',icon = 'warning')


	if clear_prompt=="yes":
		gmail_entry.delete(0,END)
		pass_entry.delete(0,END)
		recv_gmail_entry.delete(0,END)
		subject_entry.delete('1.0',END)
		body_entry.delete('1.0',END)

def save():
	global  file
	should_overwrite = messagebox.askquestion("Save?", "Are you sure you want to overwrite previous save?")
	if should_overwrite=="yes":
		sender_email = gmail_entry.get()
		reciever_mail = recv_gmail_entry.get()
		subject = subject_entry.get('1.0',END)
		body = body_entry.get('1.0',END)
		with open(file,'w') as f:
			to_be_written_data = {"S_MAIL":sender_email,"R_MAIL":reciever_mail,"SUB":subject,"BODY":body}
			json.dump(to_be_written_data,f)

#functiosn of changeing color of buttons on hover
def on_enter_clear_btn(e):
	clear_btn['bg'] = "#F2F2F2"

def on_leave_clear_btn(e):
	clear_btn['bg'] = "#E0E0E0"


def on_enter_send_btn(e):
	send_btn['bg'] = "#F2F2F2"
def on_leave_send_btn(e):
	send_btn['bg'] = "#E0E0E0"


def on_enter_show_pass_btn(e):
	show_pass_btn['bg'] = "#F2F2F2"
def on_leave_show_pass_btn(e):
	show_pass_btn['bg'] = "#E0E0E0"


def on_enter_save_btn(e):
	save_btn['bg'] = "#F2F2F2"
def on_leave_save_btn(e):
	save_btn['bg'] = "#E0E0E0"


##########  ROOT #############
root = Tk()
root.geometry("1000x650")
root.title("fast Mail")
root.config(bg="#E0E0E0")
main_icon = path.join(dir_,"main_icon.ico")
root.iconbitmap(main_icon)

#####   Gmail #####################
gmail_label = Label(root,text="Your Gmail Address* : ",font=("Roboto 10"),bg="#E0E0E0",fg="black")
gmail_label.place(x=15+10,y=30)

gmail_entry = Entry(root,width=50,borderwidth=0,font="Courier 11")
gmail_entry.place(x=17+10,y=50,height=20)
###################################

####### Password #######
pass_label = Label(root,text="Your Password* : ",font=("Roboto 10"),bg="#E0E0E0",fg="black")
pass_label.place(x=15+10,y=90)

pass_entry = Entry(root,width=50,borderwidth=0,font="Courier 11")
pass_entry.place(x=17+10,y=110,height=20)
pass_entry.config(show="*")

show_pass_img1 = path.join(dir_,"show_pass.png")
show_pass_btn_icon = PhotoImage(file=show_pass_img1)
show_pass_img2 = path.join(dir_,"show_pass2.png")
show_pass_btn_icon2 = PhotoImage(file=show_pass_img2)
show_pass_btn = Button(root,image=show_pass_btn_icon,width=18,height=18,command=show_pass,relief=GROOVE)
show_pass_btn.bind("<Enter>",on_enter_show_pass_btn)
show_pass_btn.bind("<Leave>",on_leave_show_pass_btn)
show_pass_btn.place(x=473+10,y=108)
############################


##### revier EMAIL   ###########
recv_gmail_label = Label(root,text="Reciever Gmail Address* : ",font=("Roboto 10"),bg="#E0E0E0",fg="black")
recv_gmail_label.place(x=15+10,y=148)

recv_gmail_entry = Entry(root,width=50,borderwidth=0,font="Courier 11")
recv_gmail_entry.place(x=17+10,y=168,height=20)
#########################



##################  COMPOSE MAIL    #######################
####### SUBJECT ENTRY   ###########
subject_label = Label(root,text="Subject : ",font=("Roboto 10"),bg="#E0E0E0",fg="black")
subject_label.place(x=25,y=240)

subject_entry = ScrolledText(root,width=62,borderwidth=0)
subject_entry.place(x=27,y= 260,height=50)
########################################

####### MAIL BODY ENTRY  ###########
body_label = Label(root,text="Compose : ",font=("Roboto 10"),bg="#E0E0E0",fg="black")
body_label.place(x=25,y=330)

#body_entry = Text(root, bg="white",height=50,width=60)
body_entry = ScrolledText(root,width=110,borderwidth=0)
body_entry.place(x=27,y=350,height=180)
######################################
########################################


#########       BUTTTONS        ###########
font_ = Font(size=10,family="Courier")

send_btn = Button(root,text="Send",font=font_,padx=23,pady=2,command=send,relief=GROOVE)
send_btn.place(x=30,y=565)
send_btn.bind("<Enter>",on_enter_send_btn)
send_btn.bind("<Leave>",on_leave_send_btn)

save_btn = Button(root,text="Save as draft",font=font_,padx=20,pady=2,command=save,relief=GROOVE)
save_btn.place(x=165,y=565)
save_btn.bind("<Enter>",on_enter_save_btn)
save_btn.bind("<Leave>",on_leave_save_btn)

clear_btn = Button(root,text="Clear all",font=font_,padx=23,pady=2,command=clear,relief=GROOVE)
clear_btn.place(x=368,y=565)
clear_btn.bind("<Enter>",on_enter_clear_btn)
clear_btn.bind("<Leave>",on_leave_clear_btn)
#########   ##########  


###### LOADING SAVEd data ########
with open(file,'r') as f:
	opened_data = json.loads(f.read())
	gmail_entry.insert(0,opened_data["S_MAIL"])
	recv_gmail_entry.insert(0,opened_data["R_MAIL"])
	subject_entry.insert('1.0',opened_data["SUB"])
	body_entry.insert('1.0',opened_data["BODY"])


root.mainloop()