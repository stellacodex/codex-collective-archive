import os
import re
from datetime import datetime

# ルートディレクトリの指定（必要に応じてパスを変更）
ROOT_DIR = "./03-journal"

# 出力先テンプレート
INDEX_TEMPLATE = "journal-index-{}.md"

# 日記ログファイル名のパターン
FILENAME_PATTERN = re.compile(r"diary-log-(?P<codename>\w+)-(?P<date>\d{8})-(?P<time>\d{4})-JST-(?P<title>.+)\.md")

# 年フォルダ（例：2025など）を取得
def get_year_folders():
    return [f for f in os.listdir(ROOT_DIR) if f.isdigit() and os.path.isdir(os.path.join(ROOT_DIR, f))]

# 各年のフォルダ内ファイルを取得
def get_diary_logs(year):
    path = os.path.join(ROOT_DIR, year)
    return sorted([
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f)) and f.startswith("diary-log")
    ])

# インデックスファイルを書き出し
def write_index(year, entries):
    index_path = os.path.join(ROOT_DIR, INDEX_TEMPLATE.format(year))
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(f"# 📔 日記インデックス：{year}年\n\n")
        for entry in entries:
            f.write(f"- {entry}\n")

# エントリをMarkdownリンクに整形
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
    link = f"[{jst_date}｜{title}](./{year}/{filename})"
    return link

# メイン処理
def generate_journal_index():
    for year in get_year_folders():
        logs = get_diary_logs(year)
        entries = [format_entry(year, log) for log in logs]
        write_index(year, entries)
        print(f"✅ {year}年インデックス生成完了：{len(entries)}件")

if __name__ == "__main__":
    generate_journal_index()