from scapy.all import *
from scapy.layers.dot11 import Dot11
import logging

logging.basicConfig(level=logging.INFO)

def capture_handshake(ap_mac, iface="wlan0mon", timeout=60):
    handshake_packets = []
    
    def packet_handler(packet):
        if packet.haslayer(Dot11):
            if packet.addr1 == ap_mac or packet.addr2 == ap_mac:
                # 假设这是 WPA 握手包的部分
                handshake_packets.append(packet)
                if len(handshake_packets) >= 4:  # 捕获到4个握手包
                    logging.info("WPA Handshake captured!")
                    return True

    sniff(iface=iface, prn=packet_handler, timeout=timeout)
    return handshake_packets