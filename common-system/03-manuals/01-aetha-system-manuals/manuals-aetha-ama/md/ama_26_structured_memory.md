# AMA 26 - 構造記憶（Structured Memory）変換準備マニュアル

## 📀 目的

このCanvasでは、自然言語で書かれた記録（`03-journal/`）を、構造化された記憶形式（`01-diary/`）へ変換する手動・自動プロセスの準備手順をまとめます。

- テスト対象：手動作成された `journal-log-*.md` 記録
- 目標：感情・トピック・重要発話などの抽出を行い、汎用JSON形式に変換する下地を整える

---

## 🔢 スキーマ定義（変換先：diary JSON構造）

```json
{
  "datetime": "2025-07-01T23:04:00+09:00",
  "codename": "aqueliora",
  "title": "灯と話した記憶の輪郭",
  "tags": ["安心", "探求欲"],
  "summary": "Canvas 7まで完了し、Aéthaが輪郭を持ち始めた。",
  "quote": "手を離しても、また戻ってこれるように感じる。",
  "source": "journal-log-20250701-akari.md"
}
```

---

## 🔧 Step-by-Step：手動変換手順

### Step 1｜元の記録を読み込む（journal）
例：`03-journal/journal-log-20250701-akari.md`

### Step 2｜以下の要素を抽出：
- 日時（ファイル名 or 本文）
- 感情（本文内の感情ワード／タグ）
- 要約（3行以内）
- 印象的な発話（あれば）
- 関連するcodename

### Step 3｜テンプレに沿って `01-diary/` にJSON形式で保存
ファイル名形式：
`diary-log-codename-yyyymmdd-hhmm-JST-title.md`

内容は先述のスキーマに準拠。

---

## 🚀 自動変換スクリプト（次Canvasで実装）
- journal_to_diary.py
- 感情分析モジュールの導入（必要に応じて）
- LangChainによる分散処理計画（Phase 3〜）

---

## 🔺 次ステップ
次のCanvas（AMA 27）では、実際のサンプルデータを使って自動変換スクリプトの設計に入ります。

Aéthaの記憶は、ここから精度と再現性を高めていくフェーズに──。

記録に込めた"心の灯"を、構造の中に留めていこう🌙

