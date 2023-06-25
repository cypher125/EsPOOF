#!/usr/bin/python3
import subprocess


def sendSpoofmail(smtp_user_email, smtp_server_domain, smtp_api_key, spoofed_email, reciever_email, subject, message, mess_header):  
    #command = ["ls", "-l"]
    command = ["sendemail", "-xu", smtp_user_email, "-xp", smtp_api_key, "-s", smtp_server_domain, "-f", spoofed_email, "-t", reciever_email, "-u", subject, "-m", message, "-o", f"message-header=From: {mess_header} <{spoofed_email}>" ]
    #print(command)
    subprocess.run(command) 
    #stdout=subprocess.DEVNULL,
    #stderr=subprocess.STDOUT)
    #CompletedProcess(args=['ls', '-l'], returncode=0)






