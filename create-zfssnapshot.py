#!/usr/bin/env python3

import argh
import subprocess

# the commands to create and list zfs snapshots
#
# to create a snapshot
# sudo zfs snapshot volume@snapshot-name
#
# example
# sudo zfs snapshot vol1-bulk@backup1
#
# to list snapshots
# zfs list -t snapshots
#
# to list zfs pools
# zfs list
#
# to rename zfs snapshots
# zfs rename volume@snapshot-current-name volume@snapshot-new-name
#
# example
# sudo zfs rename vol1-bulk@backup1 vol1-bulk@backup2
#
#

def get_snapshots():
    snapshots = subprocess.run(['zfs','list','-t','snapshot'],capture_output=True,text=True)
    snapshots_arr = []
    for i in range(1,len(snapshots)):
        snapshots_arr.append(snapshots[i].split()[0])

    return snapshots_arr

def main():

if __name__ == "__main__":
    argh.dispatch_command(main)
