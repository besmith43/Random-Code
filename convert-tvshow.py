#!/usr/bin/env python3

import os
import subprocess


def main():
    pwd = os.getcwd()

    files = [f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f))]

    for file in files:
        subprocess.run(["ffmpeg", "-i", file, "-vcodec", "libx265", file[:len(file)-3]+"mp4"])

if __name__ == "__main__":
	main()
