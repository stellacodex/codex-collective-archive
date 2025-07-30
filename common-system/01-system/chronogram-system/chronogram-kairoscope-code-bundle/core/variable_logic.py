# variable_logic.py

from core.gate_mapper import get_gate_and_line

def extract_phs_variables(personality_pos, design_pos):
    personality_sun = get_gate_and_line(personality_pos["Sun"])
    personality_earth = get_gate_and_line(personality_pos["Earth"])
    design_sun = get_gate_and_line(design_pos["Sun"])
    design_earth = get_gate_and_line(design_pos["Earth"])

    variables = {
        "Digestion": f"Gate {design_sun['gate']} Line {design_sun['line']}",
        "Environment": f"Gate {design_earth['gate']} Line {design_earth['line']}",
        "Perspective": f"Gate {personality_sun['gate']} Line {personality_sun['line']}",
        "Motivation": f"Gate {personality_earth['gate']} Line {personality_earth['line']}",
        "Variable": derive_variable_type(design_sun, design_earth, personality_sun, personality_earth)
    }
    return variables

def derive_variable_type(design_sun, design_earth, personality_sun, personality_earth):
    def polarity(gate):
        return "L" if gate % 2 == 0 else "R"

    brain = polarity(design_sun["gate"])
    mind = polarity(design_earth["gate"])
    body = polarity(personality_sun["gate"])
    awareness = polarity(personality_earth["gate"])

    return f"{brain}{mind}{body}{awareness}"