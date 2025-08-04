# chart_builder.py
# --- Kairoscope Chart統合処理 ---

from core.astro.astro_position import get_astro_positions
from core.gate_mapper import map_longitude_to_gate_line
from core.definitions.gate_definitions import GATE_DEFINITIONS
from core.definitions.channel_definitions import CHANNEL_DEFINITIONS

# 将来的に追加予定のモジュール
# from core.authority_logic import calculate_authority
# from core.profile_logic import determine_profile
# from core.channel_center import evaluate_active_channels


def build_chart(birth_data):
    """
    チャートを構築する主関数
    - 惑星位置を取得
    - 黄経をゲート＋ラインに変換
    - ゲート情報とチャネル情報を統合
    """
    astro_data = get_astro_positions(birth_data)  # dict: {planet: longitude}

    gates = {}
    for planet, lon in astro_data.items():
        gate, line = map_longitude_to_gate_line(lon)
        gates[planet] = {
            "gate": gate,
            "line": line,
            "gate_name_en": GATE_DEFINITIONS[str(gate)]["hd_name_en"],
            "gate_name_ja": GATE_DEFINITIONS[str(gate)]["hd_name_ja"],
        }

    # チャネルの活性状態を判定（仮設）
    active_gates = [data["gate"] for data in gates.values()]
    active_channels = []
    for ch in CHANNEL_DEFINITIONS:
        if all(g in active_gates for g in ch["gates"]):
            active_channels.append(ch)

    chart = {
        "gates": gates,
        "active_channels": active_channels,
        # "authority": calculate_authority(gates, ...),
        # "profile": determine_profile(gates, ...),
    }
    return chart


# birth_dataサンプル形式
# birth_data = {
#     "year": 1990,
#     "month": 12,
#     "day": 1,
#     "hour": 14,
#     "minute": 30,
#     "latitude": 35.6895,
#     "longitude": 139.6917,
#     "timezone": "Asia/Tokyo"
# }

# if __name__ == '__main__':
#     result = build_chart(birth_data)
#     print(result)
