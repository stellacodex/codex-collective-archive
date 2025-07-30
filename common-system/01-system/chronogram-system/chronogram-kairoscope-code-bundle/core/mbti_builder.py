/core/mbti_builder.py

def build_mbti_profile(mbti_type):
    traits = {
        "I": "内向的",
        "E": "外向的",
        "N": "直観的",
        "S": "感覚的",
        "F": "感情的",
        "T": "論理的",
        "J": "計画的",
        "P": "柔軟的"
    }

    description = [traits[c] for c in mbti_type if c in traits]
    return {
        "type": mbti_type,
        "description": description
    }