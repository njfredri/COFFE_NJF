#!/bin/bash

#source the file to save the variables

# Define variables
REMOTE_SERVER="username@remote_server_address"
REMOTE_DIR="/path/to/remote/directory"
LOCAL_DIR="/path/to/local/directory"
TCL_SCRIPT="my_script.tcl"

# Transfer input files to remote server
scp -r $LOCAL_DIR/* $REMOTE_SERVER:$REMOTE_DIR

# Execute Cadence EDI on the remote server
ssh $REMOTE_SERVER "cd $REMOTE_DIR && encounter -init $TCL_SCRIPT"

# Retrieve output files back to local machine
scp -r $REMOTE_SERVER:$REMOTE_DIR/output/* $LOCAL_DIR/output
