# core/chart_builder.py

from core.astro.astro_position import get_planet_positions
from core.gate_mapper import get_gate_and_line
from core.channel_center import get_active_channels_and_centers
from core.profile_logic import calculate_profile
from core.authority_logic import determine_authority
from core.definitions.loader import load_gate_definitions, load_channel_definitions
from core.variable_logic import extract_phs_variables
from core.mbti_templates import suggest_mbti_structure


def build_chart(birth_data):
    # Designチャートも含めて取得
    positions = get_planet_positions(birth_data, include_design=True)
    personality_pos = positions["Personality"]
    design_pos = positions["Design"]

    # Personalityの惑星位置からGATEを算出
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
        } for planet, g in raw_gates.items()
    }

    active_channels, defined_centers = get_active_channels_and_centers(raw_gates, channel_defs)
    enriched_channels = [channel_dict[c] for c in active_channels if c in channel_dict]

    profile = calculate_profile(raw_gates)
    authority = determine_authority(raw_gates, defined_centers)

    # 🌐 Variablesロジック（Personality / Design を使う）
    variables = extract_phs_variables(personality_pos, design_pos)

    # 🧠 MBTIロジック
    mbti_suggestion = suggest_mbti_structure(profile, variables.get("Variable", ""), authority)

    return {
        "planet_positions": personality_pos,
        "gates": gates,
        "active_channels": enriched_channels,
        "defined_centers": defined_centers,
        "profile": profile,
        "authority": authority,
        "variables": variables,
        "mbti_suggestion": mbti_suggestion
    }


if __name__ == "__main__":
    birth_data = {
        "date": "1983-05-01",
        "time": "14:35",
        "location": "Aomori, Japan"
    }

    chart = build_chart(birth_data)

    import json
    print(json.dumps(chart, indent=2, ensure_ascii=False))
