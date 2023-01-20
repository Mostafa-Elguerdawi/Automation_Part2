import requests
import threading
from termcolor import colored as cl

print("")
print(cl("Command : cat endpoints.txt | grep \"=\" | gf ssti | qsreplace ${{7*7}} >> XSS_Params.txt", color='red'))
print("")
fil = input(cl("Enter Your File >>> ", color='blue'))
urls = open(fil, 'r').read().split('\n')

def SSTI_Scan(payload):
    print(" ")
    print(cl("SSTI Scan Started...", color='red'))
    for url in urls:
        try:
            req = requests.get(url, timeout=5).text
            if match in req:
                print(cl(f"Check This ===> {url}", color='green'))
                print("")
                xss = open("SSTI_Result.txt", 'a')
                xss.write(f"{url}\n")
            else:
                pass
        except Exception as e:
            #print(e)
            continue

print("")            
payload = input(cl("Enter Payload To Match >>> ", color='blue'))
print("")
SSTI_Scan(payload)
