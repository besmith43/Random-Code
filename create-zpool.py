#!/usr/bin/env python3

import os
import subprocess
import locale
import datetime
from dialog import Dialog

def clear():
    subprocess.run("clear")

def get_local_drives():
    drive_path = "/dev/disk/by-path/"
    disk1_1 = drive_path + "pci-0000:00:1f.2-ata-2"
    disk1_2 = drive_path + "pci-0000:00:1f.2-ata-3"
    disk1_3 = drive_path + "pci-0000:00:1f.2-ata-4"
    disk1_4 = drive_path + "pci-0000:00:1f.2-ata-5"
    disk2_1 = drive_path + "pci-0000:01:00.0-sas-phy0-lun-0"
    disk2_2 = drive_path + "pci-0000:01:00.0-sas-phy1-lun-0"
    disk2_3 = drive_path + "pci-0000:01:00.0-sas-phy2-lun-0"
    disk2_4 = drive_path + "pci-0000:01:00.0-sas-phy3-lun-0"
    disk3_1 = drive_path + "pci-0000:01:00.0-sas-phy4-lun-0"
    disk3_2 = drive_path + "pci-0000:01:00.0-sas-phy5-lun-0"
    disk3_3 = drive_path + "pci-0000:01:00.0-sas-phy6-lun-0"
    disk3_4 = drive_path + "pci-0000:01:00.0-sas-phy7-lun-0"
    bootdisk = drive_path + "pci-0000:00:1f.2-ata-1"

    return [("disk1_1", disk1_1, False),("disk1_2", disk1_2, False),("disk1_3", disk1_3, False),("disk1_4", disk1_4, False),("disk2_1", disk2_1, False),("disk2_2", disk2_2, False),("disk2_3", disk2_3, False),("disk2_4", disk2_4, False),("disk3_1", disk3_1, False),("disk3_2", disk3_2, False),("disk3_3", disk3_3, False),("disk3_4", disk3_4, False)]

def translate_tags(tags):
    # switch state that appends the disk1_1 to the drive path value
    choices = []
    drive_path = "/dev/disk/by-path/"
    for tag in tags:
        if tag == "disk1_1":
            choices.append(drive_path + "pci-0000:00:1f.2-ata-2")
        elif tag == "disk1_2":
            choices.append(drive_path + "pci-0000:00:1f.2-ata-3")
        elif tag == "disk1_3":
            choices.append(drive_path + "pci-0000:00:1f.2-ata-4")
        elif tag == "disk1_4":
            choices.append(drive_path + "pci-0000:00:1f.2-ata-5")
        elif tag == "disk2_1":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy0-lun-0")
        elif tag == "disk2_2":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy1-lun-0")
        elif tag == "disk2_3":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy2-lun-0")
        elif tag == "disk2_4":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy3-lun-0")
        elif tag == "disk3_1":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy4-lun-0")
        elif tag == "disk3_2":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy5-lun-0")
        elif tag == "disk3_3":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy6-lun-0")
        elif tag == "disk3_4":
            choices.append(drive_path + "pci-0000:01:00.0-sas-phy7-lun-0")

    return " ".join(choices)

def save_command(command, log_path):
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    filename = log_path + datetime.datetime.now().strftime("%m_%d_%Y_log.txt")

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'

    log_file = open(filename, append_write)
    log_file.write(command + " - " + datetime.datetime.now().strftime("%X") + "\n")
    log_file.close()

def main():
    locale.setlocale(locale.LC_ALL, '')

    d = Dialog(dialog="dialog",autowidgetsize=True)
    d.set_background_title("ZFS Pool Creation")

    code, tag = d.radiolist("What Raid mode do you want for the ZFS pool?",
                choices=[("raidz","",False),
                         ("raidz2","",False),
                         ("raidz3","",False),
                         ("mirror","",False)])

    if code == d.OK:
        zpool_raid = tag
    else:
        clear()
        return

    code, tag = d.checklist("Which disks do you want in the zpool?",
                choices=get_local_drives())

    if code == d.OK:
        clear()
        zpool_disks = tag
    else:
        return

    code, tag = d.inputbox("What would you like to call the zpool?")

    if code == d.OK:
        clear()
        zpool_name = tag
    else:
        return

    clear()

    command = "sudo zpool create " + zpool_name + " " + zpool_raid + " " + translate_tags(zpool_disks)

    if d.yesno("Is this command correct? \n" + command) == d.OK:
        clear()
        save_command(command, "/home/besmith/.logs/create_zpool/")
        subprocess.run(command.split(" "))
        subprocess.run(["sudo", "zpool", "set", "compression=gzip-9", zpool_name])
        print("zpool successfully created")
    else:
        clear()

if __name__ == "__main__":
    main()
