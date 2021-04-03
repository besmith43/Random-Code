#!/usr/bin/env python3

import os
import subprocess
import platform
import datetime
from dialog import Dialog

def get_files(pwd):
    return [f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f))]

def overwrite(d):
    if d.yesno("Would you like to overwrite the original files?") == d.OK:
        return True
    else:
        return False

def save(d):
    code, path = d.dselect("/",height=10)

    if code == d.OK:
        return path
    else:
        return ""

def write_to_file(command, log_path):
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    filename = log_path + datetime.datetime.now().strftime("%m_%d_%Y_log.txt")

    print("Log File: " + filename)

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'

    log_file = open(filename, append_write)
    log_file.write(command + " - " + datetime.datetime.now().strftime("%X") + "\n")
    log_file.close()

def main():
    d = Dialog(dialog="dialog", autowidgetsize=True)
    d.set_background_title("Convert Videos")
    
    files = get_files(os.getcwd())

    overwrite_flag = overwrite(d)

    save_folder = save(d)

    for file in files:
        new_file = save_folder + file[:len(file)-4]+"-libx265-slow-qp21"+file[-4:]
        #print(file)

        command = ["ffmpeg"]
        
        if overwrite_flag:
            command.append("-y")

        command.append("-i")
        command.append(file)
        command.append("-vcodec")
        command.append("libx265")
        command.append("-acodec")
        command.append("copy")
        command.append("-scodec")
        command.append("copy")
        command.append("-qp")
        command.append("21")
        command.append("-preset")
        command.append("slow")
        command.append(new_file)

        command_str = " ".join(command)

        print("Running the following command\n" + command_str)
        write_to_file(command_str, "/home/besmith/.logs/convert-videos/")
        #subprocess.run(command_str)

if __name__ == "__main__":
    main()
