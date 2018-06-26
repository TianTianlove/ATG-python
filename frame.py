# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ATG", pos=wx.DefaultPosition, size=wx.Size(903, 667),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menubar1.Append(self.m_menu1, u"File")

        self.m_menu2 = wx.Menu()
        self.m_menu11 = wx.Menu()
        self.m_menu2.AppendSubMenu(self.m_menu11, u"About")

        self.m_menubar1.Append(self.m_menu2, u"Help")

        self.SetMenuBar(self.m_menubar1)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_splitter2 = wx.SplitterWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.m_splitter2.Bind(wx.EVT_IDLE, self.m_splitter2OnIdle)

        self.m_splitter2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))

        self.m_panel1 = wx.Panel(self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        self.m_panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_splitter7 = wx.SplitterWindow(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.m_splitter7.Bind(wx.EVT_IDLE, self.m_splitter7OnIdle)

        self.m_panel3 = wx.Panel(self.m_splitter7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Device Control", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer4.Add(self.m_staticText1, 0, wx.ALL, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer6.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textID = wx.TextCtrl(self.m_panel3, wx.ID_ANY, u"ED000200", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_textID, 1, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"BR:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)

        m_choice_BRChoices = [u"10", u"20", u"50", u"100", u"125", u"250", u"500", u"800", u"1000"]
        self.m_choice_BR = wx.Choice(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_BRChoices,
                                     0)
        self.m_choice_BR.SetSelection(5)
        bSizer7.Add(self.m_choice_BR, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Kbps", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer7.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer4.Add(bSizer7, 0, wx.EXPAND, 5)

        self.m_buttonOpen = wx.Button(self.m_panel3, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_buttonOpen, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_buttonTest = wx.Button(self.m_panel3, wx.ID_ANY, u"Send Test", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_buttonTest.Enable(False)

        bSizer4.Add(self.m_buttonTest, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        self.m_panel4 = wx.Panel(self.m_splitter7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4.SetSizer(bSizer14)
        self.m_panel4.Layout()
        bSizer14.Fit(self.m_panel4)
        self.m_splitter7.SplitHorizontally(self.m_panel3, self.m_panel4, 237)
        bSizer3.Add(self.m_splitter7, 1, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer3)
        self.m_panel1.Layout()
        bSizer3.Fit(self.m_panel1)
        self.m_panel2 = wx.Panel(self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer61 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel7 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_btn_start_tracing = wx.Button(self.m_panel7, wx.ID_ANY, u"Start Tracing", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_btn_start_tracing.Enable(False)

        bSizer18.Add(self.m_btn_start_tracing, 0, wx.ALL, 5)

        self.m_btn_pause_tracing = wx.Button(self.m_panel7, wx.ID_ANY, u"Pause Tracing", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_btn_pause_tracing.Enable(False)

        bSizer18.Add(self.m_btn_pause_tracing, 0, wx.ALL, 5)

        self.m_btn_stop_tracing = wx.Button(self.m_panel7, wx.ID_ANY, u"Stop Tracing", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_btn_stop_tracing.Enable(False)

        bSizer18.Add(self.m_btn_stop_tracing, 0, wx.ALL, 5)

        bSizer10.Add(bSizer18, 0, wx.EXPAND, 5)

        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_cb_savedb = wx.CheckBox(self.m_panel7, wx.ID_ANY, u"Save as DB", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.m_cb_savedb, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_cb_savelog = wx.CheckBox(self.m_panel7, wx.ID_ANY, u"Save as Log", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.m_cb_savelog, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_dP_db = wx.DirPickerCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                        wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        bSizer20.Add(self.m_dP_db, 1, wx.ALL, 5)

        bSizer10.Add(bSizer20, 0, wx.EXPAND, 5)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_cb_time_mode = wx.CheckBox(self.m_panel7, wx.ID_ANY, u"△t", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19.Add(self.m_cb_time_mode, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tracelist_modeChoices = [u"Chronological", u"Fixed"]
        self.m_choice_tracelist_mode = wx.Choice(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 m_choice_tracelist_modeChoices, 0)
        self.m_choice_tracelist_mode.SetSelection(0)
        bSizer19.Add(self.m_choice_tracelist_mode, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_btn_clean_up = wx.Button(self.m_panel7, wx.ID_ANY, u"Clean up", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19.Add(self.m_btn_clean_up, 0, wx.ALL, 5)

        bSizer10.Add(bSizer19, 0, wx.EXPAND, 5)

        self.m_listCtrl1 = wx.ListCtrl(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer10.Add(self.m_listCtrl1, 1, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.m_panel7.SetSizer(bSizer10)
        self.m_panel7.Layout()
        bSizer10.Fit(self.m_panel7)
        self.m_notebook1.AddPage(self.m_panel7, u"Trace", False)
        self.m_panel12 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer101 = wx.BoxSizer(wx.VERTICAL)

        bSizer181 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_btn_start_player = wx.Button(self.m_panel12, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_btn_start_player.Enable(False)

        bSizer181.Add(self.m_btn_start_player, 0, wx.ALL, 5)

        self.m_btn_pause_player = wx.Button(self.m_panel12, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_btn_pause_player.Enable(False)

        bSizer181.Add(self.m_btn_pause_player, 0, wx.ALL, 5)

        self.m_btn_stop_player = wx.Button(self.m_panel12, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_btn_stop_player.Enable(False)

        bSizer181.Add(self.m_btn_stop_player, 0, wx.ALL, 5)

        bSizer101.Add(bSizer181, 0, wx.EXPAND, 5)

        bSizer201 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_filePicker_player = wx.FilePickerCtrl(self.m_panel12, wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                     u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer201.Add(self.m_filePicker_player, 1, wx.ALL, 5)

        bSizer101.Add(bSizer201, 0, wx.EXPAND, 5)

        bSizer44 = wx.BoxSizer(wx.VERTICAL)

        bSizer45 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText24 = wx.StaticText(self.m_panel12, wx.ID_ANY, u"Loop:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        bSizer45.Add(self.m_staticText24, 0, wx.ALL, 5)

        self.m_textCtrl_player_loop = wx.TextCtrl(self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        bSizer45.Add(self.m_textCtrl_player_loop, 0, wx.ALL, 5)

        bSizer44.Add(bSizer45, 0, wx.EXPAND, 5)

        self.m_staticText23 = wx.StaticText(self.m_panel12, wx.ID_ANY, u"State:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        bSizer44.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.m_staticText_count = wx.StaticText(self.m_panel12, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_count.Wrap(-1)
        bSizer44.Add(self.m_staticText_count, 0, wx.ALL, 5)

        bSizer101.Add(bSizer44, 1, wx.EXPAND, 5)

        self.m_panel12.SetSizer(bSizer101)
        self.m_panel12.Layout()
        bSizer101.Fit(self.m_panel12)
        self.m_notebook1.AddPage(self.m_panel12, u"Playback", False)
        self.m_panel9 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer37 = wx.BoxSizer(wx.VERTICAL)

        self.m_radioBtnConfig = wx.RadioButton(self.m_panel9, wx.ID_ANY, u"Config File", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer37.Add(self.m_radioBtnConfig, 0, wx.ALL, 5)

        self.m_filePicker_config = wx.FilePickerCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                     wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer37.Add(self.m_filePicker_config, 1, wx.ALL | wx.EXPAND, 5)

        self.m_gauge1 = wx.Gauge(self.m_panel9, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        bSizer37.Add(self.m_gauge1, 0, wx.ALL | wx.EXPAND, 5)

        bSizer12.Add(bSizer37, 0, wx.EXPAND, 5)

        self.m_staticline22 = wx.StaticLine(self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer12.Add(self.m_staticline22, 0, wx.EXPAND | wx.ALL, 5)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer15.SetMinSize(wx.Size(-1, 80))
        self.m_radioBtnDos = wx.RadioButton(self.m_panel9, wx.ID_ANY, u"DoS Attack", wx.Point(30, -1), wx.Size(200, -1),
                                            0)
        bSizer15.Add(self.m_radioBtnDos, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtnFuzz = wx.RadioButton(self.m_panel9, wx.ID_ANY, u"Fuzzing Attack", wx.Point(30, -1),
                                             wx.DefaultSize, 0)
        bSizer15.Add(self.m_radioBtnFuzz, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText351 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText351.Wrap(-1)
        bSizer15.Add(self.m_staticText351, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_FuzzID = wx.TextCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer15.Add(self.m_textCtrl_FuzzID, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer12.Add(bSizer15, 0, wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer12.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        bSizer16.SetMinSize(wx.Size(-1, 80))
        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_radioBtnSpoof = wx.RadioButton(self.m_panel9, wx.ID_ANY, u"Spoofing Attack", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_radioBtnSpoof.Enable(False)

        bSizer22.Add(self.m_radioBtnSpoof, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button_analysis1 = wx.Button(self.m_panel9, wx.ID_ANY, u"Analyze", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_analysis1.Enable(False)

        bSizer22.Add(self.m_button_analysis1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer211 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText111 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"Analysis result:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        bSizer211.Add(self.m_staticText111, 0, wx.ALL, 5)

        m_listBox_spoof_attackChoices = []
        self.m_listBox_spoof_attack = wx.ListBox(self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 150),
                                                 m_listBox_spoof_attackChoices, 0 | wx.VSCROLL)
        bSizer211.Add(self.m_listBox_spoof_attack, 1, wx.ALL | wx.EXPAND, 5)

        bSizer22.Add(bSizer211, 1, wx.EXPAND, 5)

        bSizer16.Add(bSizer22, 1, wx.EXPAND, 5)

        bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox_a_fd = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"Fixed  Data", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_checkBox_a_fd.SetValue(True)
        bSizer23.Add(self.m_checkBox_a_fd, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer2 = wx.GridSizer(1, 8, 0, 0)

        self.m_textCtrl_fixdata1 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata1, 0, wx.ALL, 5)

        self.m_textCtrl_fixdata2 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata2, 0, wx.ALL, 5)

        self.m_textCtrl_fixdata3 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata3, 0, wx.ALL, 5)

        self.m_textCtrl_fixdata4 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata4, 0, wx.ALL, 5)

        self.m_textCtrl_fixdata5 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata5, 0, wx.ALL, 5)

        self.m_textCtrl_fixdata6 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata6, 0, wx.ALL, 5)

        self.m_textCtrl_fixdata7 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata7, 0, wx.ALL, 5)

        self.m_textCtrl_fixdata8 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(35, -1), 0)
        gSizer2.Add(self.m_textCtrl_fixdata8, 0, wx.ALL, 5)

        bSizer23.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer16.Add(bSizer23, 0, wx.EXPAND, 5)

        bSizer25 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox_a_do = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"Data Offset", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        bSizer25.Add(self.m_checkBox_a_do, 0, wx.ALL, 5)

        gSizer1 = wx.GridSizer(1, 8, 0, 0)

        self.m_checkBox_offset1 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset1, 0, wx.ALL, 5)

        self.m_checkBox_offset2 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset2, 0, wx.ALL, 5)

        self.m_checkBox_offset3 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset3, 0, wx.ALL, 5)

        self.m_checkBox_offset4 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset4, 0, wx.ALL, 5)

        self.m_checkBox_offset5 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset5, 0, wx.ALL, 5)

        self.m_checkBox_offset6 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset6, 0, wx.ALL, 5)

        self.m_checkBox_offset7 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset7, 0, wx.ALL, 5)

        self.m_checkBox_offset8 = wx.CheckBox(self.m_panel9, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox_offset8, 0, wx.ALL, 5)

        bSizer25.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer16.Add(bSizer25, 0, wx.EXPAND, 5)

        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText141 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"Frequency", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText141.Wrap(-1)
        bSizer26.Add(self.m_staticText141, 0, wx.ALL, 5)

        self.m_slider_fuzzing_f = wx.Slider(self.m_panel9, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.Size(300, -1),
                                            wx.SL_HORIZONTAL)
        bSizer26.Add(self.m_slider_fuzzing_f, 0, wx.ALL, 5)

        self.m_staticText142 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"Every 100 insert", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText142.Wrap(-1)
        bSizer26.Add(self.m_staticText142, 0, wx.ALL, 5)

        self.m_text_fuzzing_fv = wx.StaticText(self.m_panel9, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_text_fuzzing_fv.Wrap(-1)
        bSizer26.Add(self.m_text_fuzzing_fv, 0, wx.ALL, 5)

        bSizer16.Add(bSizer26, 0, 0, 5)

        bSizer12.Add(bSizer16, 0, wx.EXPAND, 5)

        self.m_staticline3 = wx.StaticLine(self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer12.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_attack_start = wx.Button(self.m_panel9, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize,
                                               0)
        self.m_button_attack_start.Enable(False)

        bSizer21.Add(self.m_button_attack_start, 0, wx.ALL, 5)

        self.m_button_attack_stop = wx.Button(self.m_panel9, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_attack_stop.Enable(False)

        bSizer21.Add(self.m_button_attack_stop, 0, wx.ALL, 5)

        bSizer12.Add(bSizer21, 0, wx.ALIGN_RIGHT, 5)

        self.m_panel9.SetSizer(bSizer12)
        self.m_panel9.Layout()
        bSizer12.Fit(self.m_panel9)
        self.m_notebook1.AddPage(self.m_panel9, u"Attack", True)
        self.m_panel8 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Select File:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        self.m_staticText6.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer11.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_filePicker_matrix_imput = wx.FilePickerCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                           u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                                           wx.FLP_DEFAULT_STYLE)
        bSizer11.Add(self.m_filePicker_matrix_imput, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticline6 = wx.StaticLine(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer11.Add(self.m_staticline6, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"OutPut File:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer11.Add(self.m_staticText12, 0, wx.ALL, 5)

        bSizer162 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        bSizer162.Add(self.m_staticText13, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_matrix_output_name = wx.TextCtrl(self.m_panel8, wx.ID_ANY, u"target", wx.DefaultPosition,
                                                         wx.Size(200, -1), 0)
        bSizer162.Add(self.m_textCtrl_matrix_output_name, 0, wx.ALL, 5)

        m_choice_matrix_output_formatChoices = [u".dbc", u".dbf", u".kcd", u".xls", u".xlsx", u".json", u".arxml",
                                                u".yaml", u".sym", u".xml"]
        self.m_choice_matrix_output_format = wx.Choice(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                       m_choice_matrix_output_formatChoices, 0)
        self.m_choice_matrix_output_format.SetSelection(0)
        bSizer162.Add(self.m_choice_matrix_output_format, 0, wx.ALL, 5)

        bSizer11.Add(bSizer162, 0, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText14 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Path:  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        bSizer17.Add(self.m_staticText14, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_dirPicker_matrix_output_path = wx.DirPickerCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString,
                                                               u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
                                                               wx.DIRP_DEFAULT_STYLE)
        bSizer17.Add(self.m_dirPicker_matrix_output_path, 1, wx.ALL, 5)

        bSizer11.Add(bSizer17, 0, wx.EXPAND, 5)

        self.m_staticline8 = wx.StaticLine(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer11.Add(self.m_staticline8, 0, wx.EXPAND | wx.ALL, 5)

        bSizer31 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_cb_for_IDS = wx.CheckBox(self.m_panel8, wx.ID_ANY, u"For IDS", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.m_cb_for_IDS, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_btn_convert = wx.Button(self.m_panel8, wx.ID_ANY, u"Convert", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.m_btn_convert, 0, wx.ALL, 5)

        bSizer11.Add(bSizer31, 0, wx.EXPAND, 5)

        self.m_staticline10 = wx.StaticLine(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer11.Add(self.m_staticline10, 0, wx.EXPAND | wx.ALL, 5)

        bSizer151 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText71 = wx.StaticText(self.m_panel8, wx.ID_ANY,
                                            u"supported file formats for import:\n  .dbc candb / Vector\n  .dbf Busmaster (open source!)\n  .kcd kayak (open source!)\n  .arxml autosar system description\n  .yaml dump of the python object\n  .xls(x) \n  .sym peak pcan can description",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        bSizer151.Add(self.m_staticText71, 0, wx.ALL, 5)

        self.m_staticline5 = wx.StaticLine(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        self.m_staticline5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))
        self.m_staticline5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))

        bSizer151.Add(self.m_staticline5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self.m_panel8, wx.ID_ANY,
                                            u"supported file formats for export:\n  .dbc\n  .dbf\n  .kcd\n  .xls(x)\n  .json Canard (open source!)\n  .arxml (very basic implementation)\n  .yaml (dump of the python object)\n  .sym\n  .xml fibex",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        bSizer151.Add(self.m_staticText11, 0, wx.ALL, 5)

        bSizer11.Add(bSizer151, 0, wx.EXPAND, 5)

        self.m_panel8.SetSizer(bSizer11)
        self.m_panel8.Layout()
        bSizer11.Fit(self.m_panel8)
        self.m_notebook1.AddPage(self.m_panel8, u"CAN Matrix", False)
        self.m_panel10 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer111 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText61 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"Select File:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        self.m_staticText61.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer111.Add(self.m_staticText61, 0, wx.ALL, 5)

        self.m_filePicker_data_imput = wx.FilePickerCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                         u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                                         wx.FLP_DEFAULT_STYLE)
        bSizer111.Add(self.m_filePicker_data_imput, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticline61 = wx.StaticLine(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer111.Add(self.m_staticline61, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText121 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"OutPut File:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText121.Wrap(-1)
        self.m_staticText121.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer111.Add(self.m_staticText121, 0, wx.ALL, 5)

        bSizer1621 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText131 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText131.Wrap(-1)
        bSizer1621.Add(self.m_staticText131, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_data_output_name = wx.TextCtrl(self.m_panel10, wx.ID_ANY, u"target", wx.DefaultPosition,
                                                       wx.Size(200, -1), 0)
        bSizer1621.Add(self.m_textCtrl_data_output_name, 0, wx.ALL, 5)

        m_choice_data_output_formatChoices = [u".csv", u".log"]
        self.m_choice_data_output_format = wx.Choice(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                     m_choice_data_output_formatChoices, 0)
        self.m_choice_data_output_format.SetSelection(0)
        bSizer1621.Add(self.m_choice_data_output_format, 0, wx.ALL, 5)

        bSizer111.Add(bSizer1621, 0, wx.EXPAND, 5)

        bSizer171 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText143 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"Path:  ", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText143.Wrap(-1)
        bSizer171.Add(self.m_staticText143, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_dirPicker_data_output_path = wx.DirPickerCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString,
                                                             u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
                                                             wx.DIRP_DEFAULT_STYLE)
        bSizer171.Add(self.m_dirPicker_data_output_path, 1, wx.ALL, 5)

        bSizer111.Add(bSizer171, 0, wx.EXPAND, 5)

        self.m_staticline81 = wx.StaticLine(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer111.Add(self.m_staticline81, 0, wx.EXPAND | wx.ALL, 5)

        self.m_btn_convert_data = wx.Button(self.m_panel10, wx.ID_ANY, u"Convert", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        bSizer111.Add(self.m_btn_convert_data, 0, wx.ALL, 5)

        self.m_staticline101 = wx.StaticLine(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        bSizer111.Add(self.m_staticline101, 0, wx.EXPAND | wx.ALL, 5)

        bSizer1511 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText711 = wx.StaticText(self.m_panel10, wx.ID_ANY,
                                             u"supported file formats for import:\n  .db\n  .log\n  .csv",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText711.Wrap(-1)
        bSizer1511.Add(self.m_staticText711, 0, wx.ALL, 5)

        self.m_staticline51 = wx.StaticLine(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_VERTICAL)
        self.m_staticline51.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))
        self.m_staticline51.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))

        bSizer1511.Add(self.m_staticline51, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText112 = wx.StaticText(self.m_panel10, wx.ID_ANY,
                                             u"supported file formats for export:\n  .csv\n  .log", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText112.Wrap(-1)
        bSizer1511.Add(self.m_staticText112, 0, wx.ALL, 5)

        bSizer111.Add(bSizer1511, 0, wx.EXPAND, 5)

        self.m_panel10.SetSizer(bSizer111)
        self.m_panel10.Layout()
        bSizer111.Fit(self.m_panel10)
        self.m_notebook1.AddPage(self.m_panel10, u"Dataset conversion", False)
        self.m_panel11 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer1111 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText611 = wx.StaticText(self.m_panel11, wx.ID_ANY, u"Select File:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText611.Wrap(-1)
        self.m_staticText611.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer1111.Add(self.m_staticText611, 0, wx.ALL, 5)

        self.m_filePicker_da_imput = wx.FilePickerCtrl(self.m_panel11, wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                       u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer1111.Add(self.m_filePicker_da_imput, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticline611 = wx.StaticLine(self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        bSizer1111.Add(self.m_staticline611, 0, wx.EXPAND | wx.ALL, 5)

        self.m_btn_da_analyze = wx.Button(self.m_panel11, wx.ID_ANY, u"Analyze", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1111.Add(self.m_btn_da_analyze, 0, wx.ALL, 5)

        self.m_staticText1211 = wx.StaticText(self.m_panel11, wx.ID_ANY, u"Messages:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1211.Wrap(-1)
        self.m_staticText1211.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer1111.Add(self.m_staticText1211, 0, wx.ALL, 5)

        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox(self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 120), m_listBox2Choices,
                                     wx.LB_MULTIPLE)
        bSizer1111.Add(self.m_listBox2, 0, wx.ALL | wx.EXPAND, 5)

        bSizer46 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_radioBtn4 = wx.RadioButton(self.m_panel11, wx.ID_ANY, u"Interval", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer46.Add(self.m_radioBtn4, 0, wx.ALL, 5)

        self.m_radioBtn5 = wx.RadioButton(self.m_panel11, wx.ID_ANY, u"Clock skew", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        bSizer46.Add(self.m_radioBtn5, 0, wx.ALL, 5)

        bSizer1111.Add(bSizer46, 0, 0, 5)

        self.m_staticline1011 = wx.StaticLine(self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.LI_HORIZONTAL)
        bSizer1111.Add(self.m_staticline1011, 0, wx.EXPAND | wx.ALL, 5)

        self.m_btn_figure = wx.Button(self.m_panel11, wx.ID_ANY, u"Generate Figure", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bSizer1111.Add(self.m_btn_figure, 0, wx.ALL, 5)

        self.m_panel11.SetSizer(bSizer1111)
        self.m_panel11.Layout()
        bSizer1111.Fit(self.m_panel11)
        self.m_notebook1.AddPage(self.m_panel11, u"DA", False)
        self.m_panel111 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        bSizer11111 = wx.BoxSizer(wx.VERTICAL)

        bSizer42 = wx.BoxSizer(wx.VERTICAL)

        gSizer3 = wx.GridSizer(2, 6, 0, 0)

        self.m_staticText33 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        gSizer3.Add(self.m_staticText33, 0, wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText34.Wrap(-1)
        gSizer3.Add(self.m_staticText34, 0, wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Startbit:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gSizer3.Add(self.m_staticText35, 0, wx.ALL, 5)

        self.m_staticText38 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Length:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText38.Wrap(-1)
        gSizer3.Add(self.m_staticText38, 0, wx.ALL, 5)

        self.m_staticText36 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Factor:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText36.Wrap(-1)
        gSizer3.Add(self.m_staticText36, 0, wx.ALL, 5)

        self.m_staticText39 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Offset:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText39.Wrap(-1)
        gSizer3.Add(self.m_staticText39, 0, wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self.m_panel111, wx.ID_ANY, u"0x302", wx.DefaultPosition, wx.Size(70, -1), 0)
        gSizer3.Add(self.m_textCtrl13, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self.m_panel111, wx.ID_ANY, u"980", wx.DefaultPosition, wx.Size(70, -1), 0)
        gSizer3.Add(self.m_textCtrl14, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(self.m_panel111, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size(70, -1), 0)
        gSizer3.Add(self.m_textCtrl15, 0, wx.ALL, 5)

        self.m_textCtrl16 = wx.TextCtrl(self.m_panel111, wx.ID_ANY, u"16", wx.DefaultPosition, wx.Size(70, -1), 0)
        gSizer3.Add(self.m_textCtrl16, 0, wx.ALL, 5)

        self.m_textCtrl17 = wx.TextCtrl(self.m_panel111, wx.ID_ANY, u"0.25", wx.DefaultPosition, wx.Size(70, -1), 0)
        gSizer3.Add(self.m_textCtrl17, 0, wx.ALL, 5)

        self.m_textCtrl18 = wx.TextCtrl(self.m_panel111, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(70, -1), 0)
        gSizer3.Add(self.m_textCtrl18, 0, wx.ALL, 5)

        bSizer42.Add(gSizer3, 1, wx.EXPAND, 5)

        bSizer43 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText40 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText40.Wrap(-1)
        bSizer43.Add(self.m_staticText40, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl19 = wx.TextCtrl(self.m_panel111, wx.ID_ANY, u"EngineSpeed", wx.DefaultPosition,
                                        wx.Size(150, -1), 0)
        bSizer43.Add(self.m_textCtrl19, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn10 = wx.RadioButton(self.m_panel111, wx.ID_ANY, u"Motorola", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        bSizer43.Add(self.m_radioBtn10, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn101 = wx.RadioButton(self.m_panel111, wx.ID_ANY, u"Intel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer43.Add(self.m_radioBtn101, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button21 = wx.Button(self.m_panel111, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer43.Add(self.m_button21, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer42.Add(bSizer43, 1, wx.EXPAND, 5)

        bSizer11111.Add(bSizer42, 1, wx.EXPAND, 5)

        self.m_staticline6111 = wx.StaticLine(self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.LI_HORIZONTAL)
        bSizer11111.Add(self.m_staticline6111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText12111 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Signals:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText12111.Wrap(-1)
        self.m_staticText12111.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer11111.Add(self.m_staticText12111, 0, wx.ALL, 5)

        m_listBox21Choices = [u"BrakePadelStatus, ID:0x302, Value:1, Startbit:37, Length:2, Factor:1, Offset:0",
                              u"EngineSpeed, ID:0x302, Value:980, Startbit:8, Length:16, Factor:0.25, Offset:0",
                              wx.EmptyString]
        self.m_listBox21 = wx.ListBox(self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 110),
                                      m_listBox21Choices, wx.LB_MULTIPLE)
        bSizer11111.Add(self.m_listBox21, 0, wx.ALL | wx.EXPAND, 5)

        self.m_btn_figure1 = wx.Button(self.m_panel111, wx.ID_ANY, u"Generate frames", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer11111.Add(self.m_btn_figure1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_staticline101111 = wx.StaticLine(self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                wx.LI_HORIZONTAL)
        bSizer11111.Add(self.m_staticline101111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText121111 = wx.StaticText(self.m_panel111, wx.ID_ANY, u"Result:", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText121111.Wrap(-1)
        self.m_staticText121111.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        bSizer11111.Add(self.m_staticText121111, 0, wx.ALL, 5)

        m_listBox211Choices = [u"ID:0x302, 00 0F 50 00 04 00 00 00"]
        self.m_listBox211 = wx.ListBox(self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 110),
                                       m_listBox211Choices, wx.LB_MULTIPLE)
        bSizer11111.Add(self.m_listBox211, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel111.SetSizer(bSizer11111)
        self.m_panel111.Layout()
        bSizer11111.Fit(self.m_panel111)
        self.m_notebook1.AddPage(self.m_panel111, u"Package frame", False)

        bSizer61.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticline21 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer61.Add(self.m_staticline21, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer61)
        self.m_panel2.Layout()
        bSizer61.Fit(self.m_panel2)
        self.m_splitter2.SplitVertically(self.m_panel1, self.m_panel2, 224)
        bSizer2.Add(self.m_splitter2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, 0 | wx.NO_BORDER, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.m_buttonOpen.Bind(wx.EVT_BUTTON, self.clickOpen)
        self.m_buttonTest.Bind(wx.EVT_BUTTON, self.clickTest)
        self.m_btn_start_tracing.Bind(wx.EVT_BUTTON, self.onclick_start_tracing)
        self.m_btn_pause_tracing.Bind(wx.EVT_BUTTON, self.onclick_pause_tracing)
        self.m_btn_stop_tracing.Bind(wx.EVT_BUTTON, self.onclick_stop_tracing)
        self.m_cb_time_mode.Bind(wx.EVT_CHECKBOX, self.onclick_cb_trace_time_mode)
        self.m_choice_tracelist_mode.Bind(wx.EVT_CHOICE, self.onclick_choice_tracelist_mode)
        self.m_btn_clean_up.Bind(wx.EVT_BUTTON, self.onclick_trace_clean_up)
        self.m_btn_start_player.Bind(wx.EVT_BUTTON, self.onclick_start_play)
        self.m_btn_pause_player.Bind(wx.EVT_BUTTON, self.onclick_pause_play)
        self.m_btn_stop_player.Bind(wx.EVT_BUTTON, self.onclick_stop_play)
        self.m_textCtrl_player_loop.Bind(wx.EVT_TEXT, self.on_text_enter_player)
        self.m_button_analysis1.Bind(wx.EVT_BUTTON, self.onclick_btn_fuzzing_attack)
        self.m_checkBox_a_fd.Bind(wx.EVT_CHECKBOX, self.on_check_box_fd)
        self.m_textCtrl_fixdata1.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd1)
        self.m_textCtrl_fixdata2.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd2)
        self.m_textCtrl_fixdata3.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd3)
        self.m_textCtrl_fixdata4.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd4)
        self.m_textCtrl_fixdata5.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd5)
        self.m_textCtrl_fixdata6.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd6)
        self.m_textCtrl_fixdata7.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd7)
        self.m_textCtrl_fixdata8.Bind(wx.EVT_TEXT, self.on_text_enter_at_fixd8)
        self.m_checkBox_a_do.Bind(wx.EVT_CHECKBOX, self.on_check_box_do)
        self.m_slider_fuzzing_f.Bind(wx.EVT_SCROLL, self.on_fuzzing_fre_change)
        self.m_button_attack_start.Bind(wx.EVT_BUTTON, self.onclick_attack_start)
        self.m_button_attack_stop.Bind(wx.EVT_BUTTON, self.onclick_attack_stop)
        self.m_btn_convert.Bind(wx.EVT_BUTTON, self.onclick_convert)
        self.m_btn_convert_data.Bind(wx.EVT_BUTTON, self.onclick_data_convert)
        self.m_btn_da_analyze.Bind(wx.EVT_BUTTON, self.onclick_da_analye)
        self.m_btn_figure.Bind(wx.EVT_BUTTON, self.onclick_da_generate)
        self.m_btn_figure1.Bind(wx.EVT_BUTTON, self.onclick_da_generate)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnExit(self, event):
        event.Skip()

    def clickOpen(self, event):
        event.Skip()

    def clickTest(self, event):
        event.Skip()

    def onclick_start_tracing(self, event):
        event.Skip()

    def onclick_pause_tracing(self, event):
        event.Skip()

    def onclick_stop_tracing(self, event):
        event.Skip()

    def onclick_cb_trace_time_mode(self, event):
        event.Skip()

    def onclick_choice_tracelist_mode(self, event):
        event.Skip()

    def onclick_trace_clean_up(self, event):
        event.Skip()

    def onclick_start_play(self, event):
        event.Skip()

    def onclick_pause_play(self, event):
        event.Skip()

    def onclick_stop_play(self, event):
        event.Skip()

    def on_text_enter_player(self, event):
        event.Skip()

    def onclick_btn_fuzzing_attack(self, event):
        event.Skip()

    def on_check_box_fd(self, event):
        event.Skip()

    def on_text_enter_at_fixd1(self, event):
        event.Skip()

    def on_text_enter_at_fixd2(self, event):
        event.Skip()

    def on_text_enter_at_fixd3(self, event):
        event.Skip()

    def on_text_enter_at_fixd4(self, event):
        event.Skip()

    def on_text_enter_at_fixd5(self, event):
        event.Skip()

    def on_text_enter_at_fixd6(self, event):
        event.Skip()

    def on_text_enter_at_fixd7(self, event):
        event.Skip()

    def on_text_enter_at_fixd8(self, event):
        event.Skip()

    def on_check_box_do(self, event):
        event.Skip()

    def on_fuzzing_fre_change(self, event):
        event.Skip()

    def onclick_attack_start(self, event):
        event.Skip()

    def onclick_attack_stop(self, event):
        event.Skip()

    def onclick_convert(self, event):
        event.Skip()

    def onclick_data_convert(self, event):
        event.Skip()

    def onclick_da_analye(self, event):
        event.Skip()

    def onclick_da_generate(self, event):
        event.Skip()

    def m_splitter2OnIdle(self, event):
        self.m_splitter2.SetSashPosition(224)
        self.m_splitter2.Unbind(wx.EVT_IDLE)

    def m_splitter7OnIdle(self, event):
        self.m_splitter7.SetSashPosition(237)
        self.m_splitter7.Unbind(wx.EVT_IDLE)


