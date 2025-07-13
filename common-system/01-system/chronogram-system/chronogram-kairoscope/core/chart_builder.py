# chart_builder.py
from core.astro.astro_position import get_planet_positions
from core.gate_mapper import get_gate_and_line
from core.definitions import load_gate_definitions, load_channel_definitions
from core.channel_center import get_active_channels_and_centers
from core.profile_logic import calculate_profile
from core.authority_logic import determine_authority


def build_chart(birth_data):
    positions = get_planet_positions(birth_data)
    gates = {planet: get_gate_and_line(lon) for planet, lon in positions.items()}

    gate_defs = load_gate_definitions()
    channel_defs = load_channel_definitions()

    active_channels, defined_centers = get_active_channels_and_centers(gates, channel_defs)
    profile = calculate_profile(gates)
    authority = determine_authority(gates, defined_centers)

    chart = {
        "planet_positions": positions,
        "gates": gates,
        "active_channels": active_channels,
        "defined_centers": defined_centers,
        "profile": profile,
        "authority": authority
    }
    return chart