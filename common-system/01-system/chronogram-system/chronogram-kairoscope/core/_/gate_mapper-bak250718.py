# /core/gate_mapper.py

def longitude_to_gate_line(longitude):
    """
    黄経度（0〜360°）をHDのゲート番号とライン番号に変換
    Returns: (gate_number: int, line_number: int)
    """
    longitude = longitude % 360
    gate_size = 360 / 64  # 5.625°
    line_size = gate_size / 6  # 約0.9375°
    gate_number = int(longitude / gate_size) + 1  # 1始まりのゲート番号
    within_gate_deg = longitude % gate_size
    line_number = int(within_gate_deg / line_size) + 1
    return gate_number, line_number

def get_gate_and_line(ecliptic_longitude):
    # 例：仮のロジック（あとで正式な境界データに差し替え）
    gate, line = longitude_to_gate_line(ecliptic_longitude)
    return {"gate": gate, "line": line}

# ✅ テスト用コード（削除してもOK、検証用）
if __name__ == "__main__":
    lon = 121.72
    gate, line = longitude_to_gate_line(lon)
    print(f"黄経 {lon}° → Gate {gate} / Line {line}")



