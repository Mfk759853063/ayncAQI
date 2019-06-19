#!/bin/bash
nohup python -u main.py &
echo $! > save_pid.txt
