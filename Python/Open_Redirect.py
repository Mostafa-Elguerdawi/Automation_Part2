import requests
from termcolor import colored as cl

print(" ")
print(cl("Command : cat endpoints | grep \"=\" | gf redirect | qsrelace '\\evil.com' >> Redirect_Params.txt", color='red'))
print(" ")
fil = input(cl("Enter Your File >>> ", color='blue'))
print("")
urls = open(fil, 'r').read().split('\n')

def Open_Redirect_Scan(match):
    print(" ")
    print(cl("Open_Redirect Scan Started...", color='red'))
    for url in urls:
        try:
            req = requests.get(url).url
            if match == req:
                print(cl(f"Check This ===> {url}", color='green'))
                print(" ")
                ope = open("Open_Redirect_Results", 'a')
                ope.write(f"{url}\n")
            else:
                pass
        except Exception as e:
            #print(e)
            continue

match = input(cl("Enter Match Keyword >>> ", color='blue'))
Open_Redirect_Scan(match)
