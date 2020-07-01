#!/bin/bash
# This shell script is intended to be executed by a Perforce trigger with a commited change number. All it does is run a Python script.

CHANGE=$1

python /opt/perforce/triggers/scripts/discord_post_p4commit.py -c $CHANGE
