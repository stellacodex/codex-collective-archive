# Kairoscope Variable Logic - 精密実装版

def calculate_variables_from_chart(raw_gates):
    """
    精密PHS/Variablesの推定：
    - Digestion（Determination）：Design Sun
    - Environment：Design Earth
    - Perspective：Personality Sun
    - Motivation：Personality Earth
    """
    design_sun_gate = raw_gates.get("Design_Sun", {}).get("gate")
    design_earth_gate = raw_gates.get("Design_Earth", {}).get("gate")
    personality_sun_gate = raw_gates.get("Sun", {}).get("gate")
    personality_earth_gate = raw_gates.get("Earth", {}).get("gate")

    # --- Digestion 判定 ---
    if design_sun_gate is not None:
        digestion = "Alternating" if design_sun_gate % 2 == 0 else "Consecutive"
    else:
        digestion = "Unknown"

    # --- Environment 判定 ---
    if design_earth_gate is not None:
        environment = "Markets" if design_earth_gate < 33 else "Kitchens"
    else:
        environment = "Unknown"

    # --- Perspective 判定 ---
    if personality_sun_gate is not None:
        perspective = "Observer" if personality_sun_gate < 16 else "Observed"
    else:
        perspective = "Unknown"

    # --- Motivation 判定 ---
    if personality_earth_gate in [1, 2, 3, 4, 5, 6]:
        motivation = "Hope"
    elif personality_earth_gate is not None:
        motivation = "Fear"
    else:
        motivation = "Unknown"

    # --- Variableコード形式（例: CL-OR）仮実装 ---
    variable_code = f"{digestion[0]}L-{perspective[0]}R" if digestion != "Unknown" and perspective != "Unknown" else "Unknown"

    return {
        "Digestion": digestion,
        "Environment": environment,
        "Perspective": perspective,
        "Motivation": motivation,
        "Variable": variable_code
    }
