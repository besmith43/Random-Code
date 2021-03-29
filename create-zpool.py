#!/usr/bin/env python3

import os
import subprocess
import locale
from dialog import Dialog

def get_local_drives():
	drive_path = "/dev/disk/by-path/"
	disk1_1 = ""
	disk1_2 = ""
	disk1_3 = ""
	disk1_4 = ""
	disk2_1 = ""
	disk2_2 = ""
	disk2_3 = ""
	disk2_4 = ""
	disk3_1 = ""
	disk3_2 = ""
	disk3_3 = ""
	disk3_4 = ""
	bootdisk = ""

def main():
    locale.setlocale(locale.LC_ALL, '')

    d = Dialog(dialog="dialog")
    d.set_background_title("ZFS Pool Creation")

    code, tag = d.radiolist("What Raid mode do you want for the ZFS pool?",
                choices=[("raidz","",False),
                         ("raidz2","",False),
                         ("raidz3","",False),
                         ("mirror","",False)])

    if code == d.OK:
        zpool_raid = tag
    else:
        subprocess.run("clear")
        return

    code, tag = d.checklist("Which disks do you want in the zpool?",
                choices=[("disk1-1","",False),
                         ("disk1-2","",False),
                         ("disk1-3","",False),
                         ("disk1-4","",False),
                         ("disk2-1","",False),
                         ("disk2-2","",False),
                         ("disk2-3","",False),
                         ("disk2-4","",False),
                         ("disk3-1","",False),
                         ("disk3-2","",False),
                         ("disk3-3","",False),
                         ("disk3-4","",False)])

    if code == d.OK:
        subprocess.run("clear")
        zpool_disks = tag
    else:
        return

    code, tag = d.inputbox("What would you like to call the zpool?")

    if code == d.OK:
        subprocess.run("clear")
        zpool_name = tag
    else:
        return

    subprocess.run("clear")

    print("sudo zpool create " + zpool_name + " " + zpool_raid + " " + " ".join(zpool_disks))



if __name__ == "__main__":
    main()
