#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 19/03/2013
# simple_wx_server: A wx wrapper for simpleHTTPserver
# Copyright 2013 Santiago Calvo
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
#
# Contact the author: santicalvo@gmail.com

@author: santi
'''
import sys, os
import wx
import simpleserver, server_gui

#####
# Class to redirect output to textControl
#####
class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl
 
    def write(self,string=""):
        try:
            wx.CallAfter(self.out.WriteText, string)
        except wx._core.PyAssertionError:
            print "Assertion error on empty file picker." 

class serverui(server_gui.Simple_Server_Gui):
    
    def __init__(self, parent):
        server_gui.Simple_Server_Gui.__init__( self, parent)
        self.current_cwd = os.getcwd()
        self.redir = RedirectText(self.logTextControl)
        self.out = sys.stdout
        self.err = sys.stderr
        self.redirect_to_text_control(True)
        self.path = ""

    def redirect_to_text_control(self,ok):
        if ok:
            sys.stdout = self.redir
            sys.stderr = self.redir
        else:
            sys.stdout = self.out
            sys.stderr = self.err
            
    def onStart( self, event ):
        self.redirect_to_text_control(True)
        print "Trying to start the server... "
        html = ""
        print os.path.dirname(self.path)
        if self.path != "":
            os.chdir(os.path.dirname(self.path))
            html = os.path.basename(self.path)
        print "lanzo: ", os.getcwd()
        simpleserver.start()
        self.starts.Disable()
        if html != "" and (html.endswith("html") or html.endswith("htm")) :
            simpleserver.openBrowser(html)
    
    def onStop( self, event ):
        print "Trying to stop the server... "
        try:
            self.starts.Enable()
            simpleserver.kill_server()
            print "Server stopped."
        except:
            pass
        
    
    def onSave( self, event ):
        self.redirect_to_text_control(False)
        txt = self.logTextControl.GetValue()
        log_path = os.path.join(self.current_cwd, "server_messages.log")
        print log_path
        try:
            f = open(log_path, "w")
            f.write(txt)
            f.close
            self.alertMessage("log saved to "+log_path, "Guardado")
        except:
            pass
    
    def onSelected( self, event ):
        path = self.file_selector.GetPath()
        if path.endswith(".html"):
            print "selected ", self.file_selector.GetPath()
            self.path = path
        else:
            print path, " is not an html file."
    
    def alertMessage(self, txt, title = 'Message!'):
        dlg = wx.MessageDialog(self, txt,
                               title,
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        
def create_gui():
    app = wx.App(False)
    frame = serverui(None)
    frame.Show()
    app.MainLoop()
        

if __name__ == '__main__':
    create_gui()