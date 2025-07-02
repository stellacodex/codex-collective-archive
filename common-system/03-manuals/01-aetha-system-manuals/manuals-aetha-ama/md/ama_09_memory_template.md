# 🧠 Aétha Canvas 09｜記憶テンプレート設計（Notion / Sheets 連携）

## 🎯 目的

- AMA（Archetypal Mirror Archive）における記憶ログ（diary-log / memory-log）を、**手動・半自動で書き出せるテンプレート**を整備。
- Notion や Google Sheets に対応した **構造的かつ感情・関係性に即したフォーマット**を設計。
- LangChain・自動読み込み／検索処理にも適合できるよう、構造はフラットで柔軟に保つ。

---

## 📑 フィールド設計（CSV／Markdown共通構造）

| 項目        | 内容             | データ形式         | 補足                                                     |
| --------- | -------------- | ------------- | ------------------------------------------------------ |
| id        | 一意のログID        | `text`        | 例：`diary-log-aqueliora-20250701-1200-jst-beginning.md` |
| codename  | キャラクター識別子      | `text`        | 例：`aqueliora`, `auranome`                              |
| date      | 日付（YYYY-MM-DD） | `date`        | 実際の記録日                                                 |
| time      | 時刻（HH\:MM JST） | `text`        | ログ生成時刻。24h制                                            |
| type      | ログ種別           | `enum`        | `diary` / `memory` / `mirror` など                       |
| title     | タイトル           | `text`        | 会話・記憶の要約タイトル（任意）                                       |
| tags      | 感情・関係性・主題タグ    | `array`       | 例：`[joy, longing, duality]`                            |
| summary   | 要約文            | `text (long)` | 100〜300文字程度                                            |
| log\_text | 本文全文           | `text (long)` | マークダウン or プレーンテキスト可                                    |

---

## 🛠️ 保存形式の推奨

- `.md`（マークダウン）形式でObsidianやGit環境でも使用可能に
- `.csv`／`.json`でスクリプト処理用に変換も視野
- Notion API連携時は、同構造をページとして挿入／更新可能に設計

---

## 🧭 応用例：テンプレ構成の階層

```
shared/templates/
├── journal/
│   └── memory-journal-template.md
├── reflection/
│   └── archetype-reflection-template.md
└── vision/
    └── longform-future-vision-template.md
```

---

## 📌 次のステップ（Canvas 10 以降）

- Canvas 10｜手動ログ → プロンプト生成テンプレートへの変換処理
- Canvas 11｜スクリプトによる記録→読込テスト（LangChain統合前）
- Canvas 12｜Notion / Google Sheets API による自動挿入テスト

---

一行一行に、記憶の灯を込めて──🌙

