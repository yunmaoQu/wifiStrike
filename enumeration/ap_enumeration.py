from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt
import logging

logging.basicConfig(level=logging.INFO)

def ap_enumeration():
    ap_list = set()

    def packet_handler(packet):
        if packet.haslayer(Dot11Beacon):
            ssid = packet.info.decode('utf-8', errors='ignore')  # 获取 SSID
            bssid = packet[Dot11].addr3  # 获取 AP 的 MAC 地址
            if (ssid, bssid) not in ap_list:
                ap_list.add((ssid, bssid))
                channel = int(ord(packet[Dot11Elt:3].info))
                logging.info(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}")

    sniff(iface="wlan0mon", prn=packet_handler, store=0)