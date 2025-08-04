# kairoscope_md_generator.py

import json
with open('core/definitions/channel-definitions.json', 'r') as f:
    channel_definitions = json.load(f)
    
with open("core/definitions/gate-definitions.json", "r") as f:
    gate_definitions = json.load(f)
    
import json
with open('core/definitions/gate-definitions.json', 'r') as f:
    gate_definitions = json.load(f)

import json
from datetime import datetime

import sys
import os
import json

# このスクリプトのあるディレクトリ（core/scripts）から2階層上に移動し、ルートをpathに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# ローカルモジュールのインポート
from core.builder.chart_builder import build_chart
from core.scripts.utils import (
    generate_filename_from_birth,
    create_output_dirs,
    save_json,
    load_json,
    write_to_markdown,
)

ALL_CENTERS = [
    "Head", "Ajna", "Throat", "G", "Heart", "Sacral",
    "Solar Plexus", "Spleen", "Root"
]

def load_kairoscope_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)    
    
def find_channel_definition(defs, ch_key):
    for entry in defs:
        if ch_key in entry["channel"]:
            return entry
    return None

def parse_gate_line(gl_str):
    parts = gl_str.split(".")
    gate = int(parts[0])
    line = int(parts[1])
    return gate, line

def generate_channel_section(defined_channels, channel_definitions):
    lines = ["#### 🔸 Defined Channels"]
    for ch_entry in defined_channels:
        ch_key = ch_entry if isinstance(ch_entry, str) else ch_entry.get('channel')
        info = find_channel_definition(channel_definitions, ch_key)
        if info:
            jp = info.get("japanese_name", "N/A")
            en = info.get("english_name", "N/A")
            kairo = info.get("kairoscope_name", "N/A")
            desc = info.get("description", "")
            keywords = ", ".join(info.get("keywords", []))
            lines.append(f"- **{ch_key}｜{jp} / {en}**｜Kairoscope名「{kairo}」")
            lines.append(f"　　{desc}｜🧩 Keywords: {keywords}\n")
        else:
            lines.append(f"- **{ch_key}**：❓ 未定義チャンネル")
    return "\n".join(lines)


def generate_gate_section(chart, gate_definitions, title, gate_list, gate_defs):
    lines = [f"**{title}**"]
    for gl in gate_list:
        gate, line = parse_gate_line(gl)
        defn = next((g for g in gate_defs if g["gate"] == gate), None)
        if defn:
            hd_name = defn.get("hd_name_ja", "")
            kairoscope_name = defn.get("kairoscope_name_ja", "")
            keywords = ", ".join(defn.get("keywords", []))
            channels = ", ".join(defn.get("channels", []))
            line_desc = defn.get("lines", {}).get(str(line), "")
            lines.append(
                f"- **{gate}.{line}｜{hd_name}（{defn.get('hd_name_en', '')}）**｜Kairoscope名「{kairoscope_name}」  \n"
                f"　　{line_desc}｜🧩 Keywords: {keywords}  \n"
                f"　　🔗 チャンネル: {channels}"
            )
        else:
            lines.append(f"- **{gate}.{line}**｜定義なし")

    def format_gate(gate_number):
        info = get_gate_info(gate_number, gate_definitions)
        en = info.get("english_name", "N/A")
        ja = info.get("japanese_name", "N/A")
        kairo = info.get("kairoscope_name", "N/A")
        keywords = ", ".join(info.get("keywords", []))
        return f"- Gate {gate_number}「{ja} / {en}」：Kairoscope名「{kairo}」｜Keywords: {keywords}"

    lines.append("**Personality Gates**")
    for g in chart.get('personality_gates', []):
        lines.append(format_gate(g))

    lines.append("\n**Design Gates**")
    for g in chart.get('design_gates', []):
        lines.append(format_gate(g))

    return '\n'.join(lines)

def save_md(md_text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_text)
        
def generate_kairoscope_md(data):
    md = []

    birth = data['rave_chart']['birth']
    chart = data["chart"]
    variables = data.get("variables", {})

    mdc = data['mdc']
    phs = data['phs']
    personality = chart["personality"]
    design = chart["design"]
    variables = chart["variables"]
    centers = chart["centers"]

    channel_definitions = load_channel_definitions()
    gate_definitions = load_gate_definitions()

    md = []

    md.append("# Kairoscope Chart")
    md.append("")
    md.append("## Summary")
    md.append(f"- Type: {chart.get('type', 'N/A')}")
    md.append(f"- Authority: {chart.get('authority', 'N/A')}")
    md.append(f"- Profile: {chart.get('profile', 'N/A')}")
    md.append(f"- Definition: {chart.get('definition', 'N/A')}")
    md.append("")

    # Header
    md.append("### 🧬【Kairoscope: Human Design Profile - Takeo Yamada】\n")

    # Birth Info
    md.append("**Birth Information**")
    md.append(f"- 📅 Date: {birth['date']}")
    md.append(f"- 🕛 Time: {birth['time']}")
    md.append(f"- 📍 Location: {birth['location']}\n")

    # Chart Summary
    md.append("---\n\n#### 🔹 Chart Summary")
    md.append(f"- **Type**: {chart['type']}")
    md.append(f"- **Authority**: {chart['authority']}")
    md.append(f"- **Definition**: {chart['definition']}")
    md.append(f"- **Profile**: {chart['profile']}")
    md.append(f"- **Strategy**: {chart['strategy']}")
    md.append(f"- **Not-Self Theme**: {chart['not_self']}")
    md.append(f"- **Signature**: {chart['signature']}\n")

    # Centers
    md.append("---\n\n#### 🌀 Centers")
    md.append(generate_center_section(chart.get("defined_centers", [])))
    poetic = False  # True にすればKairoscope文体で出力可
    md.append(format_centers(
        defined_centers,
        undefined_centers,
        poetic=poetic
    ))
    md.append("\n")

    # Defined Channels
    md.append("---\n\n#### 🔸 Defined Channels")
    md.append(generate_channel_section(chart['defined_channels'], channel_definitions))
    defined_channels = chart.get("defined_channels", [])
    defined_centers, undefined_centers = get_defined_undefined_centers(defined_channels, channel_definitions)
    
    print("Defined channels in chart:", defined_channels)
    print("→ Extracted center keys:", defined_centers)

    md.append("\n")

    # Gates
    md.append("---\n\n#### 🔑 Gates Activated")
    md.append(generate_gate_section(chart, gate_definitions))
    md.append(generate_gate_section("🖤 Personality Gates", personality["gates"], gate_definitions))
    md.append("\n")
    md.append(generate_gate_section("🔴 Design Gates", design["gates"], gate_definitions))
    md.append("\n")

    return "\n".join(md)

    # Variables
    md.append("---\n\n#### 🧭 Variables")
    md.append(generate_variable_section(variables))
    md.append(f"- Orientation: {variables.get('orientation', 'N/A')}")
    md.append(f"- Digestion: {variables['digestion']}")
    md.append(f"- Environment: {variables['environment']}")
    md.append(f"- Perspective: {variables['perspective']}")
    md.append(f"- Motivation: {variables['motivation']}")
    md.append(f"- View: {variables.get('view', 'N/A')}")
    md.append("\n")

    # PHS
    md.append("---\n\n#### 🧠 PHS（Primary Health System）")
    md.append(f"- Digestion: {phs['digestion']}")
    md.append(f"- Environment: {phs['environment']}")
    md.append(f"- Perspective: {phs['perspective']}")
    md.append(f"- Motivation: {phs['motivation']}")
    md.append("\n")

    # MDC
    md.append("---\n\n#### 🧬 MDC（Mythological Design Composite）")
    mdc = chart.get("mdc", {})
    md.append(f"- Composite Name: **\"{mdc.get('name', 'N/A')}\"**")
    md.append(f"- Channels Referenced: {mdc.get('channels', [])}")
    md.append(f"- Keywords: {mdc.get('keywords', [])}")
    md.append(f"- Design Language: {mdc.get('design_language', 'N/A')}")

    return '\n'.join(md)

def get_gate_info(gate_number, gate_definitions):
    gate_str = str(gate_number)
    return gate_definitions.get(gate_str, {})

def get_defined_undefined_centers(defined_channels, channel_definitions):
    defined_centers = set()

    for ch_entry in defined_channels:
        if isinstance(ch_entry, dict):
            ch = ch_entry.get("channel")
        elif isinstance(ch_entry, str):
            ch = ch_entry
        else:
            continue  # 無効な形式はスキップ

        info = find_channel_definition(channel_definitions, ch)
        if info:
            centers = info.get("centers", [])
            defined_centers.update(centers)

    undefined_centers = [c for c in ALL_CENTERS if c not in defined_centers]
    return sorted(list(defined_centers)), sorted(undefined_centers)

def format_centers(defined, undefined, poetic=False):
    center_names = {
        "Head": "Thought Crown",
        "Ajna": "Vision Gate",
        "Throat": "Voice Field",
        "G": "Identity Matrix",
        "Heart": "Will Forge",
        "Sacral": "Generative Engine",
        "Solar Plexus": "Emotional Core",
        "Spleen": "Intuition Field",
        "Root": "Base Pulse"
    }

    def convert(names):
        return [center_names.get(name, name) if poetic else name for name in names]

    defined_formatted = ', '.join(convert(defined)) if defined else "None"
    undefined_formatted = ', '.join(convert(undefined)) if undefined else "None"

    return f"**Defined**: {defined_formatted}\n**Undefined**: {undefined_formatted}"

    # PersonalityとDesignのGatesを抽出
    personality_gates = []
    design_gates = []
    for planet, g in raw_gates.items():
        gl_str = f"{g['gate']}.{g['line']}"
        if planet in personality_pos:
            personality_gates.append(gl_str)
        elif planet in design_pos:
            design_gates.append(gl_str)

    return {
        "chart": {
            "planet_positions": personality_pos,
            "gates": gates,
            "active_channels": enriched_channels,
            "defined_centers": defined_centers,
            "profile": profile,
            "authority": authority,
            "variables": variables,
            "mbti_suggestion": mbti_suggestion,
            "personality": {
                "gates": personality_gates
            },
            "design": {
                "gates": design_gates
            }
        },
        "rave_chart": {
            "birth": {
                "date": f"{birth_data['year']:04d}-{birth_data['month']:02d}-{birth_data['day']:02d}",
                "time": f"{birth_data['hour']:02d}:{birth_data['minute']:02d}",
                "location": birth_data["location"]
            }
        }
    }


# Example usage
if __name__ == '__main__':
    input_json = "data/kairoscope-hd-profile.json"
    output_md = 'output/kairoscope-hd-profile.md'

    data = load_kairoscope_json(input_json)
    md_text = generate_kairoscope_md(data)
    save_md(md_text, output_md)
    print(f"✅ .mdファイルを生成しました → {output_md}")


# 自動生成に必要な出生情報（ここ、後で引数化可）
birth_info = {
    "year": 1983,
    "month": 5,
    "day": 1,
    "hour": 12,
    "minute": 0,
    "timezone": "Asia/Tokyo",
    "location": "Aomori"
}

# チャート生成して、data.json を output/ に書き出し
chart_data = build_chart(birth_info)
os.makedirs("output", exist_ok=True)
with open("output/data.json", "w") as f:
    json.dump(chart_data, f, indent=2, ensure_ascii=False)

# Markdown化処理（本体）
md_text = generate_kairoscope_md(chart_data)
with open("output/kairoscope_chart.md", "w") as f:
    f.write(md_text)

print("✅ Kairoscope Markdown 出力完了！→ output/kairoscope_chart.md")
print(chart_data.keys())  # → dict_keys(['chart', 'rave_chart'])

