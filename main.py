from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def give_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    final_password = password_symbol + password_number + password_letter
    shuffle(final_password)
    password = "".join(final_password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pass_entered = password_entry.get()
    website_entered = website_entry.get()
    mail_entered = Email_entry.get()
    new_data = {website_entered:
                    {"Email":mail_entered,
                     "Password":pass_entered
                    }
               }
    if len(pass_entered)==0 or len(website_entered)==0:
        messagebox.showinfo(title="NO ALLOWED",message="Dont leave any field Empty")
    else:
        try:
            with open("data.json","r") as d_file:
                data = json.load(d_file) #read old data
        except FileNotFoundError:
            with open("data.json", "w") as d_file:
                json.dump(new_data, d_file, indent=4)
        else:
            data.update(new_data) #update the old data with new
            with open("data.json", "w") as d_file:
                json.dump(data, d_file, indent=4)  # Save the updated data
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END) #removes the data after add is clicked
# ---------------------------FIND PASSWORD------------------------------------#

def find():
    web_entered = website_entry.get()
    try:
        with open("data.json","r") as file_search:
            base = json.load(file_search)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="File not found")
    else:
        if web_entered in base:
            email = base[web_entered]["Email"]
            pass_ = base[web_entered]["Password"]
            messagebox.showinfo(title=web_entered, message=f"Email:{email}\nPassword:{pass_}")
        else:
            messagebox.showinfo(title="Error", message=f"No Data for {web_entered} found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20,pady=30)

canvas = Canvas(width=200, height=200)
try:
    img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=img)
except Exception:
    canvas.create_text(
        100, 100, text="🔐 PASS MANAGER", font=("Arial", 14, "bold")
    )
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)
Username_label = Label(text="Email/Username: ")
Username_label.grid(row=2,column=0)
Password_label = Label(text="Password: ")
Password_label.grid(row=3,column=0)

# Entries
password_entry = Entry(width=16)
password_entry.grid(row=3,column=1)
website_entry = Entry(width=16)
website_entry.grid(row=1,column=1)
website_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(row=2,column=1,columnspan=2)
Email_entry.insert(0,"youremail@test.com") # this will be used by default unless changed.

# Buttons
Generate_button = Button(text="Generate Password",command=give_pass)
Generate_button.grid(row=3,column=2)
Add_button = Button(text="Add",width=29,command=save)
Add_button.grid(row=4,column=1,columnspan=2)
Search_button = Button(text="Search",command=find,width=15)
Search_button.grid(row=1,column=2)
window.mainloop()