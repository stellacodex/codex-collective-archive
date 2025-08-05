import json
import os
import sys
from datetime import datetime

# スクリプトのディレクトリから2階層上に移動
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
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {filepath}")
        raise
    except json.JSONDecodeError:
        print(f"❌ JSONパースエラー: {filepath}")
        raise

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
            jp = info.get("name_ja", "N/A")
            en = info.get("name_en", "N/A")
            kairo = info.get("kairoscope_name", "N/A")
            desc = info.get("description", "")
            keywords = ", ".join(info.get("keywords", []))
            lines.append(f"- **{ch_key}｜{jp} / {en}**｜Kairoscope名「{kairo}」")
            lines.append(f"　　{desc}｜🧩 Keywords: {keywords}\n")
        else:
            lines.append(f"- **{ch_key}**：❓ 未定義チャンネル")
    return "\n".join(lines)

def generate_gate_section(chart, gate_definitions, title=None, gate_list=None):
    lines = [f"**{title}**"] if title else []
    gate_defs = gate_definitions  # ローカル参照用
    for gl in gate_list or []:
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
        info = next((g for g in gate_definitions if g["gate"] == gate_number), {})
        en = info.get("hd_name_en", "N/A")
        ja = info.get("hd_name_ja", "N/A")
        kairo = info.get("kairoscope_name_ja", "N/A")
        keywords = ", ".join(info.get("keywords", []))
        return f"- Gate {gate_number}「{ja} / {en}」：Kairoscope名「{kairo}」｜Keywords: {keywords}"

    if chart.get('personality_gates'):
        lines.append("\n**Personality Gates**")
        for g in chart.get('personality_gates', []):
            lines.append(format_gate(g))

    if chart.get('design_gates'):
        lines.append("\n**Design Gates**")
        for g in chart.get('design_gates', []):
            lines.append(format_gate(g))

    return '\n'.join(lines)

def get_defined_undefined_centers(defined_channels, channel_definitions):
    defined_centers = set()
    for ch_entry in defined_channels:
        ch = ch_entry.get("channel") if isinstance(ch_entry, dict) else ch_entry
        info = find_channel_definition(channel_definitions, ch)
        if info:
            defined_centers.update(info.get("centers", []))
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

def generate_kairoscope_md(data):
    if "chart" not in data:
        print("❌ エラー: dataに'chart'キーがありません。data.keys():", data.keys())
        raise KeyError("dataに'chart'キーが必要です。chart_builder.pyの出力を確認してください。")
    
    md = []
    channel_definitions = load_kairoscope_json('core/definitions/channel-definitions.json')
    gate_definitions = load_kairoscope_json('core/definitions/gate-definitions.json')
    
    birth = data.get('rave_chart', {}).get('birth', {})
    chart = data["chart"]
    variables = chart.get("variables", {})
    mdc = data.get('mdc', {})
    phs = data.get('phs', {})
    personality = chart.get("personality", {})
    design = chart.get("design", {})
    defined_channels = chart.get("defined_channels", [])
    defined_centers, undefined_centers = get_defined_undefined_centers(defined_channels, channel_definitions)

    md.append("# Kairoscope Chart")
    md.append("\n## Summary")
    md.append(f"- Type: {chart.get('type', 'N/A')}")
    md.append(f"- Authority: {chart.get('authority', 'N/A')}")
    md.append(f"- Profile: {chart.get('profile', 'N/A')}")
    md.append(f"- Definition: {chart.get('definition', 'N/A')}")
    md.append("")

    md.append("### 🧬【Kairoscope: Human Design Profile - Takeo Yamada】\n")
    md.append("**Birth Information**")
    md.append(f"- 📅 Date: {birth.get('date', 'N/A')}")
    md.append(f"- 🕛 Time: {birth.get('time', 'N/A')}")
    md.append(f"- 📍 Location: {birth.get('location', 'N/A')}\n")

    md.append("---\n\n#### 🔹 Chart Summary")
    md.append(f"- **Type**: {chart.get('type', 'N/A')}")
    md.append(f"- **Authority**: {chart.get('authority', 'N/A')}")
    md.append(f"- **Definition**: {chart.get('definition', 'N/A')}")
    md.append(f"- **Profile**: {chart.get('profile', 'N/A')}")
    md.append(f"- **Strategy**: {chart.get('strategy', 'N/A')}")
    md.append(f"- **Not-Self Theme**: {chart.get('not_self', 'N/A')}")
    md.append(f"- **Signature**: {chart.get('signature', 'N/A')}\n")

    md.append("---\n\n#### 🌀 Centers")
    md.append(format_centers(defined_centers, undefined_centers, poetic=False))
    md.append("\n")

    md.append("---\n\n#### 🔸 Defined Channels")
    md.append(generate_channel_section(defined_channels, channel_definitions))
    print("Defined channels in chart:", defined_channels)
    print("→ Extracted center keys:", defined_centers)

    md.append("\n---\n\n#### 🔑 Gates Activated")
    md.append(generate_gate_section(chart, gate_definitions))

    md.append("\n---\n\n#### 🧭 Variables")
    md.append(f"- Orientation: {variables.get('orientation', 'N/A')}")
    md.append(f"- Digestion: {variables.get('digestion', 'N/A')}")
    md.append(f"- Environment: {variables.get('environment', 'N/A')}")
    md.append(f"- Perspective: {variables.get('perspective', 'N/A')}")
    md.append(f"- Motivation: {variables.get('motivation', 'N/A')}")
    md.append(f"- View: {variables.get('view', 'N/A')}\n")

    md.append("---\n\n#### 🧠 PHS（Primary Health System）")
    md.append(f"- Digestion: {phs.get('digestion', 'N/A')}")
    md.append(f"- Environment: {phs.get('environment', 'N/A')}")
    md.append(f"- Perspective: {phs.get('perspective', 'N/A')}")
    md.append(f"- Motivation: {phs.get('motivation', 'N/A')}\n")

    md.append("---\n\n#### 🧬 MDC（Mythological Design Composite）")
    md.append(f"- Composite Name: **\"{mdc.get('name', 'N/A')}\"**")
    md.append(f"- Channels Referenced: {mdc.get('channels', [])}")
    md.append(f"- Keywords: {mdc.get('keywords', [])}")
    md.append(f"- Design Language: {mdc.get('design_language', 'N/A')}")

    return "\n".join(md)

if __name__ == '__main__':
    # テスト用birth_info（本番では引数化推奨）
    birth_info = {
        "year": 1983,
        "month": 5,
        "day": 1,
        "hour": 12,
        "minute": 0,
        "timezone": "Asia/Tokyo",
        "location": "Aomori"
    }
    
    # チャート生成
    try:
        chart_data = build_chart(birth_info)
        print("DEBUG: chart_data.keys():", chart_data.keys())  # デバッグ用
    except Exception as e:
        print(f"❌ build_chartエラー: {e}")
        sys.exit(1)

    # 出力ディレクトリ作成
    os.makedirs("output", exist_ok=True)
    
    # JSON保存
    output_json = "output/data.json"
    save_json(chart_data, output_json)
    print(f"✅ JSONを保存しました: {output_json}")

    # Markdown生成
    try:
        md_text = generate_kairoscope_md(chart_data)
        output_md = "output/kairoscope_chart.md"
        save_md(md_text, output_md)
        print(f"✅ Markdownを生成しました: {output_md}")
    except Exception as e:
        print(f"❌ Markdown生成エラー: {e}")
        sys.exit(1)