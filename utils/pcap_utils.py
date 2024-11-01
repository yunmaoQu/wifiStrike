import subprocess
from scapy.utils import wrpcap
def save_pcap(handshake_packets, save_path):
    wrpcap(save_path, handshake_packets)
    print(f"Handshake saved to {save_path}")

def convert_to_hc22000(pcap_file, hcx_tool_path, output_file):
    try:
        subprocess.run([hcx_tool_path, pcap_file, "-o", output_file], check=True)
        print(f"Converted {pcap_file} to {output_file}")
    except subprocess.CalledProcessError:
        print("Error converting pcap to hc22000 format")