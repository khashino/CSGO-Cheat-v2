# import modules
import threading
import webbrowser
from tkinter import *
import requests
import smt



# Designing window for registration

#exit_event = threading.Event()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    url = 'https://khashino.ir/khtest/info.php?username=' + username1 + '&password=' + password1
    response = requests.get(url)
    global status
    global isactive
    global isadmin

    if response.status_code != 200:
        user_not_found()

    print(response.json())

    status = response.json()["status"]

    if status != 0:
        isactive = response.json()["info"][0]["isactive"]
        isadmin = response.json()["info"][0]["isadmin"]

        if isactive == '1':
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    smt.updatevar()
    global login_success_screen
    global espbtn
    global wallbtn
    global radarbtn
    global moneybtn

    global espbtnst
    global wallbtnst
    global radarbtnst
    global moneybtnst
    color = '#67b85f'
    espbtnst = 0
    wallbtnst = 0
    radarbtnst = 0
    moneybtnst = 0

    login_screen.destroy()
    login_success_screen = Tk()
    login_success_screen.title("NoHack-Cheat")
    login_success_screen.geometry("300x350")
    login_success_screen['background'] = color


    Label(login_success_screen, text="Login Success, NoHack", height=4, bg=color).pack()
    radarbtn = Button(login_success_screen, bg="#748bb0", text="Radar", command=radar, height=2, width=25)
    radarbtn.pack()
    espbtn = Button(login_success_screen, bg="#748bb0", text="Wall(Glow-Esp)", command=esp, height=2, width=25)
    espbtn.pack()
    moneybtn = Button(login_success_screen, bg="#748bb0", text="Money", command=money, height=2, width=25)
    moneybtn.pack()
    wallbtn = Button(login_success_screen, bg="#748bb0", text="Wall(Simple)", command=wall, height=2, width=25)
    wallbtn.pack()
    Label(login_success_screen, text="", bg=color).pack()
    exitbtn = Button(login_success_screen, bg="#748bb0", text="Exit", command=delete_login_success, height=2, width=25)
    exitbtn.pack()

    whoami = Label(login_success_screen, text="CreatedBy: Khashino", fg="blue", cursor="hand2", bg=color)
    whoami.pack(side=BOTTOM)
    whoami.bind("<Button-1>", lambda e: callback("http://www.khashino.ir"))


def radar():
    global radarbtnst

    if radarbtnst == 0:
        print(radarbtnst)
        Radar = threading.Thread(None, smt.radar)
        Radar.start()
        radarbtn.configure(bg="#c3cc6e")
        radarbtnst = 1
    elif radarbtnst == 1:
        Radar = threading.Thread(None, smt.radar)
        Radar.start()
        radarbtn.configure(bg="#748bb0")
        radarbtnst = 0


def esp():
    global espbtnst

    if espbtnst == 0:
        #print(espbtnst)
        Esp = threading.Thread(None, smt.esp, daemon=True)
        Esp.start()
        espbtn.configure(bg="#c3cc6e")
        espbtn["state"] = "disabled"
        espbtnst = 1
    elif espbtnst == 1:
        #exit_event.set()
        #Esp
        espbtn.configure(bg="#748bb0")
        espbtnst = 0



def money():
    global moneybtnst

    if moneybtnst == 0:
        print(moneybtnst)
        Money = threading.Thread(None, smt.Money)
        Money.start()
        moneybtn.configure(bg="#c3cc6e")
        moneybtnst = 1
    elif moneybtnst == 1:
        Money = threading.Thread(None, smt.Money)
        Money.start()
        moneybtn.configure(bg="#748bb0")
        moneybtnst = 0



def wall():
    global wallbtnst

    if wallbtnst == 0:
        print(wallbtnst)
        Wall = threading.Thread(None, smt.wall)
        Wall.start()
        wallbtn.configure(bg="#c3cc6e")
        wallbtnst = 1
    elif wallbtnst == 1:
        Wall = threading.Thread(None, smt.wall)
        Wall.start()
        wallbtn.configure(bg="#748bb0")
        wallbtnst = 0



# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    exit()
    #login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window
def callback(url):
    webbrowser.open_new(url)

def main_account_screen():
    global login_screen
    color = '#67b85f'
    login_screen = Tk()
    login_screen.title("NoHack-Login")
    login_screen.geometry("300x350")
    login_screen['background'] = color
    canvas = Canvas(login_screen, width=300, height=90, bg=color, bd=0, highlightthickness=0, relief='ridge')
    canvas.pack()
    Label(login_screen, text="Please enter details below to login", bg=color).pack()
    Label(login_screen, text="", bg=color).pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    img = PhotoImage(file="Banner.png")
    canvas.create_image(0, 0, anchor=NW, image=img)
    Label(login_screen, text="Username * ", bg=color).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg=color).pack()
    Label(login_screen, text="Password * ", bg=color).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg=color).pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    whoami = Label(login_screen, text="CreatedBy: Khashino", fg="blue", cursor="hand2", bg=color)
    whoami.pack(side=BOTTOM)
    whoami.bind("<Button-1>", lambda e: callback("http://www.khashino.ir"))


    #login_sucess()
    login_screen.mainloop()


main_account_screen()
