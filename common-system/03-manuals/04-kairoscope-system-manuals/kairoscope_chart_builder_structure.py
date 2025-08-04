import json
from core.astro.astro_position import get_astro_positions
from core.gate_mapper import map_longitude_to_gate_line
from core.definitions import gate_definitions, channel_definitions
from core.profile_logic import determine_profile
from core.authority_logic import calculate_authority
from core.channel_center import find_active_channels, determine_centers

def build_chart(birth_data):
    # Step 1: 惑星の黄経取得
    planet_positions = get_astro_positions(birth_data)

    # Step 2: ゲート＋ラインへの変換
    gates = {}
    for planet, longitude in planet_positions.items():
        gate, line = map_longitude_to_gate_line(longitude)
        gates[planet] = {
            "gate": gate,
            "line": line
        }

    # Step 3: プロファイル・権威（暫定）
    profile = determine_profile(gates)
    authority = calculate_authority(gates)

    # Step 4: チャネル・センターの抽出
    active_channels = find_active_channels(gates)
    centers = determine_centers(active_channels)

    # Step 5: 統合チャートデータの構築
    chart = {
        "planet_positions": planet_positions,
        "gates": gates,
        "profile": profile,
        "authority": authority,
        "active_channels": active_channels,
        "centers": centers
    }

    return chart

# オプション：JSONとして保存
def save_chart(chart, filename="output/chart.json"):
    with open(filename, "w") as f:
        json.dump(chart, f, indent=2, ensure_ascii=False)

# テスト用
if __name__ == "__main__":
    dummy_birth = {
        "date": "1983-05-01",
        "time": "12:00",
        "timezone": "Asia/Tokyo",
        "latitude": 35.6895,
        "longitude": 139.6917
    }
    chart = build_chart(dummy_birth)
    save_chart(chart)
