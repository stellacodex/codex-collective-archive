# /core/authority_logic.py

def determine_authority(defined_centers, type_hint=None):
    """
    Determine the Inner Authority based on the defined centers and type.
    
    :param defined_centers: List of defined centers (e.g. ["Solar Plexus", "Sacral"])
    :param type_hint: Optional HD type to help resolve edge cases (e.g. "Projector", "Reflector")
    :return: String representing the inner authority (e.g. "Emotional", "Sacral", etc.)
    """
    if "Solar Plexus" in defined_centers:
        return "Emotional"
    elif "Sacral" in defined_centers:
        return "Sacral"
    elif "Spleen" in defined_centers:
        return "Splenic"
    elif "Ego" in defined_centers:
        return "Ego Projected"
    elif "G" in defined_centers:
        return "Self Projected"
    elif type_hint == "Projector":
        return "Mental Projected"
    elif type_hint == "Reflector":
        return "Lunar"
    else:
        return "Unknown"
