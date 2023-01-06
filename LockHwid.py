import subprocess
import sys
import requests
import time
import os

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r =requests.get("https://pastebin.com/eyuRm4w0")

os.system('cls')

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def Main_Program():
    if hwid in r.text:
        print("\n")  
        printSlow("Load Hwid T-RexSHOP ...")
        time.sleep(1.5)
        os.system('cls')
    else:
        print("Error! HWID Not I Database!")
        print("HWID: " + hwid)
        os.system('pause')
        exit()

Main_Program()
