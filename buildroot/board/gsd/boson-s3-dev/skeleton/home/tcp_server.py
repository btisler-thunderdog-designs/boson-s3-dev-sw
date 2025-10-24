import os
import sys
import time
import json
import socket 
import threading 

os.system("python3 /var/www/cgi-bin/getCamera_info.py")

bind_ip = "127.0.0.0" 
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((bind_ip, bind_port)) 
# we tell the server to start listening with 
# a maximum backlog of connections set to 5
server.listen(5) 

print(f"[+] Listening on port {bind_ip} : {bind_port}")                            

#client handling thread
def handle_client(client_socket): 
    #printing what the client sends 
    request = client_socket.recv(1024) 
    print(f"[+] Recieved: {request}") 

    JV = request.decode()
    print(JV)
    JX = json.loads(JV)

    command = JX["command"]
    print(command)

    if command == 'set':
        user = JX["user"]
        pwd = JX["pwd"]
        os.system(f"echo \"{user}:{pwd}\" > /etc/lighttpd/.lighttpd_plain_passwd")
        client_socket.send("User and Password Set".encode()) 
        client_socket.close()

    if command == 'resetServer':
        os.system("systemctl restart lighttpd")
        client_socket.send("Server Restarted".encode()) 
        client_socket.close()

    if command == 'resetCamera':
        os.system("echo 0 | sudo tee /sys/class/leds/boson:rst/brightness ")
        time.sleep(1)
        os.system("echo 1 | sudo tee /sys/class/leds/boson:rst/brightness ")
        client_socket.send("Camera Reset".encode()) 
        client_socket.close()
    
    if command == 'resetSystem':
        os.system("reboot")
        client_socket.send("System Reset".encode()) 
        client_socket.close()
    
    if command == 'resetStream':
        os.system("systemctl restart mediamtx")
        client_socket.send("Stream Reset".encode()) 
        client_socket.close()

while True: 
    # When a client connects we receive the 
    # client socket into the client variable, and 
    # the remote connection details into the addr variable
    client, addr = server.accept() 
    print(f"[+] Accepted connection from: {addr[0]}:{addr[1]}")
    #spin up our client thread to handle the incoming data 
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
