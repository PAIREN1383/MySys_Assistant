from datetime import datetime
from time import sleep
from os import system, name, startfile, path
from playsound import playsound # HINT: Install version 1.2.2
from socket import gethostname, gethostbyname
from requests import get


VoicesFolder = "؟؟؟:\\MySys voices\\"
CodeEditorPath = ""
BrowserPath = ""
SecureBrowserPath = ""
NotionPath = ""
MOGSPath = ""
GamePath = ""
DefragmentPath = ""
TempFolderPath1 = path.realpath("") 
TempFolderPath2 = path.realpath("")

SingleOpen = {
        "31": SecureBrowserPath,
        "32": NotionPath,
        "41": MOGSPath,
        "42": GamePath,
        "51": DefragmentPath,
        "52": TempFolderPath1,
        "53":TempFolderPath2
        }


def get_ip():
    host_name = gethostname()
    Local_IP = gethostbyname(host_name)
    print("***********************************")
    print(f"Local IP address: {Local_IP}")
    try:
        Public_IP = get("https://api.ipify.org", timeout=3).text
        print("\033[0;32;40m" + f"Public IP address: {Public_IP}" + "\033[0;47;40m")
    except:
        print("\033[0;31;40m" + "You are offline or there is a problem with your connection." + "\033[0;47;40m")
    print("***********************************\n***********************************")


def banner():
    system("cls" if name == "nt" else "clear") # Clearing terminal.
    print("\033[1;34;40m" + """
 __  __       ____                 _            _     _              _
|  \/  |_   _/ ___| _   _ ___     / \   ___ ___(_)___| |_ __ _ _ __ | |_
| |\/| | | | \___ \| | | / __|   / _ \ / __/ __| / __| __/ _` | '_ \| __|
| |  | | |_| |___) | |_| \__ \  / ___ \\\__ \__ \ \__ \ || (_| | | | | |_
|_|  |_|\__, |____/ \__, |___/ /_/   \_\___/___/_|___/\__\__,_|_| |_|\__|
        |___/       |___/
    """ + "\033[0;47;40m")
    nowdt = datetime.now()
    print(f"Datetime: {nowdt.strftime('%d-%m-%Y %H:%M:%S | %A, %d %B, %Y')}\n")
    get_ip()
    print("Special commands: \
        \nEnter 'q' or 'e' to exit. \
        \nEnter 'h' for Help. \
        \n*************************** \
        \nModes: \
        \n[1] Coding mode {Opening: Code Editor or IDE} \
        \n[2] Researching mode {Opening: Browser} \
        \n[3] Pentesting mode {Opening:  Secure Browser(1) and Notion(2)} \
        \n[4] Gaming mode {Opening: Multiplayer Online Gaming Service(1) and Game(2)} \
        \n[5] Cleaning system mode {Opening: Defragment and Optimize Drives(1) and Folder of temporary files(2,3)}")
    playsound(VoicesFolder + "Selection.mp3") # The voice that says choose.


# ========== MySys Starting ==========
print("MySys Assistant starting...")
sleep(10) # Once the system starts working, the systems also need rest.
playsound(VoicesFolder + "Welcome.mp3") # A welcoming voice.
while True:
    banner()
    Selection = input("Select your mode: ").strip()
    if Selection.lower() == "q" or Selection.lower() == "e" or Selection.lower() == "quit" or Selection.lower() == "exit":
        playsound(VoicesFolder + "Thanks.mp3")
        break
    if Selection.lower() == "h" or Selection.lower() == "help":
        print("""
******************** Help ********************
You can open multiple programs by selecting the mode or open only one program using the numbers below:
SingleOpen = {
        "31": Secure Browser,
        "32": Notion,
        "41": Multiplayer Online Gaming Service,
        "42": Game,
        "51": Defragment and Optimize Drives,
        "52": TempFolder1,
        "53": TempFolder2
}
Creator: MohammadAli
Github: https://github.com/PAIREN1383
""")
        playsound(VoicesFolder + "Help.mp3")
        input("<<< Press enter key to exit this section. >>>")
    elif Selection == "1":
        startfile(CodeEditorPath)
    elif Selection == "2":
        startfile(BrowserPath)
    elif Selection == "3":
        startfile(SecureBrowserPath)
        sleep(5)
        startfile(NotionPath)
        sleep(10)
    elif Selection == "4":
        pass
    elif Selection == "5":
        startfile(DefragmentPath)
        sleep(3)
        startfile(TempFolderPath1)
        sleep(1)
        startfile(TempFolderPath2)
    elif Selection.lower() in SingleOpen.keys():
        startfile(SingleOpen[Selection])
    else:
        print("You have entered an invalid value.")
        playsound(VoicesFolder + "Invalid value.mp3")