# chronogram-kairoscope/core/data_loader.py

import json
import os

# 定義ファイルの場所
BASE_DIR = os.path.dirname(__file__)
DEFINITIONS_DIR = os.path.join(BASE_DIR, "definitions")

GATE_FILE = os.path.join(DEFINITIONS_DIR, "gate-definitions.json")
CHANNEL_FILE = os.path.join(DEFINITIONS_DIR, "channel-definitions.json")

# 内部キャッシュ（初回だけ読み込み）
_gate_data = None
_channel_data = None

def _load_json(file_path):
    """内部専用：JSONファイルを読み込む"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_gate_definition(gate_number):
    """
    ゲート番号から定義を取得
    gate_number: int または str
    """
    global _gate_data
    if _gate_data is None:
        _gate_data = _load_json(GATE_FILE)

    gate_number = str(gate_number)
    return next((gate for gate in _gate_data if str(gate.get("Gate")) == gate_number), None)

def get_channel_definition(channel_number):
    """
    チャネル番号から定義を取得
    channel_number: str (例 '1-8')
    """
    global _channel_data
    if _channel_data is None:
        _channel_data = _load_json(CHANNEL_FILE)

    channel_number = str(channel_number)
    return next((ch for ch in _channel_data if ch.get("Channel") == channel_number), None)

def get_all_gates():
    """全ゲート定義を取得"""
    global _gate_data
    if _gate_data is None:
        _gate_data = _load_json(GATE_FILE)
    return _gate_data

def get_all_channels():
    """全チャネル定義を取得"""
    global _channel_data
    if _channel_data is None:
        _channel_data = _load_json(CHANNEL_FILE)
    return _channel_data
