from datetime import datetime
from time import sleep
from os import system, name, startfile, path
from playsound import playsound  # HINT: Install version 1.2.2
from socket import gethostname, gethostbyname
from requests import get
import webbrowser

VPN_AUTO_START = True
VoicesFolder = "???:\\MySys voices\\"
CodeEditorPath = ""
BrowserPath = ""
VPNPath = ""
YouTubeURL = "https://YouTube.com"
GitHubURL = "https://GitHub.com"
StackOverflowURL = "https://stackoverflow.com/"
YouCodeURL = "https://you.com/code"
MessengerPath = ""
SecureBrowserPath = ""
NotionPath = ""
MOGSPath = ""
GamePath = ""
DefragmentPath = ""
TempFolderPath1 = path.realpath("")
TempFolderPath2 = path.realpath("")


def url_opener(website_url):
    webbrowser.open_new_tab(website_url)


SingleOpen = {
    "11": CodeEditorPath,
    "21": BrowserPath,
    "31": SecureBrowserPath,
    "32": NotionPath,
    "41": MOGSPath,
    "42": GamePath,
    "51": DefragmentPath,
    "52": TempFolderPath1,
    "53": TempFolderPath2,
    "61": MessengerPath,
}


SingleOpenURL = {
    "12": GitHubURL,
    "22": StackOverflowURL,
    "23": YouCodeURL,
    "62": YouTubeURL
}


def start_vpn(on_off):
    if on_off == True:
        startfile(VPNPath)


def test_network(IP_address=None):
    try:
        print("****************** Result ******************")
        if IP_address == None:
            IP_address = get("https://api.ipify.org", timeout=5).text
        IP_info = get(f"https://ipwho.is/{IP_address}", timeout=15)
        print(IP_info.text.replace(",", ",\n"))
        input("<<< Press Enter to exit this section and clear the terminal. >>>")
    except:
        print("\033[0;31;40m" +
              "You are offline or there is a problem with your connection." + "\033[0;47;40m")
        input("<<< Press Enter to exit this section and clear the terminal. >>>")


def get_ip():
    host_name = gethostname()
    Local_IP = gethostbyname(host_name)
    print("***********************************")
    print(f"Local IP address: {Local_IP}")
    try:
        on_or_off = "OFF"
        if VPN_AUTO_START == True:
            on_or_off = "ON"
            print("Your VPN auto-start is turned on. Your public IP will change.")
        Public_IP = get("https://api.ipify.org", timeout=10).text
        print("\033[0;32;40m" +
              f"Public IP address (VPN: {on_or_off}): {Public_IP}" + "\033[0;47;40m")
    except:
        print("\033[0;31;40m" +
              "You are offline or there is a problem with your connection." + "\033[0;47;40m")
    print("***********************************\n***********************************")


def banner():
    system("cls" if name == "nt" else "clear")  # Clearing terminal.
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
        \n[1] Coding {Opening: Code Editor or IDE(1) and GitHub website(2)} \
        \n[2] Researching {Opening: Browser(1), Stack Overflow website(2), Youcode website(3)} \
        \n[3] Pentesting {Opening: Secure Browser(1) and Notion(2)} \
        \n[4] Gaming {Opening: Multiplayer Online Gaming Service(1) and Game(2)} \
        \n[5] Cleaning system {Opening: Defragment and Optimize Drives(1) and Folder of temporary files(2,3)} \
        \n[6] Social media {Opening: Messenger(1) and YouTube website(2)} \
        \n[!] Tools {Opening: VPN app(71), your ip info(72), IP WHOIS(73)}")
    # The voice that says choose.
    playsound(VoicesFolder + "Selection.mp3")


# ========== MySys Starting ==========
print("MySys Assistant starting...")
sleep(10)  # Once the system starts working, the systems also need rest.
playsound(VoicesFolder + "Welcome.mp3")  # A welcoming voice.
start_vpn(VPN_AUTO_START)
while True:
    banner()
    selection = input("Select your mode: ").strip()
    if selection.lower() == "q" or selection.lower() == "e" or selection.lower() == "quit" or selection.lower() == "exit":
        playsound(VoicesFolder + "Thanks.mp3")
        break
    if selection.lower() == "h" or selection.lower() == "help":
        print("""
******************** Help ********************
You can open multiple programs by selecting the mode or open only one program using the numbers below:
SingleOpen = {
    "11": CodeEditorPath,
    "21": BrowserPath,
    "31": SecureBrowserPath,
    "32": NotionPath,
    "41": MOGSPath,
    "42": GamePath,
    "51": DefragmentPath,
    "52": TempFolderPath1,
    "53": TempFolderPath2,
    "61": MessengerPath,
}
GitHub: https://github.com/PAIREN1383
""")
        playsound(VoicesFolder + "Help.mp3", block=False)
        input("<<< Press Enter to exit this section. >>>")
    elif selection == "1":
        startfile(CodeEditorPath)
    elif selection == "2":
        startfile(BrowserPath)
    elif selection == "3":
        startfile(SecureBrowserPath)
        sleep(5)
        startfile(NotionPath)
        sleep(10)
    elif selection == "4":
        startfile(MOGSPath)
        sleep(5)
        startfile(GamePath)
    elif selection == "5":
        startfile(DefragmentPath)
        sleep(3)
        startfile(TempFolderPath1)
        sleep(1)
        startfile(TempFolderPath2)
    elif selection == "6":
        startfile(MessengerPath)
        sleep(10)
        url_opener(YouTubeURL)
    elif selection == "71":
        if VPN_AUTO_START == False:
            start_vpn(True)
            print("Now your vpn is ON. Your IP will change.")
        else:
            print("Your VPN is already turned on.")
        input("Press Enter to test the VPN.")
        print("************************************\ntesting network...")
        test_network()
    elif selection == "72":
        test_network()
    elif selection == "73":
        target_ip = input("Enter the desired IP address: ")
        test_network(target_ip)
    elif selection in SingleOpen.keys():
        startfile(SingleOpen[selection])
    elif selection in SingleOpenURL.keys():
        url_opener(SingleOpenURL[selection])
    else:
        print("You have entered an invalid value.")
        playsound(VoicesFolder + "Invalid value.mp3", block=False)
