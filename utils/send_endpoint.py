import os
import requests
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量中获取远程服务器的 URL 和 API 密钥
ENDPOINT_URL = os.getenv('ENDPOINT_URL')
API_KEY = os.getenv('API_KEY')

def send_handshake_to_server(file_path):
    """将握手包文件发送到远程服务器"""
    if not ENDPOINT_URL:
        raise ValueError("远程服务器的 ENDPOINT_URL 未设置")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件 {file_path} 不存在")
    
    headers = {
        'Authorization': f'Bearer {API_KEY}'  # 使用 Bearer 令牌进行身份验证
    }
    
    files = {
        'file': open(file_path, 'rb')  # 以二进制模式打开文件
    }
    
    try:
        print(f"正在将握手包 {file_path} 发送到 {ENDPOINT_URL} ...")
        response = requests.post(ENDPOINT_URL, files=files, headers=headers)
        
        if response.status_code == 200:
            print(f"文件 {file_path} 成功发送到服务器！")
        else:
            print(f"发送失败，服务器返回状态码: {response.status_code}")
            print(f"服务器响应内容: {response.text}")
    except requests.RequestException as e:
        print(f"发送文件时出现错误: {e}")
    finally:
        files['file'].close()  # 关闭文件

# 示例用法
if __name__ == "__main__":
    handshake_file = "./handshakes/test_handshake.pcap"
    send_handshake_to_server(handshake_file)