#!/usr/bin/env python3

import os
import subprocess

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

def get_files(pwd):
    return [f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f))]

def overwrite():
    if platform == "win32":
        answer = input("Would you like to overwrite the original files? (y/N)")
        if answer == "y":
            return True
        else:
            return False
    else:
        d = Dialog(dialog="dialog")
        d.set_background_title("Convert TV Show")

        if d.yesno("Would you like to overwrite the original files?") == d.OK:
            return True
        else:
            return False

def save_type():
    if platform == "win32":
        answer = input("Would you like to convert this file to mp4? (y/N) \nif not, it will be saved as mkv")
        if answer == "y":
            return "mp4"
        else:
            return "mkv"
    else:
        d = Dialog(dialog="dialog")
        d.set_background_title("Convert TV Show")

        if d.yesno("Would you like to convert this file to mp4? (y/N) \nif not, it will be saved as mkv") == d.OK:
            return "mp4"
        else:
            return "mkv"


def main():
    if platform == "linux" or platform == "linux2":
        module_exists("from dialog import Dialog")
    
    files = get_files(os.getcwd())

    if save_type() == "mp4":
        extension = "-libx265.mp4"
    else:
        extension = "-libx265.mkv"

    overwrite_flag = overwrite()

    for file in files:
        new_file = file[:len(file)-4]+"-libx265.mp4"
        
        if overwrite_flag:
            subprocess.run(["ffmpeg", "-y", "-i", file, "-vcodec", "libx265", "-acodec", "copy", "-scodec", "copy", new_file])
        else:
            subprocess.run(["ffmpeg", "-i", file, "-vcodec", "libx265", "-acodec", "copy", "-scodec", "copy", new_file])

if __name__ == "__main__":
    main()
