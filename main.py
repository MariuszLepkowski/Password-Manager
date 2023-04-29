from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_to_file():
    """Saves name of website, email/username and password to a txt file."""
    website = website_entry.get()
    email_username= email_username_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as file:
        file.write(f"{website} | {email_username} | {password}\n")

def clear_data():
    """Clears user's input from all the entries."""
    website_entry.delete(0, 'end')
    email_username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
def generate_password():
    print("generate password")


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
website_entry.focus()

email_username_entry = Entry(width=50)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)


# Buttons

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)


add_button = Button(text="Add", width=42, command=lambda: [save_data_to_file(), clear_data()])
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()