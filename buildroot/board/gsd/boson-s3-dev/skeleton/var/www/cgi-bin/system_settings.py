import os
import sys
import json
import socket
import warnings
warnings.filterwarnings("ignore", "'cgi' is deprecated", DeprecationWarning)
warnings.filterwarnings("ignore", "'cgitb' is deprecated", DeprecationWarning)
import cgi, cgitb

sys.path.append('/home/')

target_host = "127.0.0.0"
target_port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

form = cgi.FieldStorage()

action = form.getvalue("action")

if action == "set":
    user = form.getvalue("new_user")
    pwd = form.getvalue("new_pwd")

    newpwd = {
        "command":"set",
        "user":user,
        "pwd":pwd
    }  
    print(json.dumps(newpwd))

    client.send(json.dumps(newpwd).encode())
    response = client.recv(4096)
    print(response.decode())

elif action == "get":
    file = open("/etc/lighttpd/.lighttpd_plain_passwd", 'r')
    n = 1
    while 1:
         char = file.read(1)
         if char == ':':
              break
         else:
              n = n+1
    password = file.readline()
    file.close()
    file = open("/etc/lighttpd/.lighttpd_plain_passwd", 'r')
    n = n-1
    user = file.read(n)
    file.close()
    userpwd = {
        "cur_user":user,
        "cur_pwd":password
    }  
    print(json.dumps(userpwd))

elif action == "resetServer":
    command = {
        "command":"resetServer"
    }
    client.send(json.dumps(command).encode())
    response = client.recv(4096)
    print(response.decode())

elif action == "resetCamera":
    command = {
        "command":"resetCamera"
    }
    client.send(json.dumps(command).encode())
    response = client.recv(4096)
    print(response.decode())

elif action == "powerCamera":
    client.send("powerCamera".encode())
    response = client.recv(4096)
    print(response.decode())

elif action == "resetSystem":
    command = {
        "command":"resetSystem"
    }
    client.send(json.dumps(command).encode())
    response = client.recv(4096)
    print(response.decode())

elif action == "resetStream":
    command = {
        "command":"resetStream"
    }
    client.send(json.dumps(command).encode())
    response = client.recv(4096)
    print(response.decode())

