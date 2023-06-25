from options import Option
from time import sleep
import subprocess
import os
from color import bred, bgreen, byellow, red, green, yellow
import sys
import multiprocessing
import time
import urllib.request


def hide_file():
    subprocess.run(["mv", "smtp_cred.py", ".smtp_cred.py"])
    subprocess.run(["mv", "mailspoofer.py", ".mailspoofer.py"])
    
def unhide_file():
    subprocess.run(["mv", ".smtp_cred.py", "smtp_cred.py"])
    subprocess.run(["mv", ".mailspoofer.py", "mailspoofer.py"])
    
def sprint(text, second=0.04):
    for line in text + '\n':
        sys.stdout.write(line)
        sys.stdout.flush()
        sleep(second)
        
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

        
if __name__ == '__main__':
    if connect():
        lis = [f'{red}|',f'{bred}/',f'{red}-',f'{byellow}\\',f'{yellow}|',f'{byellow}/',f'{green}-',f'{bgreen}\\',f'{green}|']*6
        for i in lis:
            print(f'\r{bred}Starting . . . {i}',end='', flush=True)
            sleep(0.1)
        os.system('clear')
        sprint(f'{bred}Mail spoofer loading . {byellow}. {bgreen}.')
        sleep(2)
        k = Option()
        try:
            if k == '1':
                os.system('clear')
                from user_cred import spoofed_email, reciever_email, subject, message, mess_header
                sprint(f'Getting smtp server ready to send mail . {byellow}. {bgreen}.')
                sleep(1)
                sprint(f'{bred}Sender is {bgreen}{spoofed_email}')
                print('\n\n')
                Emails = []
                with open('Emails.txt', 'r') as emails:
                    from user_cred import spoofed_email, reciever_email, subject, message, mess_header
                    count = 1
                    for email in emails:
                        Emails.append(email)
                for email in Emails:
                    if count != 300:
                        reciever_email = email
                        unhide_file()
                        from smtp_cred import *
                        from mailspoofer import sendSpoofmail
                        
                        def task2():
                            mes = "Sending mail"
                            prog = '->'*15
                            done = '📩'
                            sprint(f'{bred}{mes} {bgreen}{prog}{byellow} {done} {bgreen}{reciever_email}',0.03)  
                            
                        p1 = multiprocessing.Process(target=sendSpoofmail, args=[smtp_user_email, smtp_server_domain, smtp_api_key, spoofed_email, reciever_email, subject, message, mess_header])
                        p2 = multiprocessing.Process(target=task2)
                        p1.start()
                        p2.start()
                        p1.join()
                        p2.join()
                        print('\n')
                        
                        #print(f'{byellow}Status: {bgreen}recieved!\n')
                        
                        
                        hide_file()
                        count+=1
                
                    else:
                        sprint('You have reach the limit for today')
                sprint('\nDone sending messsage\nExiting Program . . . \n\n')
                sleep(1)

            elif k == '2':
                os.system('clear')
                from user_cred import spoofed_email, reciever_email, subject, message, mess_header
                sprint(f'Getting smtp server ready to send mail . {byellow}. {bgreen}.')
                sleep(1)
                sprint(f'{bred}Sender is {bgreen}{spoofed_email}')
                print('\n\n')
                unhide_file()
                from smtp_cred import *
                from user_cred import spoofed_email, reciever_email, subject, message, mess_header
                from mailspoofer import sendSpoofmail
                def task2():
                    mes = "Sending mail"
                    prog = '->'*15
                    done = '📩'
                    sprint(f'{bred}{mes} {bgreen}{prog}{byellow} {done} {bgreen}{reciever_email}',0.03)
                    
                    
                p1 = multiprocessing.Process(target=sendSpoofmail, args=[smtp_user_email, smtp_server_domain, smtp_api_key, spoofed_email, reciever_email, subject, message, mess_header])
                p2 = multiprocessing.Process(target=task2)
                p1.start()
                p2.start()
                p1.join()
                p2.join()

                sprint('\n\nDone sending messsage\nExiting Program . . . \n\n')
                sleep(1)
                hide_file()
                
            elif k == '#':
                sprint('\nExiting program . . .\n\n')
                sleep(1)
                
            else:
                error_message = '\n!!! No Such option Choose correctly . . .'
                print(error_message)
                sprint('\nExiting program . . .\n\n')
                sleep(1)
        except KeyboardInterrupt:
            sprint('Exiting ...')
            subprocess.run(["mv", "smtp_cred.py", ".smtp_cred.py"])
    else:
        sprint(f'{bred}Not connected to the internet {bgreen}!!!')