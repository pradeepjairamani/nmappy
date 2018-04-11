import subprocess
import sys
import os
import smtplib
from datetime import date, timedelta

def mailme(message):
    print "Enable Login from less secure apps from here https://myaccount.google.com/lesssecureapps?pli=1 before mailing "
    gmail_user = "" #Write Down Gmail Username , Password and reciever's details here
    gmail_password=""
    to="" #if you want to send this to more then one email address try # to=["abc.gmail.com","xyz@somesite.com"]
    print message
    if gmail_user is "" and gmail_password is "":
        gmail_user=raw_input("Enter Gmail Username: ")
        gmail_password =raw_input("Enter Password: ")
        to=raw_input("Reciever's Email: ")
    sent_from=gmail_user
    subject= "NMAPPY Reports"
    body = message
    message = 'Subject: {}\n\n{}'.format(subject, body)
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()
        print 'Email sent!'
    except Exception,err:  
        print 'Something went wrong...' , err
    
def ndf():
    path="scan-files/"
    file1=path+"scan-"+str(date.today())+".xml"
    yesterday = date.today() - timedelta(1)
    if "scan-"+str(yesterday)+".xml" not in os.listdir("scan-files"):
        print "Yesterday's scan not found."
        file2= raw_input("If you want to enter filename manually, Enter file name else leave blank: ")
        
    else:
        file2=path+"scan-"+str(yesterday)+".xml"
    try:
        if file2 is not "":
            if path not in file2:
                file2=path+file2
            f2 =open(file2,"r")
            for line in f2:
                if "args=" in line:
                    a=line
            head,sep,tail=a.partition('args="')
            f2.close()
            payload,sep,tail=tail.partition('" start')
            print payload
            payload = payload.split()
            payload = [file1 if x==file2 else x for x in payload]
            result = subprocess.check_output(payload)
            pipe = subprocess.Popen(["ndiff",file2,file1],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, stderr = pipe.communicate()
            result=stdout.splitlines(True)

            if not result[3:]:
                print "No changes in network"
            else:
                mailme("\n".join(result))
        else:
            print ("Today's Scan")
            
            payload= raw_input("Enter Payload for Scan(Default-> nmap -oX "+file1+" 'host' ) Leave blank for default: ")
            if payload is "":
                host=raw_input("Enter Host Details: ")
                print "Scan Started"
                payload = ['nmap','-oX',file1,host]
            else:
                payload=payload.splitlines(True)
            result=subprocess.check_output(payload)
            print result
    except:
        print file2," not Found"


