# import modules
import threading
from tkinter import *
import requests
import os
import smt
import sys


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

    espbtnst = 0
    wallbtnst = 0
    radarbtnst = 0
    moneybtnst = 0

    login_screen.destroy()
    login_success_screen = Tk()
    login_success_screen.title("Nohack")
    login_success_screen.geometry("300x350")
    Label(login_success_screen, text="Login Success", height=4).pack()

    radarbtn = Button(login_success_screen, bg="gray", text="Radar", command=radar, height=3)
    radarbtn.pack(fill=X)
    espbtn = Button(login_success_screen, bg="gray", text="Esp", command=esp, height=3)
    espbtn.pack(fill=X)
    moneybtn = Button(login_success_screen, bg="gray", text="Money", command=money, height=3)
    moneybtn.pack(fill=X)
    wallbtn = Button(login_success_screen, bg="gray", text="Wall", command=wall, height=3)
    wallbtn.pack(fill=X)
    exitbtn = Button(login_success_screen, bg="gray", text="Exit", command=delete_login_success, height=3)
    exitbtn.pack(fill=X)


def radar():
    global radarbtnst

    if radarbtnst == 0:
        print(radarbtnst)
        Radar = threading.Thread(None, smt.radar)
        Radar.start()
        radarbtn.configure(bg="green")
        radarbtnst = 1
    elif radarbtnst == 1:
        Radar = threading.Thread(None, smt.radar)
        Radar.start()
        radarbtn.configure(bg="gray")
        radarbtnst = 0


def esp():
    global espbtnst

    if espbtnst == 0:
        #print(espbtnst)
        Esp = threading.Thread(None, smt.esp, daemon=True)
        Esp.start()
        espbtn.configure(bg="green")
        espbtn["state"] = "disabled"
        espbtnst = 1
    elif espbtnst == 1:
        #exit_event.set()
        #Esp
        espbtn.configure(bg="gray")
        espbtnst = 0



def money():
    global moneybtnst

    if moneybtnst == 0:
        print(moneybtnst)
        Money = threading.Thread(None, smt.Money)
        Money.start()
        moneybtn.configure(bg="green")
        moneybtnst = 1
    elif moneybtnst == 1:
        Money = threading.Thread(None, smt.Money)
        Money.start()
        moneybtn.configure(bg="gray")
        moneybtnst = 0



def wall():
    global wallbtnst

    if wallbtnst == 0:
        print(wallbtnst)
        Wall = threading.Thread(None, smt.wall)
        Wall.start()
        wallbtn.configure(bg="green")
        wallbtnst = 1
    elif wallbtnst == 1:
        Wall = threading.Thread(None, smt.wall)
        Wall.start()
        wallbtn.configure(bg="gray")
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

def main_account_screen():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("400x350")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    #login_sucess()
    login_screen.mainloop()


main_account_screen()
