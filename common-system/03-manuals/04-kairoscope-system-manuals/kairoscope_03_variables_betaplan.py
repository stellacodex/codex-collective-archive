# Kairoscope 03 Module - Variables
# variable_logic.py（正式ロジック実装 / PHS - Determination, Environment, Perspective, Motivation）

from typing import Dict

def calculate_variables_from_chart(raw_gates: Dict[str, Dict]) -> Dict[str, str]:
    """
    Design/PersonalityのSun/Earthゲート情報に基づき、Variablesを正式に判定。
    - Digestion（Determination）：Design Sun
    - Environment：Design Earth
    - Perspective：Personality Sun
    - Motivation：Personality Earth
    """
    design_sun = raw_gates.get("Design_Sun", {}).get("gate")
    design_earth = raw_gates.get("Design_Earth", {}).get("gate")
    personality_sun = raw_gates.get("Sun", {}).get("gate")
    personality_earth = raw_gates.get("Earth", {}).get("gate")

    # Digestion 判定
    digestion_map = {
        (1, 2, 3, 4, 5): "Consecutive",
        (6, 7, 8, 9, 10): "Alternating",
        (11, 12, 13, 14, 15): "Open Taste",
        (16, 17, 18, 19, 20): "Closed Taste",
        (21, 22, 23, 24, 25): "Smell"
    }
    digestion = _map_gate_to_label(design_sun, digestion_map, default="Unknown")

    # Environment 判定
    environment_map = {
        (1, 2, 3, 4, 5, 6): "Caves",
        (7, 8, 9, 10, 11, 12): "Markets",
        (13, 14, 15, 16, 17, 18): "Kitchens",
        (19, 20, 21, 22, 23, 24): "Mountains",
        (25, 26, 27, 28, 29, 30): "Valleys"
    }
    environment = _map_gate_to_label(design_earth, environment_map, default="Unknown")

    # Perspective 判定
    perspective_map = {
        (1, 2, 3, 4, 5, 6): "Observer",
        (7, 8, 9, 10, 11, 12): "Observed",
        (13, 14, 15, 16, 17, 18): "Peripheral",
        (19, 20, 21, 22, 23, 24): "Strategic",
        (25, 26, 27, 28, 29, 30): "Feeling"
    }
    perspective = _map_gate_to_label(personality_sun, perspective_map, default="Unknown")

    # Motivation 判定
    motivation_map = {
        (1, 2, 3, 4, 5, 6): "Hope",
        (7, 8, 9, 10, 11, 12): "Need",
        (13, 14, 15, 16, 17, 18): "Desire",
        (19, 20, 21, 22, 23, 24): "Innocence",
        (25, 26, 27, 28, 29, 30): "Guilt"
    }
    motivation = _map_gate_to_label(personality_earth, motivation_map, default="Unknown")

    # Variableコード（例：CL-OR）
    variable_code = f"{digestion[0]}L-{perspective[0]}R" if digestion != "Unknown" and perspective != "Unknown" else "Unknown"

    return {
        "Digestion": digestion,
        "Environment": environment,
        "Perspective": perspective,
        "Motivation": motivation,
        "Variable": variable_code
    }

def _map_gate_to_label(gate: int, mapping: Dict[tuple, str], default="Unknown") -> str:
    if gate is None:
        return default
    for gates, label in mapping.items():
        if gate in gates:
            return label
    return default
