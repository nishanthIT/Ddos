import requests
import threading
import queue

q= queue.Queue()
valid_proxies = queue.Queue()

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
            r = requests.get("https://api.ipify.org?format=json",proxies={"http":proxy,"https":proxy})
        except:
            continue
        if(r.status_code == 200):
            print(proxy)
            with open("ValidProxy.txt","a") as vali_prox:
                vali_prox.write(proxy+"\n")
           

for _ in range(50):
    threading.Thread(target=check_proxy).start()           




