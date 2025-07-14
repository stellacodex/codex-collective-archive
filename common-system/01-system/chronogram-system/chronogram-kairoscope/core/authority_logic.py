# authority_logic.py

def determine_authority(defined_centers, type=None):
    """
    Determine the inner authority based on defined centers.
    Optionally use type to resolve cases like Mental Projector or Reflector.
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
    elif type == "Projector":
        return "Mental Projected"
    elif type == "Reflector":
        return "Lunar"
    else:
        return "Unknown"
