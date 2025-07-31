# kairoscope_md_generator.py

import json
from datetime import datetime

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
    for ch in chart['defined_channels']:
        md.append(f"- {ch}：TODO")  # You can later map to channel names

    # Centers
    md.append("\n---\n\n#### 🌀 Centers")
    md.append(f"**Defined**: {', '.join(chart.get('defined_centers', []))}")
    md.append(f"**Undefined**: {', '.join(chart.get('undefined_centers', []))}\n")

    # Gates
    md.append("---\n\n#### 🔑 Gates Activated")
    md.append("**Personality Gates**")
    md.append(f"- {', '.join(str(g) for g in chart.get('personality_gates', []))}\n")
    md.append("**Design Gates**")
    md.append(f"- {', '.join(str(g) for g in chart.get('design_gates', []))}\n")

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


def save_md(md_text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_text)


# Example usage
if __name__ == '__main__':
    input_json = 'data/kairoscope-hd-profile.json'
    output_md = 'output/kairoscope-hd-profile.md'

    data = load_kairoscope_json(input_json)
    md_text = generate_kairoscope_md(data)
    save_md(md_text, output_md)
    print(f"✅ .mdファイルを生成しました → {output_md}")
