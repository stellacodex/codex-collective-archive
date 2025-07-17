# core/channel_center.py

def get_active_channels_and_centers(gates, channel_defs):
    """
    ゲートペアからアクティブチャネルと定義センターを返す（簡易版）
    :param gates: dict, e.g. {"Sun": {"gate": 1, "line": 2}, ...}
    :param channel_defs: list of channel definitions
    :return: (active_channels: list, defined_centers: list)
    """
    # どのゲートが活性化されているか抽出
    active_gate_nums = {g["gate"] for g in gates.values()}
    active_channels = []
    defined_centers = set()

    for ch in channel_defs:
        gate_a, gate_b = [int(g) for g in ch["gates"]]
        if gate_a in active_gate_nums and gate_b in active_gate_nums:
            active_channels.append(ch["channel"])
            defined_centers.update(ch["centers"])

    return active_channels, list(defined_centers)
