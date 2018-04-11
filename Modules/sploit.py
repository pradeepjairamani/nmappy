from __future__ import print_function
from xml.dom import minidom
import subprocess
import os
import sys
#nmap -sV -oX PATH HOST
def sploit():
    try:
        import apt
        cache = apt.cache.Cache()
        cache.update()
        pkg=cache['exploitdb']
        if pkg.is_installed:
                print("Configuration Check Successful :D We are good to go")
                HOST = raw_input("Enter Host ")
                optn=raw_input("Enable Version Detection for searchsploit? Provides less but accurate results [y/n]: ") 
                print("Running NMAP")
                PATH=os.getcwd() + "//scan.xml"
                result = subprocess.check_output(['nmap','-sV','-oX',PATH,HOST])
                print (result)
                xmldoc = minidom.parse(PATH)
                itemlist = xmldoc.getElementsByTagName('service')
                i=0
                length=len(itemlist)
                while ( i < length):
                    i=i+1
                    try:
                        head= (itemlist[i].attributes['product'].value)
                        service,sep,tail=head.partition(" ")
                        print ("Service : " ,service)
                    except:
                        service=""
			print ("Exception occured could not find service")
                    try:
                        version=( itemlist[i].attributes['version'].value)
                        print("version : ",version)
                        head,sep,tail=version.rpartition(".")
                        version2=head+".x"
                    except:
			version=""
			version2=""
                        print ("Exception occured could not find version") 
                    if optn == "y" or optn=="Y":
                        if service is not "" and version is not "":
                            result=subprocess.check_output(['searchsploit','-w',service,version])
                            result2=subprocess.check_output(['searchsploit','-w',service,version2])
                    else:
                        if service is not "":
                            result=subprocess.check_output(['searchsploit','-w',service])
                            result2=subprocess.check_output(['searchsploit','-w',service])
                    print (result)
                    print (result2)
        else:
                print ("Search Sploit was not found")
                print ("Attempting to install Searchsploit")
                pkg.mark_install()
                try:
                    cache.commit()
                except Exception, arg:
                    print (sys.stderr+" Sorry Package installation failed " + str(arg))
    except Exception,err:
        print ("Trouble Importing Module -_- Are you sure this is ubuntu?")
	print (err)
