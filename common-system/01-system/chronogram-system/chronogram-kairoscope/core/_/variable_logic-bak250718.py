# variable_logic.py

def extract_phs_variables(personality_positions, design_positions):
    """
    PHS / Variableを生成するためのロジック：
    - Digestion  = Design Sun
    - Environment = Design Earth
    - Perspective = Personality Sun
    - Motivation = Personality Earth
    """
    def determine_digestion(degree):
        if degree is None:
            return "Unknown"
        elif 0 <= degree < 30:
            return "Consecutive"
        elif 30 <= degree < 60:
            return "Alternating"
        elif 60 <= degree < 90:
            return "Open Taste"
        elif 90 <= degree < 120:
            return "Closed Taste"
        elif 120 <= degree < 150:
            return "Calm Touch"
        elif 150 <= degree < 180:
            return "Nervous Touch"
        elif 180 <= degree < 210:
            return "Cold Thirst"
        elif 210 <= degree < 240:
            return "Hot Thirst"
        elif 240 <= degree < 270:
            return "Direct Light"
        elif 270 <= degree < 300:
            return "Indirect Light"
        elif 300 <= degree < 330:
            return "Smell Internal"
        elif 330 <= degree < 360:
            return "Smell External"
        return "Unknown"

    def determine_environment(degree):
        if degree is None:
            return "Unknown"
        elif 0 <= degree < 60:
            return "Caves"
        elif 60 <= degree < 120:
            return "Markets"
        elif 120 <= degree < 180:
            return "Kitchens"
        elif 180 <= degree < 240:
            return "Mountains"
        elif 240 <= degree < 300:
            return "Valleys"
        elif 300 <= degree < 360:
            return "Shore"
        return "Unknown"

    def determine_perspective(degree):
        if degree is None:
            return "Unknown"
        elif 0 <= degree < 60:
            return "Personal"
        elif 60 <= degree < 120:
            return "Cognition"
        elif 120 <= degree < 180:
            return "Power"
        elif 180 <= degree < 240:
            return "Probability"
        elif 240 <= degree < 300:
            return "Possibility"
        elif 300 <= degree < 360:
            return "Observer"
        return "Unknown"

    def determine_motivation(degree):
        if degree is None:
            return "Unknown"
        elif 0 <= degree < 60:
            return "Hope"
        elif 60 <= degree < 120:
            return "Need"
        elif 120 <= degree < 180:
            return "Desire"
        elif 180 <= degree < 240:
            return "Innocence"
        elif 240 <= degree < 300:
            return "Guilt"
        elif 300 <= degree < 360:
            return "Fear"
        return "Unknown"

    def variable_code(digestion, perspective):
        d_map = {
            "Consecutive": "C", "Alternating": "A", "Open Taste": "O", "Closed Taste": "C",
            "Calm Touch": "C", "Nervous Touch": "N", "Cold Thirst": "C", "Hot Thirst": "H",
            "Direct Light": "D", "Indirect Light": "I", "Smell Internal": "I", "Smell External": "E"
        }
        p_map = {
            "Personal": "P", "Cognition": "C", "Power": "P", "Probability": "P",
            "Possibility": "P", "Observer": "O"
        }
        d = d_map.get(digestion, "?")
        p = p_map.get(perspective, "?")
        return f"{d}L-{p}R"

    sun_design = design_positions.get("Sun")
    earth_design = design_positions.get("Earth")
    sun_personality = personality_positions.get("Sun")
    earth_personality = personality_positions.get("Earth")

    digestion = determine_digestion(sun_design)
    environment = determine_environment(earth_design)
    perspective = determine_perspective(sun_personality)
    motivation = determine_motivation(earth_personality)
    variable = variable_code(digestion, perspective)

    return {
        "Digestion": digestion,
        "Environment": environment,
        "Perspective": perspective,
        "Motivation": motivation,
        "Variable": variable
    }


def predict_mbti(profile, variable, authority):
    score = {
        "I": 0, "E": 0,
        "N": 0, "S": 0,
        "F": 0, "T": 0,
        "J": 0, "P": 0
    }

    # Profileによる傾向
    if profile.startswith("1") or profile.startswith("5"):
        score["I"] += 1
    if profile.startswith("4") or profile.startswith("6"):
        score["E"] += 1
    if profile.endswith("3") or profile.endswith("6"):
        score["P"] += 1
    if profile.endswith("1") or profile.endswith("5"):
        score["J"] += 1

    # Variableによる傾向（例）
    if variable in ["CL-OR", "AL-OR"]:
        score["N"] += 1
    if variable in ["DL-PR", "OL-PR"]:
        score["S"] += 1

    # Authorityによる傾向
    if authority in ["Emotional", "Ego"]:
        score["F"] += 1
    if authority in ["Spleen", "Mental"]:
        score["T"] += 1

    return (
        ("I" if score["I"] >= score["E"] else "E") +
        ("N" if score["N"] >= score["S"] else "S") +
        ("F" if score["F"] >= score["T"] else "T") +
        ("J" if score["J"] >= score["P"] else "P")
    )
