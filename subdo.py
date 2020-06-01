import requests as r
import socket
from time import sleep
from os import system as cmd
import sys

bnr = r'''
    _____           __           __        __    
   / __(_)___  ____/ /______  __/ /_  ____/ /___ 
  / /_/ / __ \/ __  / ___/ / / / __ \/ __  / __ \
 / __/ / / / / /_/ (__  ) /_/ / /_/ / /_/ / /_/ /
/_/ /_/_/ /_/\__,_/____/\__,_/_.___/\__,_/\____/ 
                                                 
 Github  : bangtebe/findsubdo   version : 1.0
'''


def findsubdo(cek):
    url1 = 'https://api.hackertarget.com/hostsearch/?q='+cek
    res1 = r.get(url1).text
    if not 'API count exceeded' in res1:
       for i in res1.split('\n'):
           print('>>> {}'.format(i))
    else:
        url = 'https://api.indoxploit.or.id/domain/'+cek
        res = r.get(url).json()
        if res['error'] == False:
           #["data"]["geolocation"]
           for i in res["data"]["subdomains"]:
               print('>>> {}, {}'.format(i,socket.gethostbyname(i)))
        else:print(res["errorMsg"])

def sl():
   for sl in "-\|/-\|/":
        print('\rPlease wait '+sl+' ',end="",flush=True)
        sleep(0.1)


def main():
    if len(sys.argv) == 2:
       sl()
       cmd('clear')
       print(bnr)
       findsubdo(sys.argv[1])

    else:
         sl()
         cmd('clear')
         print(bnr)
         try:
            i = input('[ input domain ] ')
            print()
            findsubdo(i)
         except KeyboardInterrupt:exit('\nkeluar')
         except Exception:exit()


main()
