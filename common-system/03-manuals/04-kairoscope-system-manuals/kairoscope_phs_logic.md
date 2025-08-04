了解、今回はCanvasがコードブロックで全文覆われないように、通常のテキストCanvasとして整理しなおすね。

---

# Kairoscope 03 - Variable Logic / PHS 計算ロジック構築

## ✨ 概要
KairoscopeのVariable計算ロジックを本格的に実装する段階に入った。

PHSロジックの標準的解釈に基づいて、Design Sun / Design Earth / Personality Sun / Personality Earthの計算を各位置で行い、Digestion / Environment / Perspective / Motivationの予測を行うロジックを稼働に作成する。

## 🏛 現在のステータス
- `astro_position.py` に Design Sun/Earth の計算関数 `get_design_positions()` を追加済み
- `variable_logic.py` での Variables (Digestion, Environment, Perspective, Motivation) 計算は、現在のロジックで「仮設ロジック」から、本格計算ロジックの実装へ移行している

## ★ PHS (Variable) 構成
| 項目 | ロジックソース |
|--------|----------------------------------|
| Digestion (Determination) | Design Sun の Gate + Line 計算 |
| Environment | Design Earth の Gate 計算 |
| Perspective | Personality Sun の Gate 計算 |
| Motivation | Personality Earth の Gate 計算 |

## ⚖️ ロジックの組織
- `astro_position.py`
  - `get_planet_positions()` の止め補用に `get_design_positions()` を作成
  - Design Time = Birth Time の累積 -88 日とする
- `chart_builder.py`
  - `build_chart()` 内で Personality / Design の両計算を実行
- `variable_logic.py`
  - 現在の簡易計算を実際の位置に基づく計算に編成

## 🚀 次のステップ
- `variable_logic.py`の本格実装を立ち上げる
  - Design/Personality Sun/Earth の Gate/Line を利用
  - Variant 機能と統合
- `time_variants.py` で variables も表示
- Chronogram で UI表示 + MBTIリンク

---

これ以降、通常のCanvasの表示を避ける為に
- **文章の先頭は説明文/テキストから始める**
- **一般の書式の時は初めにmarkdownのヘッダーなどを使う**
などの対策を使うようにするね。

さあ、このまま PHS ロジックの実装に進もう！

