import os
import sys
import time
import datetime

def log_(Text,LOGfile):
    f = open(LOGfile,"a+", encoding="UTF-8")
    f = open(LOGfile,"r+", encoding="UTF-8")
    fl = f.readlines()
    if fl == None:
        non = ""
    else:
        non = "\n"
    f = open(LOGfile,"a+", encoding="UTF-8")
    f.write(non+str(datetime.datetime.now())+ "  " + Text)
    f.close()

