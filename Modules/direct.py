import subprocess
import sys
def direct():
    mylist=[]
    for x in sys.argv:
        mylist.append(x)
    #mylist.remove("-v")
    del mylist[:2]
    result=subprocess.check_output(["nmap"]+mylist)
    print result

