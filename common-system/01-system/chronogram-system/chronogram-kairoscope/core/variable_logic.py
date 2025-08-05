# core/variable_logic.py

from core.gate_mapper import get_gate_and_line

# トーン名／カラー名（必要に応じて拡張可）
TONE_NAMES = {
    1: "Smell", 2: "Taste", 3: "Outer Vision", 4: "Inner Vision", 5: "Touch", 6: "Tone"
}
COLOR_NAMES = {
    1: "Color 1", 2: "Color 2", 3: "Color 3", 4: "Color 4", 5: "Color 5", 6: "Color 6"
}
BASE_NAMES = {
    1: "Base 1", 2: "Base 2", 3: "Base 3", 4: "Base 4", 5: "Base 5"
}

def get_gate_and_line_from_longitude(longitude):
    """ゲートとラインを取得"""
    return get_gate_and_line(longitude)

def get_tone_from_longitude(longitude):
    """
    360°を64ゲート×6ライン（=384）に分割し、さらに各ラインを7トーンで分割（仮想Tone）
    1ゲート ≒ 5.625°、1ライン ≒ 0.9375°
    1トーン ≒ 0.15625°
    """
    line_position = (longitude % 0.9375)
    tone_index = int(line_position / 0.15625) + 1
    return min(tone_index, 6)

def get_color_from_tone(tone):
    return COLOR_NAMES.get(((tone - 1) % 6) + 1)

def get_base_from_color(color_index):
    return BASE_NAMES.get(((color_index - 1) % 5) + 1)

def get_lr_from_tone(tone):
    return "L" if tone in [1, 3, 5] else "R"

def derive_variable_type(tone_brain, tone_mind, tone_body, tone_awareness):
    """LR判定でPRL-DRLなどを導出"""
    brain = get_lr_from_tone(tone_brain)
    mind = get_lr_from_tone(tone_mind)
    body = get_lr_from_tone(tone_body)
    awareness = get_lr_from_tone(tone_awareness)
    return f"{brain}{mind}{body}{awareness}"

def extract_phs_variables(personality_pos, design_pos):
    """
    全PHS変数（Digestion, Environment, Perspective, Motivation）＋詳細を算出
    """

    # 各ポイントのGate/Line抽出
    design_sun = get_gate_and_line_from_longitude(design_pos["Sun"])
    design_earth = get_gate_and_line_from_longitude(design_pos["Earth"])
    personality_sun = get_gate_and_line_from_longitude(personality_pos["Sun"])
    personality_earth = get_gate_and_line_from_longitude(personality_pos["Earth"])

    # 各トーン抽出
    tone_brain = get_tone_from_longitude(design_pos["Sun"])
    tone_mind = get_tone_from_longitude(design_pos["Earth"])
    tone_body = get_tone_from_longitude(personality_pos["Sun"])
    tone_awareness = get_tone_from_longitude(personality_pos["Earth"])

    variable_code = derive_variable_type(tone_brain, tone_mind, tone_body, tone_awareness)

    variables = {
        "Digestion": {
            "Gate": design_sun["gate"],
            "Line": design_sun["line"],
            "Tone": tone_brain,
            "ToneName": TONE_NAMES.get(tone_brain),
            "LR": get_lr_from_tone(tone_brain)
        },
        "Environment": {
            "Gate": design_earth["gate"],
            "Line": design_earth["line"],
            "Tone": tone_mind,
            "ToneName": TONE_NAMES.get(tone_mind),
            "LR": get_lr_from_tone(tone_mind)
        },
        "Perspective": {
            "Gate": personality_sun["gate"],
            "Line": personality_sun["line"],
            "Tone": tone_body,
            "ToneName": TONE_NAMES.get(tone_body),
            "LR": get_lr_from_tone(tone_body)
        },
        "Motivation": {
            "Gate": personality_earth["gate"],
            "Line": personality_earth["line"],
            "Tone": tone_awareness,
            "ToneName": TONE_NAMES.get(tone_awareness),
            "LR": get_lr_from_tone(tone_awareness)
        },
        "Variable": variable_code,
        "Source": "Kairoscope PHS logic v1.0"
    }

    return variables
