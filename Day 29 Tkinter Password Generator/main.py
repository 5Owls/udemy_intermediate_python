from tkinter import *
from tkinter import messagebox
import random
import json

FONT = ("Cambria", 12, "normal")


# ---------------------------- SEARCH DATA---------------- ------------------------------- #
def search_data():
    try:
        with open("data.json") as file:
            search_data_dict = json.load(file)
            website = ent_website.get()
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="File not found!!")
    else:
        if website not in search_data_dict:
            messagebox.showinfo(title="Error Website not found", message="Website not found. Create its information.")
        else:
            messagebox.showinfo(title=f"{website} Details",
                                message=f"Email: {search_data_dict[website]['email']} \nPassword: "
                                        f"{search_data_dict[website]['password']}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''# NOT A VERY SECURE METHOD TO GENERATE a PASSWORD: list_password = []
    # password = ''
    # letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    #            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    #            'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
    #            '#', '$', '%', '+', '&', '*', '(', ')']
    # for i in range(0, 10):
    #     list_password.append(random.choice(letters)) '''

    list_password = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '+', '&', '*', '(', ')']

    random_number_letters = random.randint(4, 7)
    random_number_numbers = random.randint(2, 5)
    random_symbols = random.randint(1, 3)

    list_random_letters = [random.choice(letters) for i in range(0, random_number_letters)]
    list_random_numbers = [random.choice(numbers) for i in range(0, random_number_numbers)]
    list_random_symbols = [random.choice(symbols) for i in range(0, random_symbols)]

    list_password = list_random_letters + list_random_symbols + list_random_numbers
    password = ''.join(list_password)
    random.shuffle(list_password)
    ent_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    # get data
    website = ent_website.get()
    email = ent_email.get() # its already pre-populated but the user can change it.
    password = ent_password.get()

    dict_data = {website:
        {
            'email': email,
            'password': password
        }
    }

    # verification that no entries are empty
    if website == "" or password == "":
        empty_notification = messagebox.showerror(title="Empty entries", message="You can not save empty entries!")
    else:  # save data
        is_input_okay = messagebox.askokcancel(title="verify details",
                                         message=f"Is the following details correct? Website: {website} \nPassword: {password}.")
        if is_input_okay:
            try:
                with open("data.json", "r") as data_file:
                    # read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(dict_data, file, indent=4)
            else:
                # update data
                data.update(dict_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                # clear data from widgets/ except email entry because we want it populated with data
                ent_website.delete(0, 'end')
                ent_password.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.minsize(width=300, height=300)
window.title("Password Generator")

canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(column=1, row=0)

# Labels
lbl_website = Label(text="Website", font=FONT)
lbl_website.grid(column=0, row=1)

lbl_email = Label(text="Email/Username", font=FONT)
lbl_email.grid(column=0, row=2)

lbl_password = Label(text="Password", font=FONT)
lbl_password.grid(column=0, row=3)

# Entry
ent_website = Entry(width=21)
ent_website.focus()
ent_website.grid(column=1, row=1, columnspan=1)

ent_email = Entry(width=35)
ent_email.insert(0, "lilymyburgh@gmail.com")
ent_email.grid(column=1, row=2, columnspan=2)

ent_password = Entry(width=21)
ent_password.grid(column=1, row=3)

# Button
btn_generate_password = Button(text="Generate Password", font=FONT, command=generate_password)
btn_generate_password.grid(column=2, row=3)

btn_search = Button(text="Search", width=15, font=FONT, command=search_data)
btn_search.grid(column=2, row=1)

btn_add = Button(text="Add", width=36, font=FONT, command=save_data)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
