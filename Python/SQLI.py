import requests
from termcolor import colored as cl

print(" ")
print(cl("Command : cat endpoints | grep \"=\" | gf sqli | qsrelace ' >> SQLI_Params.txt", color='red'))
print(" ")
fil = input(cl("Enter Your File >>> ", color='blue'))
print("")
urls = open(fil, 'r').read().split('\n')

def SQLI_Scan(match):
    print(cl("SQLI Scan Started...", color='red'))
    for url in urls:
        try:
            req = requests.get(url).text
            if match in req:
                print(cl(f"Check This ===> {url}", color='green'))
                print(" ")
                lfi = open("SQLI_Results", 'a')
                lfi.write(f"{url}\n")
            else:
                pass
        except Exception as e:
            #print(e)
            continue

match = input(cl("Enter Match Keyword >>> ", color='blue'))
SQLI_Scan(match)
