import pymem
import pymem.process
import re
import time
import requests


def updatevar():
    global dwEntityList
    global dwGlowObjectManager
    global m_iGlowIndex
    global m_iTeamNum
    global dwRadarBase
    global dwClientState
    global dwLocalPlayer

    url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
    response = requests.get(url)

    if response.status_code != 200:
        print('Network is unavailable')
        dwEntityList = int(81411932)
        dwGlowObjectManager = int(86951248)
        m_iGlowIndex = int(42040)
        m_iTeamNum = int(244)
        dwRadarBase = int(85822676)
        dwClientState = int(5828580)
        dwLocalPlayer = int(14205644)
    else:
        dwEntityList = int(response.json()["signatures"]["dwEntityList"])
        dwGlowObjectManager = int(response.json()["signatures"]["dwGlowObjectManager"])
        m_iGlowIndex = int(response.json()["netvars"]["m_iGlowIndex"])
        m_iTeamNum = int(response.json()["netvars"]["m_iTeamNum"])
        dwRadarBase = int(response.json()["signatures"]["dwRadarBase"])
        dwClientState = int(response.json()["signatures"]["dwClientState"])
        dwLocalPlayer = int(response.json()["signatures"]["dwLocalPlayer"])


def makeitready():
    global pm
    global client
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll")


def esp():
    print("ESP wall is on.")
    try:
        pm = pymem.Pymem("csgo.exe")
    except Exception as e:
        print(e)
        #MessageBox = ctypes.windll.user32.MessageBoxW
        #MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
        return

    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    glow_manager = pm.read_int(client + dwGlowObjectManager)
    #read("glow")
   # print("before while")
    while True:
        try:
            #read("glow")
           # print("1")
            for i in range(1, 32):  # Entities 1-32 are reserved for players.
                entity = pm.read_int(client + dwEntityList + i * 0x10)
                #print("2")
                if entity:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    player = pm.read_int(client + dwLocalPlayer)
                    player_team = pm.read_int(player + m_iTeamNum)
                    entity_glow = pm.read_int(entity + m_iGlowIndex)


                    ennemies_color = [1, 0, 0, 1.5]
                    allies_color = [0, 1, 0, 0.5]
                    #all_color = [1, 1, 1, 1]

                    if entity_team_id == player_team:  # Terrorist
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(allies_color[0]))  # R
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(allies_color[1]))  # G
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(allies_color[2]))  # B
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(allies_color[3]))  # Alpha
                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)  # Enable glow


                    if entity_team_id != player_team:  # Counter-terrorist
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(ennemies_color[0]))  # R
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(ennemies_color[1]))  # G
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(ennemies_color[2]))  # B
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(ennemies_color[3]))  # Alpha
                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)  # Enable glow

                    #time.sleep(0.002)

        except Exception as e:
            print(e)

    pm.close_process()



def wall():
    makeitready()
    print("wall secound is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',clientModule).start() + 2


    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)

def radar():
    makeitready()
    print("radar is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08', clientModule).start() + 6

    pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)


def Money():
    makeitready()
    print("radar is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',clientModule).start()

    pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)

def main():

    while True:
        cheat = int(input("Enter Number  :  "))
        if cheat == 1:
            #makeitready()
            esp()
        elif cheat == 2:
            makeitready()
            radar()
        elif cheat == 3:
            makeitready()
            Money()
        elif cheat == 4:
            makeitready()
            wall()
        elif cheat == 5:
            pm.close_process()
            print("Its Off Now")
        elif cheat == 6:
            pm.close_process()
            print("See U Soon")
            time.sleep(1)
            exit()
        else:
            print("beyne gozine ha entekhab kon!!!")

if __name__ == '__main__':
    main()

#https://github.com/danielkrupinski/OneByteWallhack/blob/master/OneByteWallhack.py
#https://github.com/danielkrupinski/OneByteRadar/blob/master/OneByteRadar.py
#https://github.com/frk1/hazedumper/blob/master/csgo.hpp
#https://github.com/naaax123/Python-CSGO-Cheat
#https://github.com/ALittlePatate/Rainbow-v2
#https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json