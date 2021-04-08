#!/bin/bash

sudo mount -t glusterfs 10.0.1.160:/bulk /mnt/servers/bulk
sudo mount -t glusterfs 10.0.1.164:/movies /mnt/servers/movies
sudo mount -t glusterfs 10.0.1.164:/tv_shows /mnt/servers/tv_shows
