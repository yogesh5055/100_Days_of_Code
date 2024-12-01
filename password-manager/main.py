from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_content={website:{
         "email":email,
         "password":password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
                with open("data.json","w") as data_file:
                     json.dump(new_content,data_file,indent=4)
        else:
                data.update(new_content)
                with open("data.json","w") as data_file:
                        json.dump(data,data_file,indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
#----------------------------FIND PASSWORD ----------------------------#
def find_password():
      website=website_entry.get()
      try:
        with open("data.json") as data_file:
                data=json.load(data_file)
                
      except FileNotFoundError:
            messagebox.showinfo(title="Error",message="File Not  Found")
      else:
            if website in data:
                    email=data[website]["email"]
                    password=data[website]["password"]
                    messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                   messagebox.showinfo(title="Error",message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(width=200,height=200)
logo_png=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_png)
canvas.grid(row=0,column=1)

website_labl=Label(text="Website:")
website_labl.grid(row=1,column=0)
email_labl=Label(text="Emain/Username:")
email_labl.grid(row=2,column=0)
password_labl=Label(text="Password:")
password_labl.grid(row=3,column=0)


website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=36)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"xyz@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)


search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)
generate_pass = Button(text="Generate Password",width=13,command=generate_password)
generate_pass.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()