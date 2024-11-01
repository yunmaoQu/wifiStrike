import os

# 配置参数和环境变量
ENDPOINT = os.getenv("ENDPOINT", "https://your-endpoint.com/upload")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your-webhook.com/notify")
MON_IFACE = os.getenv("MON_IFACE", "wlan0mon")  # 监控模式接口
PCAP_SAVE_PATH = os.getenv("PCAP_SAVE_PATH", ".data/handshakes/")
HCX_TOOL_PATH = os.getenv("HCX_TOOL_PATH", "/usr/bin/hcxpcapngtool")