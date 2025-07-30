# core/mbti_templates.py

def suggest_mbti_structure(profile, variable, authority):
    # 簡易ロジックに基づいてMBTI構造を提案
    intro_extro = "I" if variable.startswith("R") else "E"
    judge_perceive = "J" if authority in ["Emotional", "Sacral"] else "P"
 
    profile_key = str(profile)
    if profile_key in ["1/3", "5/1"]:
        thinking_feeling = "T"
        sensing_intuition = "S"
    elif profile_key in ["4/6", "2/4"]:
        thinking_feeling = "F"
        sensing_intuition = "N"
    else:
        thinking_feeling = "F"
        sensing_intuition = "S"

    return f"{intro_extro}{sensing_intuition}{thinking_feeling}{judge_perceive}"