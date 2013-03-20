#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import wx


###########################################################################
## Class Simple_Server_Gui
###########################################################################

class Simple_Server_Gui ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Simple Server", pos = wx.DefaultPosition, size = wx.Size( 409,242 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.AddGrowableRow( 1 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Seleccione archivo html", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.file_selector = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        fgSizer1.Add( self.file_selector, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Log", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        fgSizer1.Add( self.m_staticText4, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.logTextControl = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY  )
        fgSizer1.Add( self.logTextControl, 0, wx.ALL|wx.EXPAND, 5 )
        self.logTextControl.SetEditable(False)
        bSizer4.Add( fgSizer1, 1, wx.EXPAND, 5 )
        
        self.m_staticline1 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.starts = wx.Button( self.m_panel2, wx.ID_ANY, u"&Start server", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.starts, 0, wx.ALL, 5 )
        
        self.stops = wx.Button( self.m_panel2, wx.ID_ANY, u"&Stop server", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.stops, 0, wx.ALL, 5 )
        
        
        bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.slog = wx.Button( self.m_panel2, wx.ID_ANY, u"&Save log", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.slog, 0, wx.ALL, 5 )
        
        bSizer4.Add( bSizer3, 0, wx.EXPAND, 5 )
        
        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer2.Add( self.m_panel2, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.file_selector.Bind( wx.EVT_FILEPICKER_CHANGED, self.onSelected )
        self.starts.Bind( wx.EVT_BUTTON, self.onStart )
        self.stops.Bind( wx.EVT_BUTTON, self.onStop )
        self.slog.Bind( wx.EVT_BUTTON, self.onSave )
    
        # Virtual event handlers, overide them in your derived class
    def onStart( self, event ):
        event.Skip()
    
    def onStop( self, event ):
        event.Skip()
    
    def onSave( self, event ):
        event.Skip()
    def onSelected( self, event ):
        event.Skip()
    
    def __del__( self ):
        pass



