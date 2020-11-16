from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Sito:

    def __init__(self,h1,h2,h3,h4,link,div,script):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.link = link
        self.div = div
        self.script = script

    def BootStrap(self):
        bsurl = "maxcdn.bootstrapcdn.com"
        for x in self.link:
            if bsurl in str(x.get("href")):
                return(bcolors.OKGREEN + "BootStrap"+ bcolors.ENDC)
        return(bcolors.FAIL + "BootStrap"+ bcolors.ENDC)
    
    def jQuery(self):
        jqurl = "code.jquery.com"
        for x in self.script:
            if jqurl in str(x.get("src")):
                return(bcolors.OKGREEN + "Jquery"+ bcolors.ENDC)
        return(bcolors.FAIL + "Jquery"+ bcolors.ENDC)




    def Dati(self):
        print(f"""
    --- RESULT ---    

        H1 : {len(self.h1)}
        H2 : {len(self.h2)}
        H3 : {len(self.h3)}
        H4 : {len(self.h4)}
        
        Link : {len(self.link)}
        Div : {len(self.div)}
        Script : {len(self.script)}   

        --- LIBRARY ---

        {self.BootStrap()}       
        {self.jQuery()}   
        
    --- RESULT ---       
        """)

def Search(site):
    
    h1 = site.find_all(name = "h1")
    h2 = site.find_all(name = "h2")
    h3 = site.find_all(name = "h3")
    h4 = site.find_all(name = "h4")
    link = site.find_all(name = "link")
    div = site.find_all(name = "div")
    script = site.find_all(name = "script")

    return Sito(h1,h2,h3,h4,link,div,script)

