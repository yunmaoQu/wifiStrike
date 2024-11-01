from scapy.all import *
from scapy.layers.dot11 import Dot11
import logging

logging.basicConfig(level=logging.INFO)

def station_enumeration(saved_networks):
    stations = set()

    def packet_handler(packet):
        if packet.haslayer(Dot11):
            if packet.type == 2 and packet.addr2 and packet.addr3:  # Data frame
                if packet.addr3 in saved_networks:  # AP's MAC address
                    if packet.addr2 not in stations:
                        stations.add(packet.addr2)
                        logging.info(f"Station found: {packet.addr2} on AP: {packet.addr3}")

    sniff(iface="wlan0mon", prn=packet_handler, store=0)