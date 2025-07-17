# core/mbti_templates.py

from collections import defaultdict

# MBTI Suggestion Logic (by Profile + Variable Code + Authority)
def predict_mbti(profile, variable_code, authority):
    """
    プロファイル、Variableコード、Inner Authorityの組み合わせからMBTIタイプを推定。
    今後の学習で拡張可能なよう、シンプルなルールベース。
    """
    profile_map = {
        "1/3": "ISTJ", "1/4": "ISFJ",
        "2/4": "ISFP", "2/5": "ESFP",
        "3/5": "ESTP", "3/6": "ISTP",
        "4/1": "ESFJ", "4/6": "ENFJ",
        "5/1": "ENTJ", "5/2": "ESTJ",
        "6/2": "ENFP", "6/3": "INFP"
    }

    variable_map = {
        "CL-OR": "INFJ", "AL-OR": "INTJ",
        "CL-DR": "ISFP", "AL-DR": "ISTP",
        "CL-OL": "ENFP", "AL-OL": "ENTP",
        "CL-DL": "ESFP", "AL-DL": "ESTP"
    }

    authority_bias = {
        "Sacral": "P",
        "Emotional": "F",
        "Splenic": "S",
        "Ego": "T",
        "Self-Projected": "N",
        "Mental": "I"
    }

    # 初期推定
    mbti = profile_map.get(profile, "INFP")  # デフォルト
    variable_mbti = variable_map.get(variable_code, "")

    # authority補正（末尾を変更）
    if authority in authority_bias:
        if len(mbti) == 4:
            mbti = mbti[:3] + authority_bias[authority]

    # variableベースに優先して切り替え（ただし3文字一致まで）
    if variable_mbti and mbti[:2] == variable_mbti[:2]:
        mbti = variable_mbti[:3] + mbti[3]

    return mbti


# Thinking Style（外向 or 内向）推定

def get_thinking_style(mbti):
    return "Expressive" if mbti.startswith("E") else "Introspective"


def suggest_mbti_structure(profile, variable_code, authority):
    mbti = predict_mbti(profile, variable_code, authority)
    return {
        "MBTI Type": mbti,
        "MBTI Candidates": [mbti],
        "Thinking Style": get_thinking_style(mbti)
    }
