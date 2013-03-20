#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 15/06/2012

@author: scalvofe
'''
import sys, os
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import webbrowser
import threading

httpd = None
class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        createServer()

def openBrowser(html=None):
    #url = "http://127.0.0.1:8000/index.html"
    if html is not None:
        url = "http://127.0.0.1:8000/"+html
        new = 2 # open in a new tab, if possible
        webbrowser.open(url,new=new)
        print "browser opened on "+url
        

def createServer():
    global httpd
    HandlerClass = SimpleHTTPRequestHandler
    ServerClass  = BaseHTTPServer.HTTPServer
    Protocol     = "HTTP/1.0"
    
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('127.0.0.1', port)
    
    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)
    
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "... you can go to:"
    print "http://127.0.0.1:%s" % port
    httpd.serve_forever()



def start():
    t = ServerThread()
    t.start()
    print "started"
    
def kill_server():
    global httpd
    httpd.shutdown()
    httpd.server_close()


if __name__ == "__main__":
    start()

