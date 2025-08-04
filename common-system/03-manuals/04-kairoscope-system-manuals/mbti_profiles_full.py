# core/mbti_profiles.py

MBTI_PROFILES = {
    "INFP": {
        "nickname": "夢見る仲介者",
        "cognitive_function": "Fi-Ne-Si-Te",
        "thinking_style": "Abstract / Reflective",
        "description": "理想主義的で想像力豊か。内面の価値観に従って世界を見つめ、静かに他者と共鳴する詩的な感受性の持ち主。",
        "associated_profiles": ["4/6", "2/4"],
        "variable_trends": ["CL-OR", "AL-PR"]
    },
    "INFJ": {
        "nickname": "静かな予言者",
        "cognitive_function": "Ni-Fe-Ti-Se",
        "thinking_style": "Abstract / Strategic",
        "description": "深い直観と共感力を備え、未来のビジョンに導かれながら他者の成長を支援する導き手。",
        "associated_profiles": ["5/1", "1/3"],
        "variable_trends": ["DL-PR", "IL-OR"]
    },
    "INTP": {
        "nickname": "内なる理論家",
        "cognitive_function": "Ti-Ne-Si-Fe",
        "thinking_style": "Analytical / Conceptual",
        "description": "論理と思索を深め、知的探究に没頭する分析者。世界を仮説で組み立てながら、意味を探求する。",
        "associated_profiles": ["1/3", "5/1"],
        "variable_trends": ["CL-CR", "OL-OR"]
    },
    "INTJ": {
        "nickname": "戦略的構築者",
        "cognitive_function": "Ni-Te-Fi-Se",
        "thinking_style": "Strategic / Independent",
        "description": "未来志向で目的に忠実。抽象的思考と実行力を備えた思索家で、ビジョンを現実へと変換する構築者。",
        "associated_profiles": ["3/5", "6/2"],
        "variable_trends": ["DL-OR", "CL-PR"]
    },
    "ISFP": {
        "nickname": "感覚する芸術家",
        "cognitive_function": "Fi-Se-Ni-Te",
        "thinking_style": "Sensory / Reflective",
        "description": "感覚と内面の価値を融合させる表現者。静けさの中に繊細な美を見出す、感性豊かな創造者。",
        "associated_profiles": ["2/4", "4/6"],
        "variable_trends": ["CL-IR", "NL-OR"]
    },
    "ISFJ": {
        "nickname": "守護する調和者",
        "cognitive_function": "Si-Fe-Ti-Ne",
        "thinking_style": "Practical / Empathetic",
        "description": "伝統と人への思いやりを重んじ、静かに支えることに喜びを見出す。調和と安定を尊ぶ守り人。",
        "associated_profiles": ["6/2", "1/4"],
        "variable_trends": ["OL-IR", "CL-OR"]
    },
    "ISTP": {
        "nickname": "現場の分析者",
        "cognitive_function": "Ti-Se-Ni-Fe",
        "thinking_style": "Tactical / Observational",
        "description": "実践的で冷静な判断力を持ち、物事の仕組みを解き明かす思考者。手を動かしながら世界を理解する。",
        "associated_profiles": ["3/5", "5/1"],
        "variable_trends": ["CL-CR", "NL-PR"]
    },
    "ISTJ": {
        "nickname": "実務の信頼者",
        "cognitive_function": "Si-Te-Fi-Ne",
        "thinking_style": "Logical / Organized",
        "description": "責任感と秩序を重んじる実務家。経験からの学びを大切にし、安定した基盤を築く力を持つ。",
        "associated_profiles": ["1/3", "6/2"],
        "variable_trends": ["OL-CR", "CL-OR"]
    },
    "ENFP": {
        "nickname": "可能性の開拓者",
        "cognitive_function": "Ne-Fi-Te-Si",
        "thinking_style": "Imaginative / Energetic",
        "description": "アイデアと情熱に満ちた冒険者。人や世界の可能性を信じ、未来への扉を開くことに喜びを見出す。",
        "associated_profiles": ["4/6", "3/5"],
        "variable_trends": ["AL-PR", "DL-OR"]
    },
    "ENFJ": {
        "nickname": "人を導く共感者",
        "cognitive_function": "Fe-Ni-Se-Ti",
        "thinking_style": "Empathetic / Visionary",
        "description": "他者の成長を支える情熱的リーダー。人間関係の中にビジョンを見出し、協調と変容を促す。",
        "associated_profiles": ["2/4", "5/1"],
        "variable_trends": ["DL-PR", "AL-OR"]
    },
    "ENTP": {
        "nickname": "好奇心の探検者",
        "cognitive_function": "Ne-Ti-Fe-Si",
        "thinking_style": "Abstract / Explorative",
        "description": "論理と創造性の間を自由に飛び回る探求者。知的好奇心で世界を刺激し続けるイノベーター。",
        "associated_profiles": ["3/5", "6/2"],
        "variable_trends": ["DL-CR", "AL-OR"]
    },
    "ENTJ": {
        "nickname": "意志の指揮者",
        "cognitive_function": "Te-Ni-Fi-Se",
        "thinking_style": "Strategic / Decisive",
        "description": "明確なビジョンと統率力を持つリーダー。目的を定め、成果を重視しながら戦略的に前進する。",
        "associated_profiles": ["3/5", "1/3"],
        "variable_trends": ["CL-PR", "DL-CR"]
    },
    "ESFP": {
        "nickname": "今を生きる表現者",
        "cognitive_function": "Se-Fi-Te-Ni",
        "thinking_style": "Sensory / Expressive",
        "description": "エネルギッシュで社交的。五感と感情を通じて人生を味わい、人との関わりの中に喜びを見出す。",
        "associated_profiles": ["2/4", "3/5"],
        "variable_trends": ["NL-IR", "CL-OR"]
    },
    "ESFJ": {
        "nickname": "信頼の調整役",
        "cognitive_function": "Fe-Si-Ne-Ti",
        "thinking_style": "Practical / Cooperative",
        "description": "周囲への気配りに長けた調整役。関係性を育み、安心できる場づくりを大切にする。",
        "associated_profiles": ["2/4", "6/2"],
        "variable_trends": ["OL-OR", "NL-PR"]
    },
    "ESTP": {
        "nickname": "即応の実践者",
        "cognitive_function": "Se-Ti-Fe-Ni",
        "thinking_style": "Tactical / Spontaneous",
        "description": "反射神経と論理を活かし、現場での判断に優れる。刺激を求めながら、即応的に状況に対応する。",
        "associated_profiles": ["3/5", "5/1"],
        "variable_trends": ["NL-CR", "DL-PR"]
    },
    "ESTJ": {
        "nickname": "秩序の管理者",
        "cognitive_function": "Te-Si-Ne-Fi",
        "thinking_style": "Logical / Directive",
        "description": "組織や枠組みを整える指導者。効率性と秩序を重視し、現実的かつ結果にこだわる。",
        "associated_profiles": ["1/3", "5/1"],
        "variable_trends": ["OL-CR", "CL-OR"]
    }
}
