#!/bin/bash
# This script sets up and sends out a P4 Trigger packet to a Jenkins server using cURL.

CHANGE=$1
P4PORT=PERFORCE_SERVER_IP:PORT

JUSER=USERNAME
JPASS=PASSWORD
JSERVER=http://JENKINS_SERVER_IP:PORT

curl --header 'Content-Type: application/json' \
     --request POST \
     --user $JUSER:$JPASS \
     --data payload="{change:$CHANGE,p4port:\"$P4PORT\"}" \
     $JSERVER/p4/change
