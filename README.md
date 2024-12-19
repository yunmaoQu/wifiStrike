
### 目录结构

```plaintext
wifi_tool/                      # 项目主目录
│
├── config.py                   # 配置文件：包含所有配置参数和环境变量
├── enums.py                    # 常量和枚举定义
├── main.py                     # 主程序入口
│
├── attacks/                    # 攻击功能模块目录
│   ├── deauth_attack.py        # Deauthentication 攻击模块
│   ├── wpa_handshake.py        # WPA 握手捕获模块
│   
├── enumeration/                # 枚举功能模块目录
│   ├── ap_enumeration.py       # WiFi 网络 (AP) 枚举模块
│   ├── station_enumeration.py  # WiFi 连接设备 (Station) 枚举模块
│
├── utils/                      # 辅助工具函数目录
│   ├── pcap_utils.py           # 保存和转换 PCAP 文件的工具函数
│   ├── webhook.py              # Webhook 通知模块
│   ├── send_to_endpoint.py     # 发送数据到远程服务器的工具函数
│   └── logging_utils.py        # 日志记录和调试工具函数
│
├── tests/                      # 测试目录
│   ├── test_ap_enumeration.py  # WiFi 枚举模块的单元测试
│   ├── test_deauth_attack.py   # Deauth 攻击模块的单元测试
│   ├── test_handshake.py       # 握手捕获模块的单元测试
│   └── test_utils.py           # 工具函数的单元测试
│
├── data/                       # 数据存储目录
│   ├── handshakes/             # 捕获到的 WPA 握手包 (PCAP 文件)
│   └── converted/              # 转换后的 Hashcat 格式文件 (hc22000)
│
├── docs/                       # 文档目录
│   ├── README.md               # 项目使用说明和部署文档
│   └── INSTALL.md              # 安装和依赖配置说明
│
├── requirements.txt            # Python 依赖文件
├── .env                        # 环境变量文件
├── .gitignore                  # Git 忽略文件
└── LICENSE                     # 项目许可证
```

### 目录结构详细说明

1. **`config.py`**:  
   - 包含所有的配置参数和环境变量，便于集中管理配置。通过 `os.getenv` 来加载环境变量，也可以通过 `.env` 文件进行配置。

2. **`enums.py`**:  
   - 定义一些常量和枚举，用于标识数据包的状态或其他常量值。比如 Deauth 攻击标志、握手捕获状态等。

3. **`main.py`**:  
   - 主程序入口，负责解析命令行参数并调用其他模块。处理主要的逻辑流程，如枚举网络、执行攻击、捕获握手等。

4. **`attacks/`**:  
   - 存放与攻击相关的模块代码：
     - `deauth_attack.py`: 实现 Deauthentication 攻击的逻辑。
     - `wpa_handshake.py`: 实现捕获 WPA 握手的功能模块。

5. **`enumeration/`**:  
   - 存放与枚举功能相关的模块代码：
     - `ap_enumeration.py`: 实现 WiFi 网络 (AP) 的枚举逻辑。
     - `station_enumeration.py`: 实现连接到 WiFi 网络的设备 (Station) 枚举。

6. **`utils/`**:  
   - 存放辅助工具函数，用于处理常见的功能，如保存和转换文件、发送 Webhook 通知、日志记录等：
     - `pcap_utils.py`: 保存捕获的握手包并将其转换为 Hashcat 所需的 hc22000 格式。
     - `webhook.py`: 通过 Webhook 发送通知。
     - `send_to_endpoint.py`: 将握手包发送到远程服务器。
     - `logging_utils.py`: 提供日志记录和调试工具。

7. **`tests/`**:  
   - 存放项目的测试代码，用于对各个模块进行单元测试，确保功能正确：
     - `test_ap_enumeration.py`: 测试 AP 枚举模块。
     - `test_deauth_attack.py`: 测试 Deauth 攻击模块。
     - `test_handshake.py`: 测试 WPA 握手捕获模块。
     - `test_utils.py`: 测试工具函数的正确性。

8. **`data/`**:  
   - 存放运行过程中生成的文件和数据，包括捕获的握手包和转换后的 Hashcat 格式文件：
     - `handshakes/`: 存储捕获的 WPA 握手包 (PCAP 文件)。
     - `converted/`: 存储转换后的 Hashcat 格式文件 (hc22000)。

9. **`docs/`**:  
   - 文档目录，包含项目的使用说明、安装指南、架构设计等文档：
     - `README.md`: 项目总览和使用说明。
     - `INSTALL.md`: 安装依赖及环境配置的详细说明。

10. **`requirements.txt`**:  
    - 列出了项目的所有 Python 依赖库，可以使用 `pip install -r requirements.txt` 安装依赖。

11. **`.env`**:  
    - 环境变量文件，敏感或可配置的变量可以放在此文件中，避免硬编码。

12. **`.gitignore`**:  
    - 指定哪些文件和目录不应提交到 Git 版本控制中，例如临时文件、虚拟环境、日志文件等。

13. **`LICENSE`**:  
    - 项目的开源许可证，为项目的法律使用条款。
