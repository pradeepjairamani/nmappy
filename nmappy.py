import argparse
from Modules import nse
from Modules import sploit
from Modules import zenmap
from Modules import direct
from Modules import interactive
from Modules import ndf

HELP = '''
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

5: Zenmap Default Scansterm -> nmappy.py -z or nmappy.py --zenmap

6: Directly enter NMAP commands -> nmappy.py -d or nmappy.py --direct

7: Help (You are Looking at it baby) -> nmappy.py -h or nmappy.py --help

'''


def main():
    parser = argparse.ArgumentParser(description=HELP)

    parser.add_argument('-d' , '--direct' , dest='direct',  help='Direct Nmap Search'  , action="store_true")
    parser.add_argument('-n' , '--nse' , dest='nse'  , help='Nmap with Scripting Engine' , action="store_true")
    parser.add_argument('-z', '--zenmap', dest='zenmap', help='Call Nmap With Zenmap GUI', action="store_true" )
    parser.add_argument('-s', '--sploit', dest='sploit' , help='Nmap With Sploit' , action="store_true")
    parser.add_argument('-i', '--interactive', dest='interactive' , help='Nmap with interactive Shell' ,action="store_true")
    parser.add_argument('-m', '--mail', dest='mail', help='Feature Under Dev', action="store_true")

    args = parser.parse_args()

    if args.direct:
        print("[+] Initiating Direct Mode ")
        direct.direct()
    elif args.nse:
        print("[+] Initiating NSE Mode ")
        nse.nse()
    elif args.zenmap:
        print("[+] Initiating Zenmap Mode ")
        zenmap.zenmap()
    elif args.sploit:
        print("[+] Initiating Sploit Mode ")
        sploit.sploit()
    elif args.interactive:
        print("[+] Initiating Iter Mode ")
        interactive.inter()
    elif args.mail:
        print("Under Development")
    else:
        pass


if __name__ == '__main__':
    main()
