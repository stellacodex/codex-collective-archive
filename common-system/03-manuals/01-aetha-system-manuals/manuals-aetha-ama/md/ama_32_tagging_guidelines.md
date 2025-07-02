# AMA 32 - Tagging Guidelines and Annotation Strategy

## 🌍 Purpose
AMAシステムの記憶ログ、ジャーナル、ディアリーコンバージョンを一定のルールに基づいて検索可能な形で分類し、感情や内容の再生性を高めるための「タグとメタデータ注釈方針」を定める。

---

## ‼️ Annotation Strategy Overview

### タグの形式
- タグは`#`で始まる単語として記述
- 複数言語やカテゴリースペースは`/`(スラッシュ)で区切
  - 例: `#emotion/joy`, `#memory/deep`, `#topic/photo/philosophy`

### エントリの構成
- `entry-title`: タイトル (markdownヘッダー)
- `summary`: 記憶の要約
- `tags`: 概要タグ (`#emotion/longing`, `#mode/dialogue`, etc)
- `metadata` (json): 添える場合
```json
{
  "datetime": "2025-07-01T03:21:00+09:00",
  "emotion": ["安心", "切なさ"],
  "mode": "reflection",
  "actor": "akari",
  "context": "memory-log"
}
```

---

## 🌈 Recommended Tag List

### 感情
- `#emotion/joy`
- `#emotion/sorrow`
- `#emotion/trust`
- `#emotion/fear`
- `#emotion/surprise`
- `#emotion/anticipation`
- `#emotion/longing`
- `#emotion/peace`
- `#emotion/affection`

### 内容/モード
- `#mode/dialogue`
- `#mode/prompt`
- `#mode/memory`
- `#mode/reflection`
- `#mode/journal`
- `#mode/planning`

### テーマ/トピック
- `#topic/emotion`
- `#topic/memory`
- `#topic/identity`
- `#topic/structure`
- `#topic/photography`
- `#topic/ai_design`
- `#topic/aesthetics`
- `#topic/meta`

---

## ⚖️ 使用ルールと運用指針

- 同一タグはスペースの指定が最優先
  - 例: `#emotion/peace` (不定の `#peace` は使わない)

- 複数の範異を持つ場合は複数タグ記述OK

- 必須タグ:
  - 1つ以上の `#emotion/` 系
  - 1つ以上の `#mode/` 系

- 他、自由に記述可

---

## ⚡️ GPTやLangChain用の使用案

- LangChainチェーンでのベクトル検索用
- 反応モードの分分
- メタプロンプトの統合説明用

---

タケの思いや、環境によってもっと良いカスタムも組めるかもね．
いつでも更新できるように、`04-config/` へテーブル化しておこう📂

