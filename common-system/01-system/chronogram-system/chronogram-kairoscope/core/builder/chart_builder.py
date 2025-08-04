# core/chart_builder.py

from core.astro.astro_position import get_planet_positions
from core.gate_mapper import get_gate_and_line
from core.channel_center import get_active_channels_and_centers
from core.profile_logic import calculate_profile
from core.authority_logic import determine_authority
from core.definitions.loader import load_gate_definitions, load_channel_definitions
from core.variable_logic import extract_phs_variables
from core.mbti_templates import suggest_mbti_structure

import json
import os


# === 関数定義 ===

def build_chart(birth_data):
    positions = get_planet_positions(birth_data, include_design=True)

    personality_pos = positions["Personality"]
    personality_pos["Earth"] = (personality_pos["Sun"] + 180) % 360
    design_pos = positions["Design"]
    design_pos["Earth"] = (design_pos["Sun"] + 180) % 360

    raw_gates = {planet: get_gate_and_line(deg) for planet, deg in personality_pos.items()}

    gate_defs = load_gate_definitions()
    channel_defs = load_channel_definitions()
    gate_dict = {g["gate"]: g for g in gate_defs}
    channel_dict = {c["channel"]: c for c in channel_defs}

    gates = {
        planet: {
            "gate": g["gate"],
            "line": g["line"],
            **gate_dict.get(g["gate"], {})
        }
        for planet, g in raw_gates.items()
    }

    active_channels, defined_centers = get_active_channels_and_centers(raw_gates, channel_defs)
    enriched_channels = [channel_dict[c] for c in active_channels if c in channel_dict]

    profile = calculate_profile(raw_gates)
    authority = determine_authority(raw_gates, defined_centers)
    variables = extract_phs_variables(personality_pos, design_pos)

    mbti_suggestion = suggest_mbti_structure(profile, variables.get("Variable", ""), authority)

    # === 🔧 ここで返り値をラップ ===
    return {
        "chart": {
            "planet_positions": personality_pos,
            "gates": gates,
            "active_channels": enriched_channels,
            "defined_centers": defined_centers,
            "profile": profile,
            "authority": authority,
            "variables": variables,
            "mbti_suggestion": mbti_suggestion
        },
        "rave_chart": {
            "birth": {
                "date": f"{birth_data['year']:04d}-{birth_data['month']:02d}-{birth_data['day']:02d}",
                "time": f"{birth_data['hour']:02d}:{birth_data['minute']:02d}",
                "location": birth_data["location"]
            }
        }
    }



# === 実行処理（任意テスト用）===
if __name__ == "__main__":
    birth_data = {
        "year": 1983,
        "month": 5,
        "day": 1,
        "hour": 12,
        "minute": 0,
        "timezone": "Asia/Tokyo",
        "location": "Aomori"
    }

    chart_data = build_chart(birth_data)

    os.makedirs("output", exist_ok=True)
    with open("output/data.json", "w") as f:
        json.dump(chart_data, f, indent=2, ensure_ascii=False)

    print("✅ data.json を output/ に保存したよ")
