#!/usr/bin/env python3

import argh

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


def main():

if __name__ == "__main__":
    argh.dispatch_command(main)
