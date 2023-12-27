import requests
import threading
import queue

q= queue.Queue()
valid_proxies = queue.Queue()


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
Test Your Poxy
      
      """)

url = input("Enter Target Url to Test Proxy:")

with open("ProxyList.txt","r") as f:
    proxy = f.read().split("\n")
    for p in proxy:
        # print(p)
        q.put(p)
       


def check_proxy():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            r = requests.get(url,proxies={"http":proxy,"https":proxy})
        except:
            continue
        if(r.status_code == 200):
             print(f"Added to list: {proxy}")
             with open("ValidProxy.txt","a") as vali_prox:
                vali_prox.write(proxy+"\n")
           

for _ in range(50):
    threading.Thread(target=check_proxy).start()        
print("This are Working proxy thay are appended to ValidProxy.txt")


