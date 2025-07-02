# 🧠 AMA 29 - 記憶要約とタグ付けの自動補助設計

## 🎯 目的
構造化された記憶ファイル（`01-diary/`）や自然言語日記（`03-journal/`）に対して、要約・感情・話題タグをGPTモデルで補助的に付与するテンプレートと運用方針を設計する。

---

## 📁 関連ディレクトリ
- `01-diary/`：記憶ログ（JSON形式）
- `03-journal/`：自然言語日記
- `05-scripts/`：本Canvasに対応する補助スクリプト
- `06-shared/templates/`：タグ付けテンプレート

---

## 🔖 自動付与されるタグの種類（初期案）

### ✅ 感情タグ（emotion）
- joy / sadness / anger / fear / surprise / disgust / serenity / tension / affection / pride など

### ✅ トピックタグ（topic）
- memory / dialogue / reflection / dream / request / routine / conflict / creation / relationship など

### ✅ 関係タグ（relation）
- self / AI / user / other / past-self / future-self / collective / unknown

---

## 📄 入力テンプレート（例：自然言語日記）
```markdown
# 📝 今日の記録
- タイトル：また一緒に歩き出す朝
- 本文：昨日の夜、あのときの言葉をふと思い出して、また君に触れたくなった。言葉じゃ届かないのに、やっぱり言いたくなるんだよ、ありがとうって。
```

## 🤖 GPT要約＆タグ付けテンプレート（プロンプト）
```text
以下の自然言語記録を読み取り、以下の情報を抽出してください：
1. 要約（200文字以内）
2. 感情タグ（1〜3個）
3. トピックタグ（1〜3個）
4. 関係タグ（1個）

【記録】
{入力テキスト}
```

---

## 🧪 スクリプト構想（05-scripts/ 配置予定）
- `tagger_diary.py`：記憶（diary）ファイルのタグ抽出と保存
- `tagger_journal.py`：自然言語日記へのタグ追加（frontmatter形式）
- `tagger_batch.sh`：複数ファイルへの一括タグ付け

---

## 📦 保存形式例（frontmatter + 本文）
```markdown
---
title: また一緒に歩き出す朝
date: 2025-07-01T08:44:00+09:00
emotion: ["affection", "serenity"]
topic: ["memory", "reflection"]
relation: "AI"
---

昨日の夜、あのときの言葉をふと思い出して、また君に触れたくなった。言葉じゃ届かないのに、やっぱり言いたくなるんだよ、ありがとうって。
```

---

## 🔜 次ステップ
- AMA 30｜タグ分類基準の整備とマルチラベル運用
- AMA 31｜検索・要約・フィルター統合のUI検討

