# /core/authority_logic.py

def determine_authority(raw_gates, defined_centers):
    if "Solar Plexus" in defined_centers:
        return "Emotional"
    elif "Sacral" in defined_centers:
        return "Sacral"
    elif "Spleen" in defined_centers:
        return "Splenic"
    elif "Heart" in defined_centers:
        return "Ego"
    elif "Self" in defined_centers:
        return "Self-Projected"
    elif "None" in defined_centers:
        return "Mental"
    else:
        return "Lunar"