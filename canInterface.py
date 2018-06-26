import wx
import can
from can.interfaces.usb2can.usb2canInterface import Usb2canBus
import frame
import time
import threading
from wx.lib.pubsub import pub
import canmatrix.convert
import sqlite3
from tools import Tool
import math
import random
import csv
import matplotlib.pyplot as plt
import string
import re
import xlrd
import xml.dom.minidom as Dom
# import xml.etree.ElementTree as ET
import sched
from threading import Timer

# Manage the open status
openFlag = False
# Manage the tracing status
isStarted = False
isPlayerStarted = False

# Check the Spoofing analysis
isSpoofingAttackAnalysis = False
isSpoofingAttacked = False

isDoSAttacked = False
isFuzzAttacked = False

FuzzingAttackIDRangeStart = 0
FuzzingAttackIDRangeEnd = 0
FuzzingAttackData = [0, 0, 0, 0, 0, 0, 0, 0]
FuzzingAttackID = 0
Fuzzing_attack_mode = 1
FuzzingAttackFre = 0.1

Spoofing_attack_mode = 1
SpoofingAttackID = 0
SpoofingAttackFre = 100
SpoofingAttackDOSelect = [0, 0, 0, 0, 0, 0, 0, 0]
SpoofingAttackDOValue = [0, 0, 0, 0, 0, 0, 0, 0]
SpoofingAttackActiveBit = 0x00

AttackConfigCounter = 0
AttackConfigTimer = None
AttackConfigList = None
AttackConfigNowMode = 1
attack_gauge_run = None

# 0 is normal mode message are Chronological, 1 the messages are fixed
traceListMode = 0
# interval time mode
intervalTimeMode = False

global_time = 0
refresh_time = 0

# Open the port
def open_port(id, rate):
    global bus
    global openFlag
    bus = Usb2canBus(id, flags=0x00000008, serial=id, bitrate=rate)
    # identify the connect state by the return value

    if bus.handle == 0:
        print ("Open fail")
        openFlag = False
        wx.MessageBox("Failed to open device.", "Message", wx.OK | wx.ICON_INFORMATION)
        return

    else:
        openFlag = True
        print ("Open success")
        frame.m_buttonTest.Enable(enable=True)
        frame.m_button_attack_start.Enable(enable=True)
        frame.m_button_analysis1.Enable(enable=True)
        # frame.m_button_analysis2.Enable(enable=True)
        frame.m_buttonOpen.SetLabelText("Shutdown")
        frame.m_btn_start_tracing.Enable(enable=True)
        frame.m_btn_stop_tracing.Enable(enable=False)
        frame.m_btn_pause_tracing.Enable(enable=False)
        frame.m_btn_start_player.Enable(enable=True)
        frame.m_btn_stop_player.Enable(enable=False)
        frame.m_btn_pause_player.Enable(enable=False)


# Send a htx message
def send_msg(msg):

    if msg is None:
        msg = can.Message(arbitration_id=0x123,
                          data=[1, 2, 3, 4, 5, 6, 7, 8]
                          , extended_id=False
                          , timestamp=refresh_time + int(time.clock()*1000)-global_time)
    else:
        msg.timestamp = refresh_time + int(time.clock()*1000)-global_time

    try:
        bus.send(msg)
        # print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        # print("Message NOT sent")
        pass

    if isStarted is True:
        wx.CallAfter(pub.sendMessage, "ut", msg=msg, type=2)

    # flexible increase sure that the submit event will be lunched period

    global logfile
    if logfile is not None:
        canid = msg.arbitration_id
        timestamp = msg.timestamp
        data = ' '.join(hex(x) for x in msg.data)
        attack_info = ""

        if isDoSAttacked is True:
            attack_info = "1"
        elif isFuzzAttacked is True:
            attack_info = "2"
        elif isSpoofingAttacked is True:
            attack_info = "3-" + hex(SpoofingAttackActiveBit)

        logfile.writemsg(timestamp, canid, data, "2," + "A_Info:" + attack_info)


# Define shutdown the bus safe
def shutdown():
    global openFlag
    global timer1, timer2, AttackConfigTimer, isDoSAttacked, isFuzzAttacked
    global isStarted, isPlayerStarted
    global canReader
    if isStarted:
        canReader.stop()
        isStarted = False
    if isPlayerStarted:
        canReader.stop()
        isPlayerStarted = False

    Usb2canBus.shutdown(bus)
    # close the timer
    if timer1:
        timer1.cancel()
        isDoSAttacked = False
    if timer2:
        timer2.cancel()
        isFuzzAttacked = False
    if AttackConfigTimer:
        AttackConfigTimer.cancel()

    frame.m_buttonTest.Enable(enable=False)
    frame.m_button_attack_start.Enable(enable=False)
    frame.m_button_analysis1.Enable(enable=False)
    # frame.m_button_analysis2.Enable(enable=False)
    frame.m_btn_start_tracing.Enable(enable=False)
    frame.m_btn_stop_tracing.Enable(enable=False)
    frame.m_btn_pause_tracing.Enable(enable=False)
    frame.m_btn_start_player.Enable(enable=False)
    frame.m_btn_stop_player.Enable(enable=False)
    frame.m_btn_pause_player.Enable(enable=False)
    frame.m_buttonOpen.SetLabelText("Open")
    openFlag = False
    print ("Close success")


# Define Frame Class
class CalcFrame(frame.MyFrame1):
    def __init__(self, parent):
        frame.MyFrame1.__init__(self, parent)
        self.count = 0
        self.display_list()
        pub.subscribe(self.update_trace_display, "ut")
        pub.subscribe(self.get_Spoofing_attack_analysis, "ufa")

        self.IDCountMap = {}
        self.ID2Packets = {}
        self.PeriodFlag = {}
        self.TimeIntervalMap = {}
        self.TimeLastIntervalMap = {}
        self.TimeStampMap = {}
        self.last_time_stamp = 0
        self.time_show_count = 0

    def OnExit(self, event):
        # event.Skip()
        if openFlag:
            shutdown()
        global canReader
        if canReader is not None:
            canReader.stop()
        self.Destroy()

    # Device control
    def clickOpen(self, event):
        if openFlag:
            shutdown()
        else:
            open_port(str(self.m_textID.Value), int(self.m_choice_BR.GetStringSelection()))

    def clickTest(self, event):
        send_msg(None)

    # DoS Attack control
    def onclick_attack_start(self, event):

        global Spoofing_attack_mode
        global SpoofingAttackID, SpoofingAttackFre
        global SpoofingAttackDOSelect, SpoofingAttackDOValue, SpoofingAttackActiveBit
        global isSpoofingAttacked
        global canReader

        if self.m_radioBtnDos.GetValue():
            self.m_radioBtnDos.Enable(enable=False)
            global timer1, timer2, isDoSAttacked
            timer1 = threading.Timer(0.05, send_attack)
            timer1.start()
            isDoSAttacked = True

        elif self.m_radioBtnFuzz.GetValue():
            self.m_radioBtnFuzz.Enable(enable=False)
            global timer2, isFuzzAttacked, FuzzingAttackIDRangeEnd, FuzzingAttackIDRangeStart
            timer2 = threading.Timer(1, fuzz_attack)
            timer2.start()
            time_range_text = self.m_textCtrl_FuzzID.GetValue()
            time_list = time_range_text.split(",")
            time_range_list = time_list[0].split("-")
            FuzzingAttackIDRangeStart = int(time_range_list[0], 16)
            FuzzingAttackIDRangeEnd = int(time_range_list[1], 16)

            isFuzzAttacked = True

        elif self.m_radioBtnSpoof.GetValue():
            SpoofingAttackID = long(self.m_listBox_spoof_attack.GetStringSelection().split(';')[0].replace("ECU_ID:", ""))
            temp = []
            temp.append(int(self.m_textCtrl_fixdata1.GetValue(), 16))
            temp.append(int(self.m_textCtrl_fixdata2.GetValue(), 16))
            temp.append(int(self.m_textCtrl_fixdata3.GetValue(), 16))
            temp.append(int(self.m_textCtrl_fixdata4.GetValue(), 16))
            temp.append(int(self.m_textCtrl_fixdata5.GetValue(), 16))
            temp.append(int(self.m_textCtrl_fixdata6.GetValue(), 16))
            temp.append(int(self.m_textCtrl_fixdata7.GetValue(), 16))
            temp.append(int(self.m_textCtrl_fixdata8.GetValue(), 16))

            if self.m_checkBox_a_fd.GetValue() is True:
                # self.SpoofingAttackMsg = can.Message(arbitration_id=self.SpoofingAttackID, data=[temp[0], temp[1]
                #                     , temp[2], temp[3], temp[4], temp[5], temp[6], temp[7]] , extended_id=False)
                Spoofing_attack_mode = 1

            elif self.m_checkBox_a_do.GetValue() is True:
                Spoofing_attack_mode = 2

            SpoofingAttackDOSelect[0] = int(self.m_checkBox_offset1.GetValue())
            SpoofingAttackDOSelect[1] = int(self.m_checkBox_offset2.GetValue())
            SpoofingAttackDOSelect[2] = int(self.m_checkBox_offset3.GetValue())
            SpoofingAttackDOSelect[3] = int(self.m_checkBox_offset4.GetValue())
            SpoofingAttackDOSelect[4] = int(self.m_checkBox_offset5.GetValue())
            SpoofingAttackDOSelect[5] = int(self.m_checkBox_offset6.GetValue())
            SpoofingAttackDOSelect[6] = int(self.m_checkBox_offset7.GetValue())
            SpoofingAttackDOSelect[7] = int(self.m_checkBox_offset8.GetValue())

            SpoofingAttackActiveBit = 0x00
            for i in range(0, 8):
                if SpoofingAttackDOSelect[i] is 1:
                    SpoofingAttackDOValue[i] = temp[i]
                    SpoofingAttackActiveBit = SpoofingAttackActiveBit | (0x01 << (7 - i))
                else:
                    SpoofingAttackDOValue[i] = 0

            SpoofingAttackFre = 100 - self.m_slider_Spoofing_f.GetValue()

            canReader = CANPacketReader(None, None)
            canReader.start()
            isSpoofingAttacked = True

            self.m_radioBtnSpoof.Enable(enable=False)

            # print (str(self.SpoofingAttackFre))
            # print (SpoofingAttackID, self.SpoofingAttackMsg)

        elif self.m_radioBtnConfig.GetValue():
            self.m_radioBtnConfig.Enable(enable=False)
            do_attack_config(self.m_filePicker_config.GetPath())

        else:
            wx.MessageBox("Please select attack method!", "Message", wx.OK | wx.ICON_INFORMATION)
            return

        event.GetEventObject().Disable()
        self.m_button_attack_stop.Enable(enable=True)
        self.m_button_analysis1.Enable(enable=False)

    def onclick_attack_stop(self, event):
        self.m_button_attack_start.Enable(enable=True)
        self.m_button_attack_stop.Enable(enable=False)
        global timer1, timer2, isDoSAttacked, isSpoofingAttacked, isFuzzAttacked

        if self.m_radioBtnDos.GetValue():
            self.m_radioBtnDos.Enable(enable=True)
            timer1.cancel()
            isDoSAttacked = False
        elif self.m_radioBtnFuzz.GetValue():
            self.m_radioBtnFuzz.Enable(enable=True)
            timer2.cancel()
            isFuzzAttacked = False
        elif self.m_radioBtnSpoof.GetValue():
            self.m_radioBtnSpoof.Enable(enable=True)
            if isStarted:
                isSpoofingAttacked = False
            else:
                global canReader
                canReader.stop()

        elif self.m_radioBtnConfig.GetValue():
            self.m_radioBtnConfig.Enable(enable=True)
            global AttackConfigTimer, AttackConfigCounter
            AttackConfigTimer.cancel()
            AttackConfigCounter = 0
            if AttackConfigNowMode == 1:
                timer1.cancel()
                isDoSAttacked = False
            elif AttackConfigNowMode == 3:
                timer2.cancel()
                isFuzzAttacked = False
            elif AttackConfigNowMode == 2:
                if isStarted:
                    isSpoofingAttacked = False
                else:
                    global canReader
                    canReader.stop()
            if attack_gauge_run:
                attack_gauge_run.stop()
                frame.set_gauge_value(0)

        self.m_button_analysis1.Enable(enable=True)
        # global canReader
        # canReader.stop()
        # self.m_button_analysis2.Enable(enable=True)

    def onclick_start_tracing(self, event):
        global canReader
        global isStarted
        # check if the threading is started
        if isStarted:
            canReader.resume()
        else:
            isStarted = True
            if self.m_cb_savedb.GetValue():
                canReader = CANPacketReader(1, self.m_dP_db.GetPath())
            elif self.m_cb_savelog.GetValue():
                canReader = CANPacketReader(2, self.m_dP_db.GetPath())
            else:
                canReader = CANPacketReader(0, self.m_dP_db.GetPath())
            canReader.start()
        self.m_btn_start_tracing.Enable(enable=False)
        self.m_btn_pause_tracing.Enable(enable=True)
        self.m_btn_stop_tracing.Enable(enable=True)

    def onclick_pause_tracing(self, event):
        global canReader
        canReader.pause()
        self.m_btn_start_tracing.Enable(enable=True)
        self.m_btn_pause_tracing.Enable(enable=False)
        self.m_btn_stop_tracing.Enable(enable=True)

    def onclick_stop_tracing(self, event):
        global canReader
        canReader.stop()
        global isStarted
        isStarted = False
        self.m_btn_start_tracing.Enable(enable=True)
        self.m_btn_pause_tracing.Enable(enable=False)
        self.m_btn_stop_tracing.Enable(enable=False)

    def onclick_start_play(self, event):
        if self.m_filePicker_player.GetPath() == "":
            wx.MessageBox("Please select an available file!", "Message", wx.OK | wx.ICON_INFORMATION)
            return
        global canPlayer
        global isPlayerStarted
        # check if the threading is started
        if isPlayerStarted:
            canPlayer.resume()
        else:
            if self.m_textCtrl_player_loop.GetValue() is None:
                canPlayer = CanPlayer(0, self.m_filePicker_player.GetPath())
            else:
                canPlayer = CanPlayer(int(self.m_textCtrl_player_loop.GetValue()), self.m_filePicker_player.GetPath())
            canPlayer.start()
        self.m_btn_start_player.Enable(enable=False)
        self.m_btn_pause_player.Enable(enable=True)
        self.m_btn_stop_player.Enable(enable=True)

    def onclick_pause_play(self, event):
        global canPlayer
        canPlayer.pause()
        self.m_btn_start_player.Enable(enable=True)
        self.m_btn_pause_player.Enable(enable=False)
        self.m_btn_stop_player.Enable(enable=True)

    def onclick_stop_play(self, event):
        global canPlayer
        canPlayer.stop()
        global isPlayerStarted
        isPlayerStarted = False
        self.m_btn_start_player.Enable(enable=True)
        self.m_btn_pause_player.Enable(enable=False)
        self.m_btn_stop_player.Enable(enable=False)

    def on_text_enter_player(self, event):
        s = self.m_textCtrl_player_loop.GetValue()
        if len(s) > 0 and len(s) <= 5 and re.match("\A[0-9]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 5:
            self.m_textCtrl_player_loop.SetValue("")
            wx.MessageBox("Please enter a valid value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def onclick_convert(self, event):
        can_matrix_convert(self.m_cb_for_IDS.GetValue(), self.m_filePicker_matrix_imput.GetPath()
                           , str(self.m_textCtrl_matrix_output_name.GetValue())
                           , self.m_choice_matrix_output_format.GetStringSelection()
                           , self.m_dirPicker_matrix_output_path.GetPath())

    def onclick_data_convert(self, event):
        can_data_convert(self.m_filePicker_data_imput.GetPath(), str(self.m_textCtrl_data_output_name.GetValue())
                           , self.m_choice_data_output_format.GetStringSelection()
                           , self.m_dirPicker_data_output_path.GetPath())

    def onclick_trace_clean_up(self, event):
        self.m_listCtrl1.DeleteAllItems()

    def onclick_choice_tracelist_mode(self, event):
        global traceListMode
        traceListMode = int(self.m_choice_tracelist_mode.GetSelection())
        # self.m_listCtrl1.SetItemText([1, 2, 3])

    def onclick_cb_trace_time_mode(self, event):
        global intervalTimeMode
        if self.m_cb_time_mode.Value:
            intervalTimeMode = True
            print "is interval mode"
        else:
            intervalTimeMode = False
            print "is not interval mode"

    def onclick_btn_Spoofing_attack(self, event):
        global canReader
        global isSpoofingAttackAnalysis
        if isSpoofingAttackAnalysis is False:
            self.m_button_analysis1.SetLabelText("  Stop ")
            isSpoofingAttackAnalysis = True
            if isStarted:
                canReader.resume()
            else:
                canReader = CANPacketReader(None, None)
                canReader.start()
        else:
            self.m_button_analysis1.SetLabelText("Analyze")
            isSpoofingAttackAnalysis = False
            canReader.stop()
            i = 0
            for key in self.PeriodFlag:
                if self.PeriodFlag[key] >= 5:
                    i += 1
            # if there is at least one period message , we can lunch Spoofing attack
            if i >= 1:
                self.m_radioBtnSpoof.Enable(enable=True)

    def onclick_da_analye(self, event):
        dataset_analysis(self.m_filePicker_da_imput.GetPath())

    def onclick_da_generate(self, event):
        id_list = []
        select_item_num = self.m_listBox2.GetSelections()
        # get the select items ID
        for item in select_item_num:
            print select_item_num[0]
            select_item = self.m_listBox2.GetString(item)
            id_list.append(select_item.split(';')[0].replace("ID:", ""))

        dataset_analysis_generate_plot(1 ,self.m_filePicker_da_imput.GetPath(), id_list)

    def on_check_box_fd(self, event):
        self.m_checkBox_a_do.SetValue(False)

    def on_check_box_do(self, event):
        self.m_checkBox_a_fd.SetValue(False)

    # Scroll changed
    def on_Spoofing_fre_change(self, event):
        self.m_text_Spoofing_fv.SetLabelText(str(self.m_slider_Spoofing_f.GetValue()))

    def on_text_enter_at_fixd1(self, event):
        s = self.m_textCtrl_fixdata1.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata1.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def on_text_enter_at_fixd2(self, event):
        s = self.m_textCtrl_fixdata2.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata2.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def on_text_enter_at_fixd3(self, event):
        s = self.m_textCtrl_fixdata3.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata3.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def on_text_enter_at_fixd4(self, event):
        s = self.m_textCtrl_fixdata4.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata4.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def on_text_enter_at_fixd5(self, event):
        s = self.m_textCtrl_fixdata5.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata5.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def on_text_enter_at_fixd6(self, event):
        s = self.m_textCtrl_fixdata6.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata6.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def on_text_enter_at_fixd7(self, event):
        s = self.m_textCtrl_fixdata7.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata7.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def on_text_enter_at_fixd8(self, event):
        s = self.m_textCtrl_fixdata8.GetValue()
        if len(s) > 0 and len(s) <= 2 and re.match("\A[0-9a-fA-F]+\Z", s) is not None:
            return
        elif len(s) > 0 or len(s) > 2:
            self.m_textCtrl_fixdata8.SetValue("")
            wx.MessageBox("Please enter a valid hex value!", "Message", wx.OK | wx.ICON_INFORMATION)
        else:
            return

    def set_gauge_range(self, range1):
        self.m_gauge1.SetRange(range1)

    def set_gauge_value(self, value):
        self.m_gauge1.SetValue(value)

    # Display
    def display_list(self):
        self.m_listCtrl1.InsertColumn(1, 'Time', format=wx.LIST_FORMAT_CENTRE)
        self.m_listCtrl1.InsertColumn(2, 'ECU_ID', format=wx.LIST_FORMAT_CENTRE)
        self.m_listCtrl1.InsertColumn(3, 'Data', format=wx.LIST_FORMAT_CENTRE)
        self.m_listCtrl1.InsertColumn(4, 'Count', format=wx.LIST_FORMAT_CENTRE)
        self.m_listCtrl1.InsertColumn(5, 'Dir', format=wx.LIST_FORMAT_CENTRE)

        self.m_listCtrl1.SetColumnWidth(0, 80)
        self.m_listCtrl1.SetColumnWidth(1, 80)
        self.m_listCtrl1.SetColumnWidth(2, 300)
        self.m_listCtrl1.SetColumnWidth(3, 80)
        self.m_listCtrl1.SetColumnWidth(4, 80)

    def update_trace_display(self, msg, type):
        global intervalTimeMode
        my_msg = msg
        # set the count in Dic
        # t = time.clock()
        timestamp = my_msg.timestamp

        idtemp = msg.arbitration_id
        idStr = hex(idtemp).replace('L', '')
        payload = ' '.join(hex(x) for x in msg.data)
        # print time.clock()-t

        if type == 2:
            # self.m_listCtrl1.Append([timestamp, idStr, payload, "", "TX"])
            return

        # Change the count
        if not self.IDCountMap.has_key(idStr):
            self.IDCountMap[idStr] = 1
        else:
            self.IDCountMap[idStr] += 1

        # check the show mode
        if intervalTimeMode is False and traceListMode == 0:
            # insert the message into the listview

            self.m_listCtrl1.Append([timestamp, idStr, payload,"","RX"])
            self.m_listCtrl1.EnsureVisible(self.m_listCtrl1.GetItemCount() - 1 if self.m_listCtrl1.GetItemCount() > 0 else 0)

        # check the show mode
        if intervalTimeMode is True and traceListMode == 0:
            # insert the message into the listview
            self.m_listCtrl1.Append([-1 if self.last_time_stamp == 0 else timestamp-self.last_time_stamp, idStr, payload,"","RX"])
            self.m_listCtrl1.EnsureVisible(
                self.m_listCtrl1.GetItemCount() - 1 if self.m_listCtrl1.GetItemCount() > 0 else 0)
            self.last_time_stamp = timestamp

        elif intervalTimeMode is True and traceListMode == 1:
            if not self.TimeIntervalMap.has_key(idStr):
                self.TimeStampMap[idStr] = timestamp
                self.TimeIntervalMap[idStr] = -1
            else:
                self.TimeIntervalMap[idStr] = timestamp - self.TimeStampMap[idStr]
                self.TimeStampMap[idStr] = timestamp

            self.ID2Packets[idStr] = payload

            self.time_show_count += int(timestamp - self.last_time_stamp) / 10 + 1
            self.last_time_stamp = timestamp

            if self.time_show_count >= 250:
                self.time_show_count = 0
                self.m_listCtrl1.DeleteAllItems()
                for key in self.TimeIntervalMap:
                    self.m_listCtrl1.Append([self.TimeIntervalMap[key], key, self.ID2Packets[key], self.IDCountMap[key], "RX"])

        elif intervalTimeMode is False and traceListMode == 1:
            if not self.TimeIntervalMap.has_key(idStr):
                self.TimeStampMap[idStr] = timestamp
                self.TimeIntervalMap[idStr] = -1
            else:
                self.TimeIntervalMap[idStr] = timestamp - self.TimeStampMap[idStr]
                self.TimeStampMap[idStr] = timestamp

            self.ID2Packets[idStr] = payload

            self.time_show_count += int(timestamp - self.last_time_stamp) / 10 + 1
            self.last_time_stamp = timestamp

            if self.time_show_count >= 500:
                self.time_show_count = 0
                self.m_listCtrl1.DeleteAllItems()
                for key in self.TimeIntervalMap:
                    self.m_listCtrl1.Append([self.TimeStampMap[key], key, self.ID2Packets[key], self.IDCountMap[key], "RX"])

        else:
            pass

    def get_Spoofing_attack_analysis(self, msg):
        global intervalTimeMode
        # my_msg = msg
        # set the count in Dic

        timestamp = msg.timestamp
        idtemp = msg.arbitration_id

        idStr = str(idtemp)
        # payload = ' '.join(hex(x) for x in msg.data)
        # if get target messages, then send the attack messages
        if isSpoofingAttacked:
            if idtemp == SpoofingAttackID and random.randint(0, 100) > SpoofingAttackFre:
                if Spoofing_attack_mode is 1:
                    for i in range(0, len(msg.data)):
                        if SpoofingAttackDOSelect[i] is 1:
                            msg.data[i] = SpoofingAttackDOValue[i]
                            if msg.data[i] > 0xff:
                                msg.data[i] = 0xff
                elif Spoofing_attack_mode is 2:
                    for i in range(0, len(msg.data)):
                        msg.data[i] += SpoofingAttackDOValue[i]
                        if msg.data[i] > 0xff:
                            msg.data[i] = 0xff
                send_msg(msg)
                # print ("log2")
            return

        # Change the count
        if not self.IDCountMap.has_key(idStr):
            self.IDCountMap[idStr] = 1
            self.PeriodFlag[idStr] = 0
        else:
            self.IDCountMap[idStr] += 1

        if not self.TimeIntervalMap.has_key(idStr):
            self.TimeStampMap[idStr] = timestamp
            self.TimeIntervalMap[idStr] = -1
            self.TimeLastIntervalMap[idStr] = -1
        else:
            self.TimeIntervalMap[idStr] = timestamp - self.TimeStampMap[idStr]
            self.TimeStampMap[idStr] = timestamp
            # if the contiguous messages interval is in a very min range
            if self.TimeLastIntervalMap is not -1 and math.fabs(self.TimeIntervalMap[idStr] - self.TimeLastIntervalMap[idStr]) < 10:
                self.PeriodFlag[idStr] += 1
                if self.PeriodFlag[idStr] >= 5:
                    self.PeriodFlag[idStr] = 5
            else:
                self.PeriodFlag[idStr] -= 1
                if self.PeriodFlag[idStr] <= 0:
                    self.PeriodFlag[idStr] = 0

            self.TimeLastIntervalMap[idStr] = self.TimeIntervalMap[idStr]

        self.time_show_count += int(timestamp - self.last_time_stamp) / 10 + 1
        self.last_time_stamp = timestamp

        if self.time_show_count >= 250:
            self.time_show_count = 0
            self.m_listBox_spoof_attack.Clear()
            for key in self.TimeIntervalMap:
                self.m_listBox_spoof_attack.Append("ECU_ID:"+key+";Time:"+str(self.TimeIntervalMap[key])+";IF:"
                                                  + str(self.PeriodFlag[key]))


# DoS Attack send message
def send_attack():
    # t=msg
    global timer1, isDoSAttacked
    msg = can.Message(arbitration_id=0x0,
                      data=[0x0, 0x0],
                      extended_id=False)
    send_msg(msg)
    if isDoSAttacked is True:
        timer1 = threading.Timer(0.0005, send_attack)
        timer1.start()


# DoS Attack send message
def fuzz_attack():
    # t=msg
    global timer2, isFuzzAttacked, FuzzingAttackIDRangeStart, FuzzingAttackIDRangeEnd,\
        FuzzingAttackData, FuzzingAttackFre, Fuzzing_attack_mode, FuzzingAttackID

    data = []
    if Fuzzing_attack_mode == 1:
        r_id = random.randint(FuzzingAttackIDRangeStart, FuzzingAttackIDRangeEnd)
        for i in range(0, 8):
            data.append(random.randint(0, 255))

        msg = can.Message(arbitration_id=r_id,
                          data=data,
                          extended_id=False)
        t = random.randint(20, 100) / 1000
        send_msg(msg)

    elif Fuzzing_attack_mode == 2:
        msg = can.Message(arbitration_id=FuzzingAttackID,
                          data=FuzzingAttackData,
                          extended_id=False)
        t = FuzzingAttackFre
        send_msg(msg)

    if isFuzzAttacked is True:
        timer2 = threading.Timer(t, fuzz_attack)
        timer2.start()


def do_attack_config(path):
    global AttackConfigTimer, AttackConfigCounter, AttackConfigList, attack_gauge_run
    AttackConfigList = Tool.getlist(path)
    AttackConfigCounter = 0
    AttackConfigTimer = Timer(AttackConfigList[AttackConfigCounter].start_t, set_and_start
                              , (AttackConfigList[AttackConfigCounter],))
    AttackConfigTimer.start()
    #set A gauge
    gauge_total_time = AttackConfigList[len(AttackConfigList)-1].end_t - AttackConfigList[AttackConfigCounter].start_t
    frame.set_gauge_range(gauge_total_time)
    attack_gauge_run = GaugeRun(gauge_total_time)
    attack_gauge_run.start()


def set_and_start(attack_info):

    global AttackConfigTimer, AttackConfigNowMode
    global SpoofingAttackID, SpoofingAttackFre, SpoofingAttackActiveBit
    global SpoofingAttackDOSelect, SpoofingAttackDOValue
    global AttackConfigList
    global isSpoofingAttacked
    global Spoofing_attack_mode
    global canReader

    # DoS attack
    if attack_info.attack_type == 1:
        global timer1, isDoSAttacked
        timer1 = threading.Timer(0.05, send_attack)
        timer1.start()
        isDoSAttacked = True
        AttackConfigNowMode = 1
        print "set and start DoS"

    # Fuzz attack
    elif attack_info.attack_type == 3:
        global timer2, isFuzzAttacked, FuzzingAttackIDRangeStart, \
            FuzzingAttackIDRangeEnd, Fuzzing_attack_mode, FuzzingAttackID, FuzzingAttackFre, FuzzingAttackData

        Fuzzing_attack_mode = attack_info.msg_type
        if Fuzzing_attack_mode == 1:
            time_list = attack_info.msg_range.split(",")
            time_range_list = time_list[0].split("-")
            FuzzingAttackIDRangeStart = int(time_range_list[0], 16)
            FuzzingAttackIDRangeEnd = int(time_range_list[1], 16)

        elif Fuzzing_attack_mode == 2:
            FuzzingAttackID = attack_info.msg_id
            FuzzingAttackFre = attack_info.msg_fre * 0.001
            for i in range(0, 8):
                FuzzingAttackData[i] = int(attack_info.msg_data[i], 16)

        timer2 = threading.Timer(0.05, fuzz_attack)
        timer2.start()
        isFuzzAttacked = True
        AttackConfigNowMode = 3
        print "set and start Fuzz"

    # Spoofing attack
    elif attack_info.attack_type == 2:
        SpoofingAttackID = long(attack_info.msg_id)
        temp = []
        for i in range(0, 8):
            temp.append(int(attack_info.msg_data[i], 16))

        Spoofing_attack_mode = attack_info.msg_type

        for i in range(0, 8):
            SpoofingAttackDOSelect[i] = attack_info.msg_active_bit >> (7-i) & 0x01

        SpoofingAttackActiveBit = attack_info.msg_active_bit

        for i in range(0, 8):
            if SpoofingAttackDOSelect[i] == 1:
                SpoofingAttackDOValue[i] = temp[i]
            else:
                SpoofingAttackDOValue[i] = 0

        SpoofingAttackFre = 100 - attack_info.msg_fre

        if canReader is None:
            canReader = CANPacketReader(None, None)
            canReader.start()
        elif canReader.runstate == 0 or canReader.runstate == 2:
            canReader.resume()
        elif canReader.runstate == 1:
            pass

        isSpoofingAttacked = True
        AttackConfigNowMode = 2

        print "set and start Spoofing"

    AttackConfigTimer = Timer(AttackConfigList[AttackConfigCounter].end_t
                              - AttackConfigList[AttackConfigCounter].start_t, end_and_wait
                              , ())
    AttackConfigTimer.start()


def end_and_wait():
    global timer1, timer2, AttackConfigTimer, AttackConfigNowMode, AttackConfigCounter
    global AttackConfigList
    global isDoSAttacked, isFuzzAttacked

    if AttackConfigNowMode == 1:
        timer1.cancel()
        isDoSAttacked = False
        print "Stop DoS"
    elif AttackConfigNowMode == 3:
        timer2.cancel()
        isFuzzAttacked = False
        print "Stop Fuzz"
    elif AttackConfigNowMode == 2:
        global isSpoofingAttacked
        isSpoofingAttacked = False
        print "Stop Spoofing"

    AttackConfigCounter += 1
    if AttackConfigCounter < len(AttackConfigList):
        AttackConfigTimer = Timer(AttackConfigList[AttackConfigCounter].start_t
                                  - AttackConfigList[AttackConfigCounter-1].end_t, set_and_start
                                  , (AttackConfigList[AttackConfigCounter],))
        AttackConfigTimer.start()
    else:
        frame.onclick_attack_stop(None)
        AttackConfigTimer.cancel()


# CAN packetReader
class GaugeRun(threading.Thread):
    Debug = 1

    def __init__(self, total_time):
        # threading.Thread.__init__(self)
        super(GaugeRun, self).__init__()
        self.__flag = threading.Event()  # To add flag to a stop
        self.__flag.set()  # set True
        self.__running = threading.Event()  # set stop
        self.__running.set()
        self.count = 0
        self.end_t = total_time

    def run(self):
        while self.__running.isSet():
            time.sleep(1)
            self.count += 1
            frame.set_gauge_value(self.count)
            if self.count == self.end_t:
                self.stop()

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()


# CAN packetReader
class CANPacketReader(threading.Thread):
    Debug = 1

    runstate = 0

    def __init__(self, is_save, log_db):
        # threading.Thread.__init__(self)
        super(CANPacketReader, self).__init__()
        self.__flag = threading.Event()  # To add flag to a stop
        self.__flag.set()  # set True
        self.__running = threading.Event()  # set stop
        self.__running.set()  # runset true
        self.LogDB = log_db
        self.IsSave = is_save
        global logfile
        logfile = None

    def run(self):
        global global_time, refresh_time
        self.runstate = 1
        i = 0
        j = 0
        data1 = []
        sql = 'INSERT INTO Packets(Timestamp, ECU_ID, Data) VALUES(?,?,?);'
        last_time_stamp = 0

        if self.IsSave == 1 and self.LogDB:
            conn = sqlite3.connect(self.LogDB+"\\mydata.db")
            cursor = conn.cursor()
            try:
                # create table
                cursor.execute(
                    "CREATE TABLE Packets(id INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp INTEGER, ECU_ID INTEGER, Data VARCHAR(15))")
            except:
                pass

        if self.IsSave == 2 and self.LogDB:
            # os.mknod(self.LogDB+"\\mydata.txt")
            # self.logf = open(self.LogDB+"\\mydata.log", 'w')
            global logfile
            logfile = File(self.LogDB)

        if self.Debug > 0:
            fd = None
            try:
                fd = open("raw_packets.log", "wb")
            except:
                import traceback
                traceback.print_exc()

        while openFlag is True and self.__running.isSet():
            self.__flag.wait()
            global bus
            msg = Usb2canBus.recv(bus, timeout=None)
            if msg is not None:
                # if Spoofing attack is started
                if isSpoofingAttackAnalysis or isSpoofingAttacked:
                    wx.CallAfter(pub.sendMessage, "ufa", msg=msg)

                if isStarted is True and self.IsSave == 0:
                    wx.CallAfter(pub.sendMessage, "ut", msg=msg, type=1)

                # current_time = time.time()
                # save msg to sqlite
                if self.IsSave == 1:
                    canid = msg.arbitration_id
                    timestamp = msg.timestamp
                    data = ' '.join(hex(x) for x in msg.data)
                    # flexible increase sure that the submit event will be lunched period
                    i += int(timestamp-last_time_stamp)/10 + 1
                    last_time_stamp = timestamp
                    data1.append((timestamp, canid, data))
                    if i >= 500:
                        i = 0
                        try:
                            sql = sql[:-1] + ';'
                            cursor.executemany(sql, data1)
                            conn.commit()
                        except:
                            import traceback
                            if self.Debug > 0:
                                if fd is not None:
                                    fd.write("Exception:" + traceback.format_exc())
                            else:
                                traceback.print_exc()
                        data1 = []

                if self.IsSave == 2:
                    # start_time = time.clock()
                    canid = msg.arbitration_id
                    timestamp = msg.timestamp
                    data = ' '.join(hex(x) for x in msg.data)
                    # flexible increase sure that the submit event will be lunched period
                    global logfile
                    logfile.writemsg(timestamp, canid, data, "1")

                timestamp = msg.timestamp
                j += int(timestamp - last_time_stamp) / 10 + 1
                last_time_stamp = timestamp
                if j >= 500:
                    j = 0
                    global_time = int(time.clock()*1000)
                    refresh_time = timestamp

    def pause(self):
        self.runstate = 2
        self.__flag.clear()

    def resume(self):
        self.runstate = 1
        self.__flag.set()

    def stop(self):
        self.runstate = 0
        self.__flag.set()
        self.__running.clear()
        global logfile
        if logfile is not None:
            logfile.close_file()


class CanPlayer(threading.Thread):
    Debug = 1

    def __init__(self, loop, file):
        # threading.Thread.__init__(self)
        super(CanPlayer, self).__init__()
        self.__flag = threading.Event()  # To add flag to a stop
        self.__flag.set()  # set True
        self.__running = threading.Event()  # set stop
        self.__running.set()  # runset true
        self.LogDB = file
        self.loop = loop
        self.logf = None

    def run(self):
        global isPlayerStarted
        isPlayerStarted = True

        if self.LogDB:
            self.logf = open(self.LogDB, 'r')

        count = 0

        while openFlag is True and self.__running.isSet():
            self.__flag.wait()
            global bus
            time_stamp = 0

            for i in range(0, self.loop):
                self.logf = open(self.LogDB, 'r')
                for line in self.logf:

                    data = line.split(",")
                    time_st = long(data[0].replace("Time:", ""))
                    id_my = int(data[1].replace("ID:", ""))
                    datastr = data[2].replace("Data:", "")

                    if time_stamp > 0:
                        slp = time_st - time_stamp
                        if slp < 0:
                            slp = 0
                    else:
                        slp = 0

                    time_stamp = time_st

                    data_temp = []
                    i = 0
                    for s in datastr.split(" "):
                        data_temp.append(int(s, 16))
                        i += 1
                    msg = can.Message(arbitration_id=id_my,
                                      data=data_temp,
                                      extended_id=False)
                    try:
                        bus.send(msg)
                    except can.CanError:
                        pass

                    if slp == 0:
                        pass
                    elif slp == 1:
                        temp = time.clock()
                        wx.MilliSleep(1)
                        print time.clock() - temp
                    elif slp > 1:
                        time.sleep(slp * 0.001)

                self.logf.close()

            self.stop()
            global isPlayerStarted
            isPlayerStarted = False
            frame.m_btn_start_player.Enable(enable=True)
            frame.m_btn_pause_player.Enable(enable=False)
            frame.m_btn_stop_player.Enable(enable=False)

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()
        self.logf.close()


# CanMatrix Convert
def can_matrix_convert(mode, input_file, output_file_name, out_file_format, output_file_path):
    if mode is False:
        extent = Tool.GetFileNameAndExt(input_file)
        if input_file == '':
            wx.MessageBox("Please select file!", "Message", wx.OK | wx.ICON_INFORMATION)
            return
        if out_file_format == '':
            wx.MessageBox("Please select file!", "Message", wx.OK | wx.ICON_INFORMATION)
            return
        if output_file_path == '':
            wx.MessageBox("Please input the path!", "Message", wx.OK | wx.ICON_INFORMATION)
            return
        if extent == out_file_format:
            wx.MessageBox("Convert format must be different!", "Message", wx.OK | wx.ICON_INFORMATION)
            return
        output = "%s\\%s%s" % (output_file_path, output_file_name, out_file_format)
        canmatrix.convert.convert(input_file, output)
    else:
        if input_file == '':
            wx.MessageBox("Please select file!", "Message", wx.OK | wx.ICON_INFORMATION)
            return
        # if out_file_format is not ".xml":
        #     wx.MessageBox("Please select file!", "Message", wx.OK | wx.ICON_INFORMATION)
        #     return
        # if output_file_path == '':
        #     wx.MessageBox("Please input the path!", "Message", wx.OK | wx.ICON_INFORMATION)
        #     return
        output = "%s\\%s%s" % (output_file_path, output_file_name, ".xml")
        data = open_excel(input_file)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        colnames = table.row_values(0)
        list = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(0, 3):
                    app[colnames[i]] = row[i]
                if len(list) > 1:
                    if app != list[len(list)-1]:
                        list.append(app)
                else:
                    list.append(app)

        generate_xml(list, output)

        return list


def generate_xml(list, outfile):
    doc = Dom.Document()
    root_node = doc.createElement("elements")
    root_node.setAttribute("name", "pdus")
    doc.appendChild(root_node)

    for item in list:
        book_node = doc.createElement("pdu")

        book_name_node = doc.createElement("id")
        book_name_value = doc.createTextNode(item["ID"])
        book_name_node.appendChild(book_name_value)
        book_node.appendChild(book_name_node)

        book_author_node = doc.createElement("period")
        book_author_value = doc.createTextNode(str(item["Cycle Time [ms]"]))
        book_author_node.appendChild(book_author_value)
        book_node.appendChild(book_author_node)

        book_author_node = doc.createElement("frame_name")
        book_author_value = doc.createTextNode(item["Frame Name"])
        book_author_node.appendChild(book_author_value)
        book_node.appendChild(book_author_node)

        root_node.appendChild(book_node)

    f = open(outfile, "w")
    f.write(doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
    f.close()


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


def dataset_analysis_generate_plot(mode,input_file, id_set):
    if mode is 1:
        for j in range(0, len(id_set)):
            print (j,len(id_set))
            time_step = []
            time_stamp = []
            with open(input_file, 'rb') as csvfile:
                spamreader = csv.reader(csvfile)
                i = 0
                while True:
                    try:
                        list_temp = spamreader.next()
                        if list_temp is not None:
                            if list_temp[1] == id_set[j]:
                                if i is 0:
                                    time_stamp.append(string.atof(list_temp[0]))
                                else:
                                    k = string.atof(list_temp[0])
                                    l = string.atof(time_stamp[len(time_step) - 1])
                                    time_stamp.append(string.atof(list_temp[0]))
                                    m = k - l
                                    time_step.append(m)
                                i += 1

                    except StopIteration:
                        break
                if j == 0:
                    plt.plot(range(0, len(time_step), 1), time_step , 'go')
                elif j == 1:
                    plt.plot(range(0, len(time_step), 1), time_step, 'ro')

        plt.ylabel("Interval (ms)")
        plt.xlabel("count")

        # plt.axis([0, 6, 0, 20])
        plt.show()
    else:
        return


def dataset_analysis(input_file):
    analysis_result = {}
    sum = 0
    if input_file == '':
        wx.MessageBox("Please select file!", "Message", wx.OK | wx.ICON_INFORMATION)
        return

    with open(input_file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        while True:
            try:
                list_temp = spamreader.next()
                if list_temp is not None:
                    id = list_temp[1]
                    if not analysis_result.has_key(id):
                        analysis_result[id] = 1
                    else:
                        analysis_result[id] += 1
            except StopIteration:
                break

    if analysis_result is not None:
        frame.m_listBox2.Clear()
        for key in analysis_result:
            frame.m_listBox2.Append("ID:"+key+"; Count:"+str(analysis_result[key]))
            sum += analysis_result[key]
    print sum


# Data Convert
def can_data_convert(input_file, output_file_name, out_file_format, output_file_path):
    extent = Tool.GetFileNameAndExt(input_file)
    if input_file == '':
        wx.MessageBox("Please select file!", "Message", wx.OK | wx.ICON_INFORMATION)
        return
    if out_file_format == '':
        wx.MessageBox("Please select file!", "Message", wx.OK | wx.ICON_INFORMATION)
        return
    if output_file_path == '':
        wx.MessageBox("Please input the path!", "Message", wx.OK | wx.ICON_INFORMATION)
        return
    if extent == out_file_format:
        wx.MessageBox("Convert format must be different!", "Message", wx.OK | wx.ICON_INFORMATION)
        return
    output = "%s\\%s%s" % (output_file_path, output_file_name, out_file_format)

    with sqlite3.connect(input_file) as connection:
        csvWriter = csv.writer(open(output, "w"))
        c = connection.cursor()
        rows = c.execute("SELECT * FROM Packets")
        t = time.time()
        for x in rows:
            csvWriter.writerow(x)
        print time.time()-t


class File():
    def __init__(self, path):
        # self.path = path
        self.logfile = open(path+"\\mydata5.log", 'w')

    def writemsg(self, timestamp, canid, data, dir):
        self.logfile.write("Time:" + str(timestamp) + ",ID:" + str(canid) + ",Data:" + data + ",Dir:"+ dir + '\n')

    def close_file(self):
        self.logfile.close()

app = wx.App()
frame = CalcFrame(None)
# Define the bus instance
bus = None
canReader = None
canPlayer = None
logfile = None
timer1 = None
timer2 = None
timerSpoofing = None
frame.Show(True)
# start the applications
app.MainLoop()
