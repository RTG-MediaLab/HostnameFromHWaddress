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
 	alias(mac)
	if dochange == 1:
     		#Change hostname
		os.system('sudo hostname ' + mac) #The hostname command is volatile, maybe we should consider something else?

  		#Change the hosts file
  		hostsfile = open('/etc/hosts', 'w')
        	hostsfile.write('127.0.0.1	localhost')
          	hostsfile.write('127.0.1.1	' + mac)
           	hostsfile.close()

#MacOS
elif currentos == 'Darwin': #Darwin is the name of the kernel that Apple uses for MacOS
	print('Du bruger macOS')
	iface = "en1"
	cutmac = os.popen('ifconfig ' + iface + ' |grep ether').read()
	halfmac = cutmac.rsplit(' ')
	mac = halfmac[1]
	alias(mac)
	if dochange == 1:
		os.system("sudo scutil --set HostName " + mac)
#Windows
elif currentos == 'Windows':
	print("Du bruger Windows")
	mac = os.popen('wmic path win32_networkadapter where index=1 get MACAddress').read()
 	alias(mac)
	if dochange == 1:
		#CMD command for changing hostname
		os.system('wmic computersystem where name="%COMPUTERNAME%" call rename name="' +mac + '"')
		print(mac)

if mac != "null":
	print(mac)
else:
	print("Couldn't find MAC address")
print(so.gethostname())
