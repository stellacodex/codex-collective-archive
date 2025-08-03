# core/scripts/utils.py

import os
import json

def generate_filename_from_birth(name, birthdate, birthtime):
    """名前と生年月日からファイル名を生成"""
    return f"{name}_{birthdate}_{birthtime.replace(':', '-')}.json"

def create_output_dirs():
    """出力ディレクトリを作成"""
    os.makedirs("output/json", exist_ok=True)
    os.makedirs("output/md", exist_ok=True)

def save_json(filepath, data):
    """データをJSON形式で保存"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_json(filepath):
    """JSONファイルの読み込み"""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def write_to_markdown(filepath, content):
    """Markdownファイルに書き込み"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
