import os

#os.system("Get-WmiObject win32_networkadapterconfiguration  > networkconfiguration.txt")
os.system('powershell "Get-WmiObject win32_networkadapterconfiguration | select description, macaddress > networkconfiguration.txt"')

#f = open("networkconfiguration.txt", "r")
with open("networkconfiguration.txt", "rb") as ssss:
    for line in ssss:
        #print line.strip()
        if "Broadcom NetX" in line.decode("UCS-2"):
            #print 4444444
            print line.strip().split()[-1]
    ssss.close()


