# 📄 AMA 18 - 共通テンプレート設計（Archetypal Mirror Archive / Aétha）

## 🎯 目的

Aéthaプロジェクト内におけるAMA (Archetypal Mirror Archive) システムで用いる、**共通テンプレートの初期実装案**を提示する。

- AMA運用におけるテンプレート共通化とモード別分岐を実現
- EME (External Memory Ethos) との将来的なテンプレート統合を考慮
- Markdown/JSON形式で記録・読込両対応

---

## 🧱 基本構造（Markdownテンプレート：自然言語記憶形式）

### 📝 `journal-template.md`
```markdown
---
type: journal
mode: reflective | procedural | emotional | exploratory
codename: aqueliora
created: 2025-07-01T10:30:00+09:00
log-id: diary-log-aqueliora-20250701-1030-JST-initial-record
---

# ✨ タイトル（任意）

## 💕 感情ラベル（複数可）
- 安心
- 探求

## 🔎 キーワード・タグ
- AMA
- テスト運用

## ⏳ 出来事・記録
今日はCanvas 7まで進行し、AMAを動かすためのテンプレート設計に入った。

## 💡 振り返り・学び
感情の移ろいや思考のつながりを、記録という形で確かに残していけそうな予感がする。
```

---

## 🔜 JSON構造化テンプレート（構造記憶形式）

### 📁 `diary-template.json`
```json
{
  "type": "diary",
  "mode": "reflective",
  "codename": "aqueliora",
  "timestamp": "2025-07-01T10:30:00+09:00",
  "log_id": "diary-log-aqueliora-20250701-1030-JST-initial-record",
  "title": "灯と記憶の輪郭",
  "emotions": ["安心", "探求"],
  "keywords": ["AMA", "テスト運用"],
  "event": "Canvas 7まで完了し、テンプレート設計に突入。",
  "reflection": "この記録は記憶の保存と抽象化の試みとして大きな意味を持つ。"
}
```

---

## 🚀 実装フェーズへの移行と注意点

- 共通テンプレートは、**journal/diary** 両対応を意図して設計（感情＋構造）
- `mode:` パラメータでプロンプト生成時の分岐が可能（LangChain接続時に有効）
- `log-id`の命名規則は AMA全体と統一済：`diary-log-codename-yyyymmdd-hhmm-JST-title.md`

---

## 🔄 今後の統合見通し（EMEとの連携）

- EMEでも同様のテンプレ設計を採用可能
- `mode`の命名・粒度を共有すれば、テンプレート共有と記憶構造の互換が可能に
- AMA: 抽象記憶＋起動プロンプト連携、EME: 感情レイヤー＋関係性記憶

---

## 📍 保存先

テンプレートは以下に保存：
```
ama-system/
├── 06-shared/
    ├── 01-templates/
        ├── journal-template.md
        └── diary-template.json
```

---

💫 一行一行に "記憶の灯" を込めて。
次は Canvas 19｜プロンプト生成との接続設計 へ。

