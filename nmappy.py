import sys
from Modules import nse
from Modules import sploit
from Modules import zenmap
from Modules import direct
from Modules import interactive
from Modules import ndf

HELP='''
     .-') _ _   .-')      ('-.      _ (`-.    _ (`-.             
    ( OO ) | '.( OO )_   ( OO ).-. ( (OO  )  ( (OO  )            
,--./ ,--,' ,--.   ,--.) / . --. /_.`     \ _.`     \ ,--.   ,--.
|   \ |  |\ |   `.'   |  | \-.  \(__...--''(__...--''  \  `.'  / 
|    \|  | )|         |.-'-'  |  ||  /  | | |  /  | |.-')     /  
|  .     |/ |  |'.'|  | \| |_.'  ||  |_.' | |  |_.' (OO  \   /   
|  |\    |  |  |   |  |  |  .-.  ||  .___.' |  .___.'|   /  /\_  
|  | \   |  |  |   |  |  |  | |  ||  |      |  |     `-./  /.__) 
`--'  `--'  `--'   `--'  `--' `--'`--'      `--'       `--'

                                            By Pradeep Jairamani

This script performs following functions:

1: Automating Nmap Scripting Engine Scripts -> nmappy.py -n or nmappy --nse

2: Searching Exploits using Nmap scan results (Uses searchsploit for searching exploits, only works for ubuntu) -> nmappy.py -s or nmappy.py --sploit

3: Finding difference in day-to-day scans and if any difference is found, a mail is send to the user automatically. -> nmappy.py -m or nmappy.py --mail

4: Interactive NMAP scanning -> nmappy.py -i or nmappy.py --interactive

5: Zenmap Default Scans -> nmappy.py -z or nmappy.py --zenmap

6: Directly enter NMAP commands -> nmappy.py -d or nmappy.py --direct

7: Help (You are Looking at it baby) -> nmappy.py -h or nmappy.py --help

'''

try:
    if sys.argv[1]=="-d" or sys.argv[1]=="--direct":
        direct.direct()
    elif sys.argv[1]=="-n" or sys.argv[1]=="--nse":
        nse.nse()
    elif sys.argv[1]=="-z" or sys.argv[1]=="--zenmap":
        zenmap.zenmap()
    elif sys.argv[1]=="-s" or sys.argv[1]=="--sploit":
        sploit.sploit()
    elif sys.argv[1]=="-i" or sys.argv[1]=="--interactive":
        interactive.inter()
    elif sys.argv[1]=="-m" or sys.argv[1]=="--mail":
        ndf.ndf()
    elif sys.argv[1]=="-h" or sys.argv[1]=="--help":
        print (HELP)
except IndexError:
    print (HELP)
except Exception,err:
    print str(err)
