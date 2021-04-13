# This is a sample Python script.
import requests
from tkinter import *
from tkinter.ttk import *
import json

status = 0
isactive = 0
isadmin = 0
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#dwEntityList = int(81411932)
#dwGlowObjectManager = int(86951248)
#m_iGlowIndex = int(42040)
#m_iTeamNum = int(244)
#dwRadarBase = int(85822676)
#dwClientState = int(5828580)
#dwLocalPlayer = int(14205644)

def login(username, password):
    url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
    response = requests.get(url)


    if response.status_code != 200:
        print('Network is unavailable')
        exit()
    dwEntityList = int(response.json()["signatures"]["dwEntityList"])
    dwGlowObjectManager = int(response.json()["signatures"]["dwGlowObjectManager"])
    m_iGlowIndex = int(response.json()["netvars"]["m_iGlowIndex"])
    m_iTeamNum = int(response.json()["netvars"]["m_iTeamNum"])
    dwRadarBase = int(response.json()["signatures"]["dwRadarBase"])
    dwClientState = int(response.json()["signatures"]["dwClientState"])
    dwLocalPlayer = int(response.json()["signatures"]["dwLocalPlayer"])

    print(dwEntityList)
    print(dwGlowObjectManager)
    print(m_iGlowIndex)
    print(m_iTeamNum)
    print(dwRadarBase)
    print(dwClientState)
    print(dwLocalPlayer)


#    status = response.json()["status"]
 #   isactive = response.json()["info"][0]["isactive"]
 #   isadmin = response.json()["info"][0]["isadmin"]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    login('khashino', '25645')
    print(isactive)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
