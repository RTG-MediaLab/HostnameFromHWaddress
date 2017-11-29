#Import modules
import os
import subprocess as sp
import platform as pl
import socket as so
import commands

dochange = 0 #Enables or disables the changing of hostnames
mac = 'null'
currentos =  pl.system()

#Determine os and change hostname 
#Linux
if currentos == 'Linux':
	print('Du bruger Linux') 
	iface = 'wlp3s0'
	mac = commands.getoutput('cat /sys/class/net/' + iface + '/address')
	if dochange == 0:
		os.system('sudo hostname ' + mac)
#MacOS
elif currentos == 'Darwin': #Darwin is the name of the kernel that Apple uses for MacOS
	print('Du bruger macOS')
	iface = "en1"
	cutmac = os.popen('ifconfig ' + iface + ' |grep ether').read()
	halfmac = cutmac.rsplit(' ')
	mac = halfmac[1]
	if dochange == 0:
		os.system("sudo scutil --set HostName " + mac)
#Windows
elif currentos == 'Windows':
	print("Du bruger Windows")
	mac = os.popen('').read()
	if dochange == 0:
		#CMD command for changing hostname
		os.system('wmic computersystem where name="%COMPUTERNAME%" call rename name="' +mac + '"')
		print(mac)
if mac != "null":
	print(mac)
else:
	print("Kunne ikke finde MAC address")
print(so.gethostname())
