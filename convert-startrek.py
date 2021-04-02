#!/usr/bin/env python3

import os
import subprocess
import enum

class SIZE_UNIT(enum.Enum):
	BYTES = 1
	KB = 2
	MB = 3
	GB = 4

def convert_unit(size_in_bytes, unit):
	if unit == SIZE_UNIT.KB:
		return size_in_bytes/1024
	elif unit == SIZE_UNIT.MB:
		return size_in_bytes/(1024*1024)
	elif unit == SIZE_UNIT.GB:
		return size_in_bytes/(1024*1024*1024)
	else:
		return size_in_bytes

def get_file_size(file_path, size_type = SIZE_UNIT.MB):
	size = os.path.getsize(file_path)
	return convert_unit(size, size_type)

def get_video_file(directory):
	working_directory = os.getcwd() + '/' + directory
	files = [f for f in os.listdir(working_directory) if os.path.isfile(os.path.join(working_directory, f))]
	largest_file = files[0]

	for file in files:
		if largest_file == file:
			pass
		elif get_file_size(working_directory + '/' + file) > get_file_size(working_directory + '/' + largest_file):
			largest_file = file
		
	if ".mkv" in largest_file:
		return working_directory + '/' + largest_file
	else:
		return -1

def get_output_video_file_name(directory):
	return directory[:20].replace('.',' ',2).replace('.','-').replace("TNG", "The Next Generation") + ".mp4"

def convert_video(input_file_name, output_file_name):
	print(["ffmpeg", "-i", input_file_name, "-vcodec", "libx265", "-crf", "28", output_file_name])
	subprocess.run(["ffmpeg", "-i", input_file_name, "-vcodec", "libx265", "-crf", "28", output_file_name])
	
def main():
	pwd = os.getcwd()

	subdirectories = os.listdir(pwd)

	for subdirectory in subdirectories:
		if "Season" not in subdirectory:
			print(subdirectory)
			video_file = get_video_file(subdirectory)
			output_video_file = pwd + '/' + get_output_video_file_name(subdirectory)

			if video_file == -1:
				print("no video file found")
			else:
				convert_video(video_file, output_video_file)

if __name__ == "__main__":
	main()
