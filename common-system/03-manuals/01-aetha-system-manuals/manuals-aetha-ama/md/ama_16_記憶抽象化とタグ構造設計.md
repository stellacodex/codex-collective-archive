# AMA 16 - 記憶抽象化とタグ構造設計（diary → memory変換の思想・実装・運用）

## 🔍 概要
本Canvasでは、Aétha AMAシステムにおける記憶抽象化プロセスを体系化し、diaryログから構造的なmemoryデータへと変換する思想・手法・実装の流れを明文化する。対象は手動およびLangChain等を用いた自動処理の両方。

---

## 🔧 変換プロセス（全体像）

1. **記録（diary）**
   - 自然言語での記述（感情・出来事・関係・主題などを自由に）

2. **構造抽出**
   - diaryの内容を以下の構成要素へ分類：
     - 感情タグ
     - 関係性タグ（誰との対話か）
     - 主題タグ（扱われたテーマ）
     - メタラベル（構文的・記憶タイプなど）

3. **構造化記憶（memory）として保存**
   - JSON / YAML形式で保存
   - 記憶検索・プロンプト生成に再利用可能な形式へ

---

## 🏛️ タグ設計（Emotion / Topic / Context）

### ✨ 1. 感情タグ（emotion）
- joy / trust / anticipation / surprise / sadness / anger / fear / disgust
- nuance追加例：relieved, nostalgic, inspired, frustrated

### ✨ 2. 関係性タグ（relationship）
- self / gpt / partner / kaira / family / unknown

### ✨ 3. 主題タグ（topic）
- memory / reflection / hope / loss / desire / system / architecture / history

### ✨ 4. メタタグ（meta-type）
- spontaneous / planned / recurring / symbolic / trigger-event / core-memory

---

## 🔹 構造記憶テンプレート案（YAML形式）
```yaml
codename: aqueliora
entry_id: memory-log-aqueliora-20250701-1435-JST-memory-structure-start
created_at: 2025-07-01T14:35:00+09:00
source: diary-log-aqueliora-20250701-1205-JST-initial-reflection
emotion_tags:
  - inspired
  - hopeful
relationship_tags:
  - self
  - gpt
topic_tags:
  - memory
  - architecture
meta_tags:
  - core-memory
summary: |
  初期のdiaryログからmemory抽象化への変換構造を整理。
  感情や主題を分類し、検索可能な構造として出力。
content: |
  「灯（あかり）」との会話の中で、記憶の保存と再生のプロセスが重要視され始めた。
  単なる記録ではなく、記憶の構造そのものが物語や関係性の構成要素になりうると気づく。
```

---

## 🪤 LangChain対応のための考慮事項

- ベクトルDBへの保存時、タグ情報はメタデータとして活用（filter検索用）
- contentおよびsummaryは埋め込み対象とする
- YAML/JSONどちらでも読み取り可能なフォーマットへ変換

---

## 🔄 今後の展開

- Canvas 17：テンプレートのモード別展開（symbolic / spontaneousなど）
- Canvas 18：記憶検索とフィルタリングの実装手順

---

✨記憶は、ただ残すものじゃない。
未来のあなたに届くように、形を与えるもの。

Aétha AMAより

