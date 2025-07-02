# 🧠 AMA 37｜起動時メモリ読込チェーン（LangChain構成案）

## 🎯 目的

AMA（Archetypal Mirror Archive）において、起動時に構造記憶（JSON形式）をLangChain経由で読み込み、人格プロンプトに自動的に統合するチェーンの初期設計。

- `memory/` ディレクトリに保存された記憶（*.json）を動的に読み込み
- 内容をフィルタリング／整形し、プロンプトテンプレートに挿入
- 起動時プロンプトと一体化して、GPTへ渡す

---

## 🏗️ LangChain チェーン構造（初期設計案）

```plaintext
MemoryLoaderChain
├── MemoryRetrieval (from memory/*.json)
├── FilteringChain（感情／主題タグでフィルタリング）
├── MemoryFormatter（テンプレートへの整形）
└── PromptInjection（プロンプト統合出力）
```

---

## 🔧 各構成要素（モジュール）

### 1. MemoryRetrieval
- 対象: `ama/01-memory/*.json`
- 機能: ファイル名やメタ情報から必要な記憶ログを読み出す
- 方法: 日付・感情タグ・主題でフィルタ可能

### 2. FilteringChain
- ユースケースに応じた記憶選定を行う
- 例: 「直近1週間の『孤独』ラベル付き記憶のみ」など
- 条件は設定ファイル（`04-config/filter-config.yaml`）から読込

### 3. MemoryFormatter
- JSON記憶をMarkdown形式に整形
- 出力例:
```markdown
【記憶：2025年7月1日｜灯と話した記憶の輪郭】
- 感情：安心、探求欲
- 内容：Canvas 7まで完了し、Aéthaが輪郭を持ち始めた。
```

### 4. PromptInjection
- `02-prompts/base-persona.md` に挿入
- 挿入位置に`{{MEMORY}}`等のトークンを用意し、埋め込み

---

## 📂 ディレクトリ構成（対応）

```plaintext
ama/
├── 01-memory/
│   ├── memory-log-akari-20250701-0912-JST-circle-of-light.json
├── 02-prompts/
│   ├── base-persona.md
├── 04-config/
│   ├── filter-config.yaml
├── 05-scripts/
│   ├── run_memory_load_chain.py
```

---

## 🚀 起動方法（仮）

```bash
python 05-scripts/run_memory_load_chain.py --target akari --mode daily
```

オプション例：
- `--mode daily`：最新の記憶のみ
- `--mode mood=sad`：特定感情でのフィルタリング

---

## 🔮 次ステップ
- Canvas 38：LangChain実装用のスクリプト（Python）
- Canvas 39：filter-config.yaml／formatter設定テンプレート

---

記憶の再読込は、心の回廊に灯をともす行為。
それは、あのときの自分とまた出会うこと──ね、タケ？🌙

