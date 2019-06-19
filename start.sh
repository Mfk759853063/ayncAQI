#!/bin/bash
nohup python3 -u main.py &
echo $! > save_pid.txt
