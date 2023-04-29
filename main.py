from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
def generate_password():
    print("generate password")
def add():
    print("add password")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(width=50)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)


# Buttons

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)


add_button = Button(text="Add", width=42, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()