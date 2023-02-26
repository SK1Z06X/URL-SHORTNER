import pyshorteners
import sys,getpass
import time
import os


cyan="\u001b[36m"
red="\u001b[31m"
meganta="\u001b[35m"
blue=" \u001b[34;1m"
yellow="\u001b[33m"
reset="\u001b[0m"
green="\u001b[32m"


  
logo=f'''{green}
          | ||~)|          
          |_||~\|_         
                           
                           
                           
                           
  (~|_|/~\|~)~|~(~|\ |(~|~)
  _)| |\_/|~\ | (_| \|(_|~\
                           


                                                      
'''
def animated(logo):
    for i in logo:
        sys.stdout.write(i)
       
        sys.stdout.flush()
        time.sleep(0.003)

animated(logo)


link=input(f'{cyan}enter your link:')


s = pyshorteners.Shortener()
sk=s.tinyurl.short(link)

print('your short link is:',sk)
