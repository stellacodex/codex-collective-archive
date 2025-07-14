# /core/profile_logic.py

def calculate_profile(planet_gates):
    """
    Calculate the HD Profile based on Personality and Design Sun lines.
    :param planet_gates: dict with keys like 'Personality_Sun', 'Design_Sun', each containing a 'line' field
    :return: Profile string like "6/2"
    """
    personality_line = planet_gates.get("Personality_Sun", {}).get("line")
    design_line = planet_gates.get("Design_Sun", {}).get("line")
    
    if personality_line and design_line:
        return f"{personality_line}/{design_line}"
    else:
        return "Unknown"
