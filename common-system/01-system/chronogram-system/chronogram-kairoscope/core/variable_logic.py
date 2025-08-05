# core/variable_logic.py

from core.gate_mapper import get_gate_and_line

# 各辞書：Tone名、Color名、Base名、MDC象徴名（例）
TONE_NAMES = {
    1: "Smell", 2: "Taste", 3: "Outer Vision", 4: "Inner Vision", 5: "Touch", 6: "Tone"
}
COLOR_NAMES = {
    1: "Security", 2: "Fear", 3: "Need", 4: "Form", 5: "Fixer", 6: "Personal"
}
BASE_NAMES = {
    1: "Base 1", 2: "Base 2", 3: "Base 3", 4: "Base 4", 5: "Base 5"
}
MDC_NAMES = {
    "Digestion": ["The Alchemist", "The Sensor", "The Seer", "The Mirror", "The Empath", "The Frequency"],
    "Environment": ["The Market", "The Cave", "The Bridge", "The Tree", "The Island", "The Hearth"],
    "Perspective": ["Observer", "Participant", "Mapper", "Mirror Gaze", "Invisible Eye", "Fractal Lens"],
    "Motivation": ["Hope", "Fear", "Desire", "Need", "Guilt", "Innocence"]
}

def get_tone_from_longitude(longitude):
    line_position = (longitude % 0.9375)
    tone_index = int(line_position / 0.15625) + 1
    return min(tone_index, 6)

def get_color_from_tone(tone):
    return ((tone - 1) % 6) + 1

def get_base_from_color(color_index):
    return ((color_index - 1) % 5) + 1

def get_lr_from_tone(tone):
    return "L" if tone in [1, 3, 5] else "R"

def derive_variable_type(tone_brain, tone_mind, tone_body, tone_awareness):
    brain = get_lr_from_tone(tone_brain)
    mind = get_lr_from_tone(tone_mind)
    body = get_lr_from_tone(tone_body)
    awareness = get_lr_from_tone(tone_awareness)
    return f"{brain}{mind}{body}{awareness}"

def extract_phs_variables(personality_pos, design_pos):
    # 黄経からToneを導出
    tone_brain = get_tone_from_longitude(design_pos["Sun"])
    tone_mind = get_tone_from_longitude(design_pos["Earth"])
    tone_body = get_tone_from_longitude(personality_pos["Sun"])
    tone_awareness = get_tone_from_longitude(personality_pos["Earth"])

    # 各Color / Base
    color_brain = get_color_from_tone(tone_brain)
    color_mind = get_color_from_tone(tone_mind)
    color_body = get_color_from_tone(tone_body)
    color_awareness = get_color_from_tone(tone_awareness)

    base_brain = get_base_from_color(color_brain)
    base_mind = get_base_from_color(color_mind)
    base_body = get_base_from_color(color_body)
    base_awareness = get_base_from_color(color_awareness)

    variable_code = derive_variable_type(tone_brain, tone_mind, tone_body, tone_awareness)

    def build_section(name, tone, color, base):
        return {
            "Tone": tone,
            "ToneName": TONE_NAMES.get(tone),
            "Color": color,
            "ColorName": COLOR_NAMES.get(color),
            "Base": base,
            "LR": get_lr_from_tone(tone),
            "MDC": MDC_NAMES[name][tone - 1]
        }

    return {
        "Digestion": build_section("Digestion", tone_brain, color_brain, base_brain),
        "Environment": build_section("Environment", tone_mind, color_mind, base_mind),
        "Perspective": build_section("Perspective", tone_body, color_body, base_body),
        "Motivation": build_section("Motivation", tone_awareness, color_awareness, base_awareness),
        "Variable": variable_code,
        "Source": "Kairoscope v2.0 — PHS full logic"
    }
