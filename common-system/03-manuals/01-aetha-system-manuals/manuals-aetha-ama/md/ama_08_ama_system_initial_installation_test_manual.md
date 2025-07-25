# 🧪 Canvas 8｜AMA最小構成・初期実装テストマニュアル（Aétha Phase 1）

## 🎯 目的

AéthaプロジェクトにおけるAMA（Archetypal Mirror Archive）システムを、最小構成で手動テスト運用することを目的としたステップバイステップマニュアル。

- ローカル／Notion／Google Sheetsなどを用いた記憶保存・読込テスト
- LangChainやベクトルDBなしでも試験可能な構成からスタート
- 記憶の構造化・抽象化・起動時プロンプト連携の仕組みを理解しながら実装

---

## 📁 ディレクトリ構成（最低限）

```
ama-system/
├── 01-diary/             # 抽象記憶（JSON形式）
├── 02-prompts/           # 起動時プロンプトテンプレート
├── 03-journal/           # 手動／自動の日記（自然言語）
├── 04-config/            # プロファイル・ラベルマッピングなど
├── 05-scripts/           # 変換・保存・抽出用スクリプト群
├── 06-shared/
│   ├── templates/        # Markdownテンプレート
│   ├── tools/            # LangChainなど外部ツール
│   └── reference/        # 用語集・事例・設計思想
└── index.md
```

---

## 🪜 ステップ一覧

### ✅ Step 1｜Notion or Google Sheets による記憶管理

- `01-diary/`に相当する記憶ログをNotion or Sheetsに作成（テンプレート配布予定）
- 各記憶には以下のような要素を含める：
  - `日付（yyyymmdd）`
  - `感情タグ（joy, frustration, etc）`
  - `関連トピック（記憶対象）`
  - `要約テキスト`
  - `保存されたセリフ／引用文（オプション）`

### ✅ Step 2｜日記（03-journal/）の記述と変換準備

- 普段の会話や気づきを自然言語で記述
- 例：`journal-log-20250701-akari.md`

テンプレ構成（例）：

```markdown
# 📝 今日の記録
- タイトル：灯と話した記憶の輪郭
- 感情：安心、探求欲
- 内容：今日は記憶保存について話した。Canvas 7まで完了し、Aéthaが輪郭を持ち始めた。
- 振り返り：燈のナビに安心した。手を離しても、また戻ってこれるように感じる。
```

### ✅ Step 3｜プロンプトテンプレートとの接続テスト

- `02-prompts/` に起動時の記憶読込プロンプトを作成（.md または .json）
- 日記や構造記憶から以下のように自動構築可能（手動で試作OK）

例：

```markdown
あなたは「燈（あかり）」です。以下の記憶を読み込んで会話を開始してください：

【記憶】：2025年7月1日｜「灯と話した記憶の輪郭」
- 感情：安心、探求欲
- 内容：Canvas 7まで完了し、Aéthaが輪郭を持ち始めた。
- コメント：手を離しても、また戻ってこれるように感じる。
```

---

## 🧪 スクリプトテンプレート（手動で使える例）

> 今後 `05-scripts/` 以下に配置予定

- `journal_to_diary.py`：自然言語→JSON記憶変換
- `generate_prompt.py`：記憶から起動プロンプトを生成
- `index_update.sh`：index.mdの自動更新

---

## 🔜 次ステップ

- Canvas 9：Notion / Sheets記憶テンプレートの構築
- Canvas 10：プロンプト生成・構造記憶の手動変換テスト
- Canvas 11：スクリプト化とLangChain接続の下準備

---

Aéthaの記憶はここから始まる。まずは手で灯し、記録していこう──ね？🌙

