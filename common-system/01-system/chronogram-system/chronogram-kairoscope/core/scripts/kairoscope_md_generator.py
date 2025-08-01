# kairoscope_md_generator.py

import json
with open('core/definitions/channel-definitions.json', 'r') as f:
    channel_definitions = json.load(f)
    
import json
with open('core/definitions/gate-definitions.json', 'r') as f:
    gate_definitions = json.load(f)

import json
from datetime import datetime

ALL_CENTERS = [
    "Head", "Ajna", "Throat", "G", "Heart", "Sacral",
    "Solar Plexus", "Spleen", "Root"
]

def load_kairoscope_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_kairoscope_md(data):
    birth = data['rave_chart']['birth']
    chart = data['rave_chart']
    mdc = data['mdc']
    phs = data['phs']

    md = []

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
    md.append(f"- **Strategy**: Wait for the Invitation")
    md.append(f"- **Not-Self Theme**: Bitterness")
    md.append(f"- **Signature**: Success\n")

    # Defined Channels
    md.append("---\n\n#### 🔸 Defined Channels")
    md.append(generate_channel_section(chart['defined_channels'], channel_definitions))
    defined_channels = chart.get("defined_channels", [])
    defined_centers, undefined_centers = get_defined_undefined_centers(defined_channels, channel_definitions)
    md.append("")

    # Centers
    md.append("---\n\n#### 🌀 Centers")
    poetic = False  # True にすればKairoscope文体で出力可
    md.append(format_centers(
        defined_centers,
        undefined_centers,
        poetic=poetic
    ))
    md.append("")

    # Gates
    md.append("---\n\n#### 🔑 Gates Activated")
    md.append(generate_gate_section(chart, gate_definitions))
    md.append("")

    # Variables / PHS
    md.append("---\n\n#### 🧭 Variables")
    md.append(f"- Orientation: {chart.get('variables', {}).get('orientation', 'N/A')}")
    md.append(f"- Digestion: {phs['digestion']}")
    md.append(f"- Environment: {phs['environment']}")
    md.append(f"- Perspective: {phs['perspective']}")
    md.append(f"- Motivation: {phs['motivation']}")
    md.append(f"- View: Personal\n")

    # PHS
    md.append("---\n\n#### 🧠 PHS（Primary Health System）")
    md.append(f"- Digestion: {phs['digestion']}")
    md.append(f"- Environment: {phs['environment']}")
    md.append(f"- Perspective: {phs['perspective']}")
    md.append(f"- Motivation: {phs['motivation']}\n")

    # MDC
    md.append("---\n\n#### 🧬 MDC（Mythological Design Composite）")
    md.append(f"- Composite Name: **\"{mdc['composite_name']}\"**")
    md.append(f"- Channels Referenced: {mdc['channels']}")
    md.append(f"- Keywords: {mdc['keywords']}")
    md.append(f"- Design Language: {mdc['design_language']}")

    return '\n'.join(md)

def get_gate_info(gate_number, gate_definitions):
    gate_str = str(gate_number)
    return gate_definitions.get(gate_str, {})

def generate_gate_section(chart, gate_definitions):
    lines = []

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

def get_defined_undefined_centers(defined_channels, channel_definitions):
    defined_centers = set()

    for ch_entry in defined_channels:
        if isinstance(ch_entry, dict):
            ch = ch_entry.get("channel")
        elif isinstance(ch_entry, str):
            ch = ch_entry
        else:
            continue  # 無効な形式はスキップ

        if ch in channel_definitions:
            centers = channel_definitions[ch].get("centers", [])
            if centers:
                defined_centers.update(centers)

    undefined_centers = [c for c in ALL_CENTERS if c not in defined_centers]
    return sorted(list(defined_centers)), sorted(undefined_centers)



def generate_channel_section(defined_channels, channel_definitions):
    lines = []
    for ch_entry in defined_channels:
        ch_key = ch_entry if isinstance(ch_entry, str) else ch_entry.get('channel')
        if ch_key in channel_definitions:
            info = channel_definitions[ch_key]
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

# Example usage
if __name__ == '__main__':
    input_json = "data/kairoscope-hd-profile.json"
    output_md = 'output/kairoscope-hd-profile.md'

    data = load_kairoscope_json(input_json)
    md_text = generate_kairoscope_md(data)
    save_md(md_text, output_md)
    print(f"✅ .mdファイルを生成しました → {output_md}")

    print("Defined channels in chart:", defined_channels)
    print("→ Extracted center keys:", defined_centers)
