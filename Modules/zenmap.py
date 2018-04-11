from __future__ import print_function
import subprocess
import sys


def zenmap():
        x= '''
        [1] Regular Scan
        [2] Quick Scan
        [3] Quick Scan Plus
        [4] Quick TraceRoute
        [5] Intense Scan
        [6] Intense Scan plus UDP
        [7] Intense Scan plus All TCP ports
        [8] Intense Scan with no Ping
        [9] Slow Comprehensive Scan
        [10] Ping Scan
        [11] Exit
        '''
        #    while(1):
        print(x)
        h=raw_input("Enter Your Choice: ")
        host = raw_input("Enter Host, IP address, IP range or Subnet: ")
        print("[+] Scan Started")
        if h == "1":
            result = subprocess.check_output(['nmap',host])
            print(result)
        if h=="2":
            result = subprocess.check_output(['nmap','-T4','-F',host])
            print(result)
        if h=="3":
            result = subprocess.check_output(['nmap','-sV','-F','-T4','-O','--version-light',host]) #nmap -sV -T4 -O -F --version-light
            print(result)
        if h=="4":
            result = subprocess.check_output(['nmap','-sn','--traceroute',host]) #nmap -sn --traceroute
            print(result)
        if h=="5":
            result = subprocess.check_output(['nmap','-T4','-A','-v',host]) #nmap -T4 -A -v
            print(result)
        if h=="6":
            result = subprocess.check_output(['nmap','-sS','-sU','-T4','-A','-v',host]) #nmap -sS -sU -T4 -A -v
            print(result)
        if h=="7":
            result = subprocess.check_output(['nmap','-p','1-65535','-T4','-A','-v',host]) #nmap -p 1-65535 -T4 -A -v
            print(result)
        if h=="8":
            result = subprocess.check_output(['nmap','-T4','-A','-v','-Pn',host]) #nmap -T4 -A -v -Pn
            print(result)
        if h=="9":
            result = subprocess.check_output(['nmap','-sS','-sU','-T4','-A','-v','-PE','-PP','-PS80,443','-PA3389','-PU40125','-PY','-g','53','--script','"default','or','(discovery','and','safe)"',host]) #nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)"
            print(result)
        if h=="10":
            result = subprocess.check_output(['nmap','-sn',host]) #nmap -sn
            print(result)
        if h=="11":
            raise SystemExit
