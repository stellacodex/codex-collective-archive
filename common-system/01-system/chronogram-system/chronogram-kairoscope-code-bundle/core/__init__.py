# /core/__init__.py

import json
import os

def load_gate_definitions(filepath="core/definitions/gate-definitions.json"):
    """
    Load the Gate Definitions JSON file.
    :param filepath: path to gate-definitions.json
    :return: dict of gate definitions
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Gate definitions file not found at: {filepath}")
    
    with open(filepath, "r", encoding="utf-8") as f:
        gate_data = json.load(f)
    
    return gate_data


def load_channel_definitions(filepath="core/definitions/channel-definitions.json"):
    """
    Load the Channel Definitions JSON file.
    :param filepath: path to channel-definitions.json
    :return: dict or list of channel definitions
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Channel definitions file not found at: {filepath}")
    
    with open(filepath, "r", encoding="utf-8") as f:
        channel_data = json.load(f)
    
    return channel_data
