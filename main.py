#Import modules
import os
import platform as pl
import socket as so
import commands

#custom modules
from aka import alias

dochange = 0 #Enables or disables the changing of hostnames
mac = 'null'
currentos =  pl.system()

#Determine os and change hostname 
#Linux
if currentos == 'Linux':
	print('Du bruger Linux') 
	iface = 'wlp3s0'
	mac = commands.getoutput('cat /sys/class/net/' + iface + '/address')
 	hname = alias(mac)
	if dochange == 1:
     		#Change hostname
		os.system('sudo hostname ' + hname) #The hostname command is volatile, maybe we should consider something else?

  		#Change the hosts file
  		hostsfile = open('/etc/hosts', 'w')
        	hostsfile.write('127.0.0.1	localhost')
          	hostsfile.write('127.0.1.1	' + hname)
           	hostsfile.close()

#MacOS
elif currentos == 'Darwin': #Darwin is the name of the kernel that Apple uses for MacOS
	print('Du bruger macOS')
	iface = "en0"
	cutmac = os.popen('ifconfig ' + iface + ' |grep ether').read()
	halfmac = cutmac.rsplit(' ')
	mac = halfmac[1]
	hname = alias(mac)
	if dochange == 1:
		os.system("sudo scutil --set HostName " + hname)
#Windows
elif currentos == 'Windows':
	print("Du bruger Windows")
	mac = os.popen('wmic path win32_networkadapter where index=1 get MACAddress').read()
 	hname = alias(mac)
	if dochange == 1:
     		if so.gethostname() == hname:
			#CMD command for changing hostname
			os.system('powershell Rename-Computer -NewName -Force -Restart "' + hname + '"')

if mac != "null":
	print(mac)
 	print(hname)
else:
	print("Couldn't find MAC address")
print(so.gethostname())
