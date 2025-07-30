from loader import load_gate_definitions, load_channel_definitions

def test_loader():
    gate_defs = load_gate_definitions()
    channel_defs = load_channel_definitions()

    gate_dict = {g["gate"]: g for g in gate_defs}
    channel_dict = {c["channel"]: c for c in channel_defs}

    print("✅ Gate 定義数:", len(gate_defs))
    print("✅ Channel 定義数:", len(channel_defs))

    # 確認用に最初のGateとChannelを出力
    print("🔍 Gate 1:", gate_dict.get(1))
    print("🔍 Channel 1-8:", channel_dict.get("1-8"))

if __name__ == "__main__":
    test_loader()
