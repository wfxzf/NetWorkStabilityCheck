from ping3 import ping
import time


def csvwrite(text):
    f = open("NetWorkCheck.csv","a")
    f.write(text)
    print("write")
    f.close()



hosts = ["114.114.114.114","223.5.5.5","202.102.154.3","192.168.31.1"]
i = 0
timeout = 1
cou = 0
while True:
    print("next loop ........"+str(i))
    for host in hosts:
        if ping(host,timeout= timeout):
            if i == 600:
                csvwrite(time.strftime("%Y-%m-%d || %H:%M:%S,")+host+"access"+"\n")
                print(time.strftime("%Y-%m-%d || %H:%M:%S,")+host+"access"+"\n")
                
                i =0
        else:
            cou=cou + 1
            csvwrite(time.strftime("%Y-%m-%d || %H:%M:%S,")+"fail to connect "+host+"\n")
            print(time.strftime("%Y-%m-%d || %H:%M:%S,")+"fail to connect "+host+"\n")
    time.sleep(len(hosts)*timeout)
    if cou != 0:
        csvwrite(" , \n")
    i = i + 1
    cou = 0
