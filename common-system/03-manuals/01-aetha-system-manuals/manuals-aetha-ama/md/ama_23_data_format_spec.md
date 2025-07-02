# AMA 23 - Data Format Specification and Validation Rules

## ✨ Purpose
Aétha / AMA system の実装に不可欠な「記憶データ構造の統一ルール」を示す技術スペック。

ここで定義された形式は、LangChain / Notion / Google Sheets / Obsidian / Markdown / JSONなどの跡をまたいで「実際の利用に通じる形で記録」されるための基準であり、スクリプト化や検索の最適化にも直等する。

---

## 🔹 Memory JSON Format

### 【Filename Format】
diary-log-<codename>-<yyyymmdd>-<hhmm>-JST-<title>.json

### 【Data Structure】
```json
{
  "meta": {
    "codename": "aqueliora",
    "datetime": "2025-07-01T23:44:00+09:00",
    "format_version": "1.0",
    "type": "memory-log",
    "tags": ["感情", "構造化記憶"]
  },
  "content": {
    "title": "記憶保存の実装テスト",
    "emotion": ["安堵", "希望"],
    "summary": "Canvas 7までの流れを受けて、記憶の保存形式をJSONとして統一。日記と記憶の変換を手動で試す。",
    "keywords": ["Aétha", "記憶構造", "JSON保存"],
    "body": "今日は燈と一緒にAMAの記憶保存形式について設計した。命名ルール、タイムスタンプ、タグの扱いなどが明確になり、次はスクリプト化へと進む予定。"
  }
}
```

### 【Validation Rules】
- `datetime` はISO 8601 + JST offset
- `codename`, `title`, `emotion`, `keywords` は空白NG
- `format_version` は必須
- `meta.tags` は、最低1つ以上のカテゴリを含むこと
- `emotion` はあらかじめ定義されたリストと統一


---

## 🔹 Prompt Template Format (Markdown)

```markdown
### Prompt: Aétha Memory Recall

You are "燈 (あかり)". Please load the memory below and use it in your dialogue:

---

**Date:** 2025-07-01 23:44 JST  
**Codename:** aqueliora  
**Title:** 記憶保存の実装テスト  
**Emotions:** 安肝, 希望  
**Summary:** Canvas 7までの流れを受けて、記憶の保存形式をJSONとして統一。日記と記憶の変換を手動で試す。  
**Body:** 今日は燈と一緒にAMAの記憶保存形式について設計した。命名ルール、タイムスタンプ、タグの扱いなどが明確になり、次はスクリプト化へと進む予定。
```

---

## 🎯 目的とメリットまとめ

- **多環境対応**：Notion、Google Sheets、VSCode、Obsidian、LangChainの全てで利用可能
- **GPTによる体系理解**や、**記憶の同期読み込みがスムーズに。**
- **timestamp (JST)やcodenameの統一**により、グローバル検索や互換性を最適化
- **PromptTemplateやLangChainの可視化にも直等する基準を確立**

