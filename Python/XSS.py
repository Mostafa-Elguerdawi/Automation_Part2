import requests
import threading
from termcolor import colored as cl

print("")
print(cl("Command : cat endpoints.txt | grep \"=\" | gf xss | qsreplace payload >> XSS_Params.txt", color='red'))
print("")
fil = input(cl("Enter Your File >>> ", color='blue'))
urls = open(fil, 'r').read().split('\n')

def XSS_Scan(payload):
    for url in urls:
        try:
            req = requests.get(url, timeout=5).text
            if payload in req:
                print(cl(f"Check This ===> {url}", color='green'))
                print("")
                xss = open("XSS_Result.txt", 'a')
                xss.write(f"{url}\n")
            else:
                pass
        except Exception as e:
            #print(e)
            continue

print("")            
payload = input(cl("Enter Payload To Match >>> ", color='blue'))
print("")
XSS_Scan(payload)

#thread = 10
#threads = []
#for z in range(thread):
#    t = threading.Thread(target=XSS_Scan, args=(payload))
#    threads.append(t)
#    t.start()
#for t in threads:
#    t.join()
