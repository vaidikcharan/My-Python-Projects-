import psutil
import platform
import time

ram = psutil.virtual_memory()#used to print RAM info.
disk = psutil.disk_usage('/')#Disk usage nikalne ke liye.

print(f"Operating System: {platform.system()} {platform.release()}")#OS ka naam (Windows/Linux/Darwin), OS version
print(platform.version()) #Detailed version number
print(platform.machine())#Architecture (jaise 'AMD64')
print(platform.node())#Computer/network ka naam
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"CPU Cores: {psutil.cpu_count()}")

print("-"*30)

print(f"Total RAM: {ram.total/(1024**3):.2f}GB.")
print(f"Used RAM: {ram.used/(1024**3):.2f}GB.")
print(f"RAM usage: {ram.percent}%")#Dot used to print specific part of avmem(namedtupple)

print("-"*30)

print(f"Total Disk Space: {disk.total/(1024**3):.2f}GB.")
print(f"Used Disk: {disk.used/(1024**3):.2f}GB.")
print(f"Disk Usage: {disk.percent:.2f}%")

try:
    while True:
        print("Updating...")
        time.sleep(1)
except KeyboardInterrupt:
    print("Monitor stoped.")