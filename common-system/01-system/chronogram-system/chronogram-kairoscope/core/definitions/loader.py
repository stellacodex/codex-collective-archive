# core/definitions/loader.py
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_gate_definitions(filename="gate-definitions.json"):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Gate definitions file not found at: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def load_channel_definitions(filename="channel-definitions.json"):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Channel definitions file not found at: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    gate_defs = load_gate_definitions()
    gate_dict = {g["gate"]: g for g in gate_defs}          # intキーで辞書化
    channel_defs = load_channel_definitions()
    hannel_dict = {c["channel"]: c for c in channel_defs} # 文字列キーで辞書化


    print(f"✅ Gate 定義数: {len(gate_defs)}")
    print(f"✅ Channel 定義数: {len(channel_defs)}")
    print("🔍 Gate 1:", gate_dict.get(1))
    print("🔍 Channel 1-8:", channel_dict.get("1-8"))
