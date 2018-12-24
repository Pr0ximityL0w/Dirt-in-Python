#!/usr/bin/env python2.7

import socket

host="irc.freenode.org"
port=6667
nick="SLEEPW∆LKR"
password="*****"
ident="*****"
realname="*****"
channel="*****"


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )
s.connect((host, port))
s.sendall("NICK %s\r\n" % nick)
s.sendall("USER %s %s bla :%s\r\n" % (ident, host, realname))
s.sendall("PRIVMSG nickserv :identify %s %s\r\n" % (nick, password))
s.send("JOIN :%s\r\n" % channel)


filetxt = open('/home/user/*****', 'a+')


try:
    while True:
        buffer = s.recv(1024)
        msg = buffer.split( )
        if msg[0] == "PING":
            s.send("PONG %s" % msg[1])


        if msg [1] == 'PRIVMSG':
            nick_name = msg[0][:msg[0].find("!")]
            message = ' '.join(msg[3:])
            filetxt.write(nick_name.lstrip(':') + ' -> ' +
                          message.lstrip(':') + '\n')
            filetxt.flush( )


        if msg[1] == 'PRIVMSG' and msg[2] == (nick) and msg[3] == ':!Shutdown':
            s.sendall("QUIT :Quit: Leaving..\r\n")
            break


finally:
    filetxt.close( )
