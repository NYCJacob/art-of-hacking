#!/usr/bin/python
# Author: Omar Santos @santosomar
# version 1.0
# This is a quick demonstration on how to create a
# basic TCP port scanner using python.
#####################################################################


import socket, subprocess,sys

subprocess.call('clear',shell=True)

print '''\t
   ___  __  __   _   ___ _ ___
  / _ \|  \/  | /_\ | _ ( ) __|
 | (_) | |\/| |/ _ \|   //\__ \
  \___/|_| _|_/_/_\_\_|_\ |___/
 | |  |_ _|_   _|_   _| |  | __|
 | |__ | |  | |   | | | |__| _|
 |____|___| |_|  _|_| |____|___|__
 / __|/ __| /_\ | \| | \| | __| _ \\
 \__ \ (__ / _ \| .` | .` | _||   /
 |___/\___/_/ \_\_|\_|_|\_|___|_|_\\

'''

target_ip = raw_input("\t Please enter the IP address of the target host:")
port_1 = int(raw_input("\t Enter the first port to scan:\t"))
port_2 = int (raw_input("\t Enter the last port to scan:\t"))
print "~"*50
print "\n ...scanning target now. ",target_ip
print "~"*50

try:
  for port in range(port_1,port_2):
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((target_ip,port))
    if result==0:
      print "Found open port:\t", port
    sock.close()

except KeyboardInterrupt:
  print "[!] Scan stopped by user... "
  sys.exit()

except socket.gaierror:
  print "[!] The target's hostname could not be resolved..."
  sys.exit()

except socket.error:
  print "[!] Target is unreachable..."
  sys.exit()

print "The scan is complete. Happy hacking!"
