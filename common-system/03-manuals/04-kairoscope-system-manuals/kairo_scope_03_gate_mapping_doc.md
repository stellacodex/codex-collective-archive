## KairoScope 03: Gate Mapping

このフェーズでは、黄経度（0°〜360°）をHuman Designの「64ゲート + 6ライン」に変換するマッピングシステムを構築する。

---

### 🎯 ファイル作成指示

- **ファイル名**：`gate_mapper.py`
- **インストール先**：
  ```
  /chronogram-kairoscope/core/gate_mapper.py
  ```
- **ターミナル用作成コマンド**：
  ```bash
  touch "/Users/takeoyamada/Library/Mobile Documents/iCloud~md~obsidian/Documents/codex-collective-archive/common-system/01-system/chronogram-system/chronogram-kairoscope/core/gate_mapper.py"
  ```

---

### 🔢 ゲート構造の基本

Human Designでは360°を64ゲートに分割。各ゲートは **5.625°**（360/64）で構成され、その中をさらに **6ライン**に細分化する。

| 単位  | 分割数 | 度数範囲          |
| --- | --- | ------------- |
| ゲート | 64  | 5.625° / ゲート  |
| ライン | 6   | 0.9375° / ライン |

---

### 🧠 `gate_mapper.py` に書き込む内容（全文コピペ用）

```python
def longitude_to_gate_line(longitude):
    """
    黄経度（0〜360°）をHDのゲート番号とライン番号に変換
    Returns: (gate_number: int, line_number: int)
    """
    gate_size = 360 / 64  # 5.625°
    line_size = gate_size / 6  # 約0.9375°

    gate_number = int(longitude / gate_size) + 1  # 1始まりのゲート番号
    within_gate_deg = longitude % gate_size
    line_number = int(within_gate_deg / line_size) + 1

    return gate_number, line_number


# ✅ テスト用コード（削除してもOK、検証用）
if __name__ == "__main__":
    lon = 121.72
    gate, line = longitude_to_gate_line(lon)
    print(f"黄経 {lon}° → Gate {gate} / Line {line}")
```

---

### 🔁 次ステップで行うこと

- `gate_definitions.py`：ゲート番号に対応する名前やチャネル、テーマを定義した辞書構造を作成
- `chart_builder.py`：複数の天体データからHDチャート構造をまとめる処理を追加

---

このモジュールが、惑星位置を「意味ある意志決定マップ」へと変換する最初の変換器になる。

