#!/bin/bash

#Source the variables
source ../ssh_config.bash

#First copy the necessary files to the server
scp -r $LOCAL_DIR/* $REMOTE_SERVER:$REMOTE_DIR