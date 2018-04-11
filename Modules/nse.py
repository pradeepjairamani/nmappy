#!c:/Python27/python.exe -u
import subprocess
import sys
import os

def nse():
    PATH="C:\\Program Files (x86)\\Nmap\\scripts\\"
    PATHW=os.listdir(PATH)
    lists=[]
    lists2=[]
    lalist=[]
    flag=0

    print ( "\t\t    ::: Python NSE Scripts Automation :::      ")
    print ("\t\t    ::: Total " + str(len(PATHW)) + "   NSE Scripts Loaded :::   \n")
    #print ("        Show All the scripts of  NMap Scripting Engine ")

    for file in os.listdir(PATH):
        i=0
        lists2.append(file)
        a=""
        
        if "-" in file:
            while(file[i] != "-"):
                a=a+file[i]
                i+=1
            lists.append(a)
        else:
            lists.append(file)
    listwa= set(lists)
    print ("\t".join(sorted(listwa)))
       # print i,"\t",
    print ("\nTotal Options: " ,len(listwa))
    inp1= raw_input("\nEnter option you want to choose(Like for HTTP scripts type http): ")
    if inp1 in listwa:
        for inpt in lists2:
            if inp1 in inpt:
                print inpt
               # result = subprocess.check_output(['nmap','--script-help', inp1])
               # print result
        while(True):
            script = raw_input("Type Option: ")
            if script in lists2:
                print " :: Payload Selected :: ",script
                result = subprocess.check_output(['nmap','--script-help', script],stderr=subprocess.STDOUT)
                head,sep,tail=result.partition("Time")
                print tail
                with open(PATH+script) as openfile:
                    for line in openfile:
                        if "--script" in line and "nmap" in line:
                            if "@usage" not in line:
                                print "Usage :" ,line[3:]
                            else:
                                print "Usage :",line[9:]
                            flag=1
                    if flag==0:
                        print "Please Check The URL for the script usage"
                while(True):
                  #  if option =="launch":# or option is 'l' or option is 'L' or option is '1':
                        #host = raw_input("Enter Host :")
                    payload= raw_input("Enter Command: ")
                    for word in payload.split(" "):
                        lalist.append(word)
                    try:
                        result = subprocess.check_output(lalist,stderr=subprocess.STDOUT)
                        print result
                    except:
                        print "There's an error with the command :\ Please Check it again"
            else:
                print "Script Not Found"
    else:
        print "Option not Found"

