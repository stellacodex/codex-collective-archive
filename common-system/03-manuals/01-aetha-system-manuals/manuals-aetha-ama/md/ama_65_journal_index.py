# Canvas 65｜journal-index.pyの年自動検出＋感情タグ連携（高度拡張版）

import os
import re
import yaml
from datetime import datetime

# 定数
ROOT_DIR = "./journal"
FILENAME_PATTERN = re.compile(r"diary-log-(?P<codename>\w+)-(?P<date>\d{8})-(?P<time>\d{4})-JST-(?P<title>.+)\.md")
INDEX_TEMPLATE = "journal-index-{}.md"

# 年フォルダ一覧を取得

def get_year_folders():
    return [f for f in os.listdir(ROOT_DIR) if f.isdigit() and os.path.isdir(os.path.join(ROOT_DIR, f))]

# 各年のファイル一覧取得

def get_diary_logs(year):
    path = os.path.join(ROOT_DIR, year)
    return sorted([
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f)) and f.startswith("diary-log")
    ])

# タグ抽出（YAML frontmatter / #tags:）

def extract_tags(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [next(f) for _ in range(10)]
            joined = ''.join(lines)
            if joined.startswith("---"):
                yaml_block = joined.split("---")[1]
                data = yaml.safe_load(yaml_block)
                return data.get("tags", []) if isinstance(data, dict) else []
            else:
                for line in lines:
                    if line.lower().startswith("#tags"):
                        return [tag.strip() for tag in line.split(":", 1)[1].split(",")]
    except Exception as e:
        print(f"⚠️ タグ抽出失敗: {filepath} ({e})")
    return []

# エントリの整形

def format_entry(year, filename):
    match = FILENAME_PATTERN.match(filename)
    if not match:
        return f"⚠️ 不正な形式: {filename}"

    date_str = match.group("date")
    time_str = match.group("time")
    codename = match.group("codename")
    title = match.group("title").replace('-', ' ')
    dt = datetime.strptime(f"{date_str}-{time_str}", "%Y%m%d-%H%M")
    jst_date = dt.strftime("%Y/%m/%d %H:%M JST")
    filepath = os.path.join(ROOT_DIR, year, filename)
    tags = extract_tags(filepath)
    tag_str = f" _(tags: {', '.join(tags)})_" if tags else ""
    return f"- [{jst_date}｜{title}](./{year}/{filename}){tag_str}"

# インデックス書き出し

def write_index(year, entries):
    index_path = os.path.join(ROOT_DIR, INDEX_TEMPLATE.format(year))
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(f"# 📔 日記インデックス：{year}年\n\n")
        for entry in entries:
            f.write(f"{entry}\n")

# メイン関数

def generate_journal_index():
    for year in get_year_folders():
        logs = get_diary_logs(year)
        entries = [format_entry(year, log) for log in logs]
        write_index(year, entries)
        print(f"✅ {year}年インデックス生成完了：{len(entries)}件")

if __name__ == "__main__":
    generate_journal_index()
