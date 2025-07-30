# /core/profile_logic.py

def calculate_profile(planet_gates):
    """
    Calculate the HD Profile based on Personality and Design Sun lines.
    :param planet_gates: dict with keys like 'Personality_Sun', 'Design_Sun', each containing a 'line' field
    :return: Profile string like "6/2"
    """
    sun = planet_gates.get("Sun", {})
    earth = planet_gates.get("Earth", {})
    personality_line = sun.get("line")
    design_line = earth.get("line")

    if personality_line and design_line:
        return f"{personality_line}/{design_line}"
    return "Unknown"
