import time     #timing module
from multiprocessing import Process

myturn=True
yourturn=False
selection=""
yourselection=""
keepgoing=True
ani_started = False
tick_sec=0


def get_system_speed():
    calculating=True
    ticks=0
    ticks_per_sec=0
    start=time.time()
    then=time.time()
    print("Calculating system speed")
    while calculating:
        ticks+=1
        now=time.time()
        if int(now)>int(then):
            then=now
            print("One sec has elapsed")

        if now-start>=10:
            calculating=False
            ticks_per_sec=int(ticks/10)
            print(f"Ticks per second: {ticks_per_sec}")


    return ticks_per_sec


def listenforinput():
    global selection
    selection=input("What to do?")
    if selection=="exit":
        global keepgoing
        keepgoing=False


def executecommand():
    print("executing user command\n")


def finishanimation():
    # global ani_started
    # ani_started=True
    # print("An animation happened\n")
    # return True
    global tick_sec
    x=0
    # tick=0
    while x<3:
        tick=0
        loopdone=False
        start=time.time()
        while not loopdone:
            tick+=1
            now=time.time()
            if now-start>= .02:
                print("did an animation")
                print(f"Tick: {tick}")
                loopdone=True
                x+=1

    return True

def switchturns():
    global myturn, yourturn
    myturn = not myturn
    yourturn = not yourturn

def executecpucommand():
    print("Cpu did something\n")


def doaistuff():
    global yourselection
    yourselection=("something")
    print("cpu is thinking\n")

# tick_sec=get_system_speed()

while keepgoing:
    if myturn:
        listenforinput()
        if selection!="":
            executecommand()
            if finishanimation():
                switchturns()
                selection=""

    if yourturn:
        doaistuff()
        if yourselection!="":
            executecpucommand()
            if finishanimation():
                switchturns()
                yourselection=""
