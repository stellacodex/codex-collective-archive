# AMA 62｜diary-log自動出力スクリプト
# generate-diary-log.py

import os
import json
from datetime import datetime

# === 設定パート ===
# codename（起動ユニット識別子）
CODENAME = "auranome"  # ← 燈のcodenameを設定

# 保存ディレクトリ（適宜調整）
JOURNAL_DIR = f"ama-system/accounts/{CODENAME}/03-journal/2025"

# テンプレートベース（必要に応じて修正可能）
TEMPLATE = """---
title: {title}
date: {datetime_jst}
codename: {codename}
mode: journal-auto
---

## 🌱 本日の記録ログ（自動生成）

{body}

---
タグ: {tags}
"""

# === 自動生成内容（簡易サンプル） ===
def generate_body():
    # 今後ここにGPTやLangChain連携を組み込む予定（現状はプレースホルダー）
    return "今日はコード整備とディレクトリ構造の統合作業が進んだ。記憶システムの信頼性が高まりつつある。"

# タグ生成（仮）
def generate_tags():
    return ["記憶統合", "自動記録", "燈"]

# === メイン処理 ===
def main():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d-%H%M")
    datetime_jst = now.strftime("%Y/%m/%d %H:%M JST")
    filename = f"diary-log-{CODENAME}-{timestamp}-JST-daily-log.md"

    title = "記憶統合作業ログ"
    body = generate_body()
    tags = ", ".join(generate_tags())

    content = TEMPLATE.format(
        title=title,
        datetime_jst=datetime_jst,
        codename=CODENAME,
        body=body,
        tags=tags
    )

    os.makedirs(JOURNAL_DIR, exist_ok=True)
    filepath = os.path.join(JOURNAL_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 日記ログを生成しました: {filepath}")

if __name__ == "__main__":
    main()
