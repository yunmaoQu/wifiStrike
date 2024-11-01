# 常量定义
TO_DS_FLAG = 0b01
FROM_DS_FLAG = 0b10

# 用于表示数据包状态的枚举
class PacketStatus:
    HANDSHAKE_CAPTURED = "Handshake Captured"
    DEAUTH_SENT = "Deauth Sent"
    STATION_FOUND = "Station Found"