import os
import xml.etree.ElementTree as ET


class Tool():

    @staticmethod
    def GetFileNameAndExt(filename):
        (filepath, tempfilename) = os.path.split(filename)
        (shotname, extension) = os.path.splitext(tempfilename)
        return extension

    @staticmethod
    def getlist(path):
        attack_list = []
        tree = ET.parse(path)
        root = tree.getroot()
        for attack in root:
            # print('child-tag is:',child.tag,',child.attrib:',child.attrib,',child.text:',child.text)
            if attack.attrib["type"] == "DoS":
                # print "1"
                i = 0
                atk = AttackMessage()
                atk.attack_type = 1
                for attack_info in attack:
                    if i == 0:
                        atk.start_t = int(attack_info.text)
                    # print attack_info.text
                    elif i == 1:
                        atk.end_t = int(attack_info.text)
                    i += 1
                # print atk.display_attack()
                attack_list.append(atk)

            if attack.attrib["type"] == "Fuzzing":
                # print "1"
                i = 0
                atk = AttackMessage()
                atk.attack_type = 3
                for attack_info in attack:
                    if i == 0:
                        atk.start_t = int(attack_info.text)
                    elif i == 1:
                        atk.end_t = int(attack_info.text)
                    if i == 2:
                        # print attack_info.attrib["type"]
                        if attack_info.attrib["type"] == "random":
                            atk.msg_type = 1
                            # print "1"
                            j = 0
                            for msg_info in attack_info:
                                if j == 0:
                                    atk.msg_range = msg_info.text
                                j += 1
                        elif attack_info.attrib["type"] == "fixed":
                            atk.msg_type = 2
                            # print "1"
                            j = 0
                            for msg_info in attack_info:
                                if j == 0:
                                    atk.msg_id = int(msg_info.text, 16)
                                elif j == 1:
                                    atk.msg_data = msg_info.text.split(" ")
                                elif j == 2:
                                    atk.msg_fre = int(msg_info.text)
                                j += 1
                    i += 1

                # print atk.display_attack()
                attack_list.append(atk)

            elif attack.attrib["type"] == "Spoofing":
                print "Spoofing"
                i = 0
                atk = AttackMessage()
                atk.attack_type = 2
                for attack_info in attack:
                    if i == 0:
                        atk.start_t = int(attack_info.text)
                        # print attack_info.text
                    elif i == 1:
                        atk.end_t = int(attack_info.text)
                    # print attack_info.text
                    if i == 2:
                        # print attack_info.attrib["type"]
                        if attack_info.attrib["type"] == "fixed":
                            atk.msg_type = 1
                            # print "1"
                            j = 0
                            for msg_info in attack_info:
                                if j == 0:
                                    atk.msg_id = int(msg_info.text, 16)
                                elif j == 1:
                                    atk.msg_data = msg_info.text.split(" ")
                                    pass
                                elif j == 2:
                                    atk.msg_active_bit = int(msg_info.text, 16)
                                elif j == 3:
                                    atk.msg_fre = int(msg_info.text)
                                j += 1

                        elif attack_info.attrib["type"] == "offset":
                            atk.msg_type = 2
                            # print "2"
                            j = 0
                            for msg_info in attack_info:
                                if j == 0:
                                    atk.msg_id = int(msg_info.text, 16)
                                elif j == 1:
                                    atk.msg_data = msg_info.text.split(" ")
                                elif j == 2:
                                    atk.msg_active_bit = int(msg_info.text, 16)
                                elif j == 3:
                                    atk.msg_fre = int(msg_info.text)
                                j += 1

                        elif attack_info.attrib["type"] == "random":
                            atk.msg_type = 3
                            # print "3"
                            for msg_info in attack_info:
                                    atk.msg_fre = int(msg_info.text)

                    i += 1
                attack_list.append(atk)

        return attack_list


class AttackMessage:
    start_t = 0
    end_t = 0
    attack_type = 0
    # type 1 = DoS,type 2 = Spoofing, type 3 = Fuzzing
    msg_type = 0
    # msg_type 1 = fixed, msg_type 2 = offset, msg_type 3 = random
    msg_id = 0
    msg_data = [0, 0, 0, 0, 0, 0, 0, 0]
    msg_active_bit = 0xff
    msg_fre = 100

    msg_range = ""

    # def __init__(self, start_t, end_t, attack_type, msg_typ, msg_id, msg_data, msg_active_bit, msg_fre):
    #     self.start_t = start_t
    #     self.end_t = end_t
    #     self.attack_type = attack_type
    #     self.msg_type = msg_typ
    #     self.msg_id = msg_id
    #     self.msg_data = msg_data
    #     self.msg_active_bit = msg_active_bit
    #     self.msg_fre = msg_fre

    def __init__(self):
        self.start_t =  0
        self.end_t = 0
        self.attack_type = 0
        self.msg_type = 0
        self.msg_id =  0
        self.msg_data = [0, 0, 0, 0, 0, 0, 0, 0]
        self.msg_active_bit = 0xff
        self.msg_fre = 100
        self.msg_range = 100

    def display_attack(self):
        print (str(self.attack_type) + " Attack from " + str(self.start_t) + "-" + str(self.end_t))





