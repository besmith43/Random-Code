#!/usr/bin/env python3

import os
import subprocess
import datetime
import shutil
from dialog import Dialog

def get_files(pwd):
    return [f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f))]

def get_folders(pwd):
    return [d for d in os.listdir(pwd) if os.path.isdir(os.path.join(pwd, d))]

def overwrite(d):
    if d.yesno("Would you like to overwrite the original files?") == d.OK:
        return True
    else:
        return False

def copy(d):
    if d.yesno("Would you like to copy the original file if there is any errors?") == d.OK:
        return True
    else:
        return False

def save(d):
    code, path = d.dselect("/",height=10)

    if code == d.OK:
        return path
    else:
        return ""

def recursive(d):
    if d.yesno("Would you like to operate recursively?") == d.OK:
        return True
    else:
        return False

def run_recursively(pwd, overwrite_flag, save_folder, copy_if_error=False):
    folders = get_folders(pwd)

    for folder in folders:
        if not os.path.exists(save_folder + folder):
            os.mkdir(save_folder + folder)
            print("making folder: " + save_folder + folder)

        run_recursively(pwd + folder + "/", overwrite_flag, save_folder + folder + "/")

    files = get_files(pwd)

    for video_file in files:
        convert_video(video_file, overwrite_flag, pwd, save_folder, copy_if_error)

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

def write_error_to_file(result, log_path):
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    filename = log_path + datetime.datetime.now().strftime("%m_%d_%Y_errors_log.txt")

    print("Log File: " + filename)

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'

    log_file = open(filename, append_write)
    log_file.write(" ".join(result.args) + "\n\n" + " ".join(result.stderr) + "\n\n" + " - " + datetime.datetime.now().strftime("%X") + "\n")
    log_file.close()

def convert_video(video_file, overwrite_flag, pwd, save_folder, copy_if_error=False):
    if video_file[-4:] == ".mp4" or video_file[-4:] == ".mkv":
        new_file = save_folder + video_file[:len(video_file)-4]+"-libx265-slow-qp21"+video_file[-4:]
        command = ["ffmpeg"]
        
        if overwrite_flag:
            command.append("-y")
        else:
            command.append("-n")

        command.append("-i")
        command.append(pwd + video_file)
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
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 1:
            print("Transcode exited with errors")
            write_error_to_file(result, "/home/besmith/.logs/convert-videos/")
            os.remove(new_file)
            if copy_if_error:
                print("Copying original to destination")
                shutil.copy(pwd + video_file, save_folder + video_file)
                print("Copy complete")
        else:
            print("Transcode Completed")

def main():
    d = Dialog(dialog="dialog", autowidgetsize=True)
    d.set_background_title("Convert Videos")

    overwrite_flag = overwrite(d)

    copy_if_error = copy(d)

    save_folder = save(d)

    if recursive(d):
        pwd = os.getcwd() + "/"
        run_recursively(pwd, overwrite_flag, save_folder, copy_if_error)
    else:
        files = get_files(os.getcwd())

        for file in files:
            convert_video(file, overwrite_flag, os.getcwd(), save_folder, copy_if_error)

if __name__ == "__main__":
    main()
