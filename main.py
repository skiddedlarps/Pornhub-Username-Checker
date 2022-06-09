try: 
    import threading, requests, ctypes, os
    from colorama import Fore, Style
    from pystyle import Center, Anime, Colors, Colorate, System
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt using `pip install -r requirements.txt`")

name = "Pornhub Username Checker"

System.Clear()
System.Title(f"{name} ")
System.Size(120, 30)

proxies = []
w = Fore.WHITE
l = Fore.LIGHTBLUE_EX
rs = Style.RESET_ALL
g = Fore.GREEN
re = Fore.RED

class MAIN:
    def __init__(self):
        # req
        self.checking = True
        self.counter = 0
        self.proxy_counter = 0
        self.usernames = []
        self.lock = threading.Lock()
        self.session = requests.Session()
        # var
        self.Available = 0
        self.Taken = 0
        self.Checked = 0
        self.Errors = 0
        self.Retries = 0

    def safeprint(self, arg):
        self.lock.acquire()
        print(arg)
        self.lock.release()

    def loadusernames(self): 
        if os.path.exists("usernames.txt"):
            with open ("usernames.txt","r",encoding="UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    self.usernames.append(line)
                if len(self.usernames) == 0:
                    self.safeprint(ape)
                    print(Fore.RED + f"\a\n\t\t{l}[!] {w}Usernames file is empty, please put in lines.")
                    input(); quit()
        else:
            open ("usernames.txt", "x")
            self.safeprint(ape)
            print(Fore.RED + f"\a\n\t\t{l}[!] {w}Usernames file is empty, please put lines in.")
            input(), quit()

    def loadproxies(self): 
        if os.path.exists("proxies.txt"):
            with open ("proxies.txt","r",encoding="UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    proxies.append(line)
                if len(proxies) == 0:
                    self.safeprint(ape)
                    print(Fore.RED + f"\a\n\t\t{l}[!] {w}Proxies file is empty, please put in proxies.")
                    input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()
        else:
            open ("proxies.txt", "x")
            self.safeprint(ape)
            print(Fore.RED + f"\a\n\t\t{l}[!] {w}Proxies file is empty, please put in proxies.")
            input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()

    def Threads(self):
        try:
            os.system('cls')
            self.safeprint(ape)
            threads = int(input(f'\n\t\t{w}> {l}Threads: {rs}'))
            os.system('cls')
            self.safeprint(ape)
            return threads
        except ValueError:
            self.Threads()

    def title(self): 
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name} - Checked: {self.Checked} |  Available: {self.Available} | Taken: {self.Taken} | Retries: {self.Retries} | Developed by @skiddedlarps on Github")

    def login(self,username,proxy): 
        self.title()
        try:
            if len(username) <= 6:
                return
            url = f"https://www.pornhub.com/users/{username}"
            proxiess = {"http":f"http://{proxy}","https":f"http://{proxy}"}
            r = self.session.get(url,proxies=proxiess)
            if 'Error Page Not Found' in r.text:
                self.Checked += 1
                self.Available += 1
                self.safeprint(f"\t\t{l}[{w}!{l}] {g}Available {w}" + username)
                with open("Available.txt", "a") as f:
                    f.write(username + "\n")
            if 'Last Login' in r.text:
                self.safeprint(f"\t\t{l}[{w}!{l}] {re}Taken {w}" + username)
                self.Checked += 1
                self.Taken += 1
            self.title()
        except Exception as e: 
            self.Retries += 1
            self.login(username,proxy)
            self.title()
            pass

    def start(self):
        self.loadproxies()
        self.loadusernames()
        threads = self.Threads()
        
        def thread_starter():
            self.login(self.usernames[self.counter],proxies[self.proxy_counter])    
        
        while self.checking:
            try:
                if threading.active_count() <= threads:
                    threading.Thread(target = thread_starter).start()
                    self.proxy_counter += 1
                    self.counter += 1
                if len(proxies) <= self.proxy_counter:
                    self.proxy_counter = 0
                if len(self.usernames) <= self.counter:
                    self.checking = False
            except Exception as e:
                pass

ape = (Fore.LIGHTBLUE_EX + f"""
\t\t██████╗ ███████╗██╗      █████╗ ██╗   ██╗███████╗██████╗ 
\t\t██╔══██╗██╔════╝██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
\t\t██████╔╝███████╗██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
\t\t██╔═══╝ ╚════██║██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
\t\t██║     ███████║███████╗██║  ██║   ██║   ███████╗██║  ██║
\t\t╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚════{w}github.com/skiddedlarps{l}                                                                                                                                                                                                                                                                                 
""")   

banner = f"""
 ██▓███    ██████  ██▓    ▄▄▄     ▓██   ██▓▓█████  ██▀███  
▓██░  ██▒▒██    ▒ ▓██▒   ▒████▄    ▒██  ██▒▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒░ ▓██▄   ▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒  ▒   ██▒▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░▒██████▒▒░██████▒▓█   ▓██▒ ░ ██▒▓░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░     ░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
░░       ░  ░  ░    ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░ 
               ░      ░  ░     ░  ░░ ░        ░  ░   ░     
                                   ░ ░                     
                                                                                                                                                
                   Press Enter To Continue
"""[1:]

Anime.Fade(Center.Center(banner), Colors.rainbow, Colorate.Vertical, enter=True)

obj = MAIN()
obj.start()
input()
