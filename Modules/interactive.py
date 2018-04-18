import subprocess
import sys
def inter():
    result = subprocess.check_output(["nmap","-h"])
    result=result.splitlines(True)
    print result[1]
    for p in result[2:9]: print p
    HOST = raw_input("Enter Target Specification: ")
    HOST = HOST.split()
    print "\n"
    for p in result[9:20]: print p
    DISC = raw_input("Enter Host Discovery Option: ")
    DISC=DISC.split()
    print "\n"
    for p in result[20:29]: print p
    TECH = raw_input("Enter Scan Technique: ")
    TECH=TECH.split()
    print "\n"
    for p in result[29:37]: print p
    PORT = raw_input("Enter Port Specification ")
    PORT=PORT.split()
    print "\n"
    for p in result[37:43]: print p
    SERV = raw_input("Enter Service and Version Detection option: ")
    SERV=SERV.split()
    print "\n"
    for p in result[43:54]: print p
    SCRIPT = raw_input("Enter Script Scan Option: ")
    SCRIPT=SCRIPT.split()
    print "\n"
    for p in result[54:58]: print p
    OS = raw_input("Enter OS Detection Technique: ")
    OS=OS.split()
    print "\n"
    for p in result[58:71]: print p
    TIME = raw_input("Enter Timing and Performance Technique: ")
    TIME=TIME.split()
    print "\n"
    for p in result[71:85]: print p
    FIRE = raw_input("Enter Firewall/IDS Evasion and Spoofing Technique: ")
    FIRE=FIRE.split()
    print "\n"
    for p in result[85:100]: print p
    OUT = raw_input("Enter  Output Option: ")
    OUT=OUT.split()
    print "\n"
    for p in result[100:109]: print p
    MISC = raw_input("Enter Miscellaneous Technique: ")
    MISC=MISC.split()
    print "\n"

    mainlist = MISC + OUT + TIME + OS+ SCRIPT+SERV+PORT+TECH+DISC+HOST
    mainlist.insert(0, 'sudo nmap')
    print " ".join(mainlist)
    print " :: Scanning Initiated :: " 
    try:
       result=subprocess.check_output(mainlist)
       print(result)
    except Exception as e:
       print e
