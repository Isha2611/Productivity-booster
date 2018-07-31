from datetime import datetime as dt
import time
import platform

if platform.system() in ['Darwin','Linux']:
    host_file = "/etc/hosts"
elif platform.system() == 'Windows':
    host_file = r"C:\Windows\System32\drivers\etc\hosts"

redirect = '127.0.0.1'
websites_to_be_blocked = ['www.facebook.com','facebook.com','www.quora.com','quora.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Working Hours...")
        with open(host_file,'r+') as f:
            content = f.read()
            for w in websites_to_be_blocked:
                line = redirect+' '+w+"\n"
                if line in content:
                    pass
                else:
                    f.write(line)
    else:
        print("Fun time...")
        with open(host_file,'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(w in line for w in websites_to_be_blocked):
                    f.write(line)
            f.truncate()
    time.sleep(5)
