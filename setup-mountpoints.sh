#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "This script needs to be run with sudo"
	exit 1
fi

if [ ! -d /mnt/nas/books ]; then
	mkdir -p /mnt/nas/books
fi

if [ ! -d /mnt/nas/budget ]; then
	mkdir -p /mnt/nas/budget
fi

if [ ! -d /mnt/nas/development ]; then
	mkdir -p /mnt/nas/development
fi

if [ ! -d /mnt/nas/docker ]; then
	mkdir -p /mnt/nas/docker
fi

if [ ! -d /mnt/nas/docs ]; then
	mkdir -p /mnt/nas/docs
fi

if [ ! -d /mnt/nas/home ]; then
	mkdir -p /mnt/nas/home
fi

if [ ! -d /mnt/nas/music ]; then
	mkdir -p /mnt/nas/music
fi

if [ ! -d /mnt/nas/photo ]; then
	mkdir -p /mnt/nas/photo
fi

if [ ! -d /mnt/nas/podcast ]; then
	mkdir -p /mnt/nas/podcast
fi

if [ ! -d /mnt/nas/video ]; then
	mkdir -p /mnt/nas/video
fi

if [ ! -d /mnt/servers/bulk ]; then
	mkdir -p /mnt/servers/bulk
fi

if [ ! -d /mnt/servers/movies ]; then
	mkdir -p /mnt/servers/movies
fi

if [ ! -d /mnt/servers/tv_shows ]; then
	mkdir -p /mnt/servers/tv_shows
fi

if [ ! -d /mnt/sshfs ]; then
	mkdir -p /mnt/sshfs
fi
