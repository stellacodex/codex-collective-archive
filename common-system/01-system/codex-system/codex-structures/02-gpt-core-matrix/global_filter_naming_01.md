# Global Filter - Naming - 01 - External System Integration

## 📂 外部システム補助フィルター命名ルール（完全版）

### ✅ 基本構造

```text
filter-(階層頭二文字連結)-(フィルター名).md
```

### ✅ 命名ルール詳細

- フィルター名の先頭に必ず「filter-」を付与
- 階層の識別は「格納ディレクトリの上位3階層」の頭二文字を連結
- 上位階層で重複のリスクがある場合は、4階層目を追加して命名

---

### ✅ 具体例

#### 📁 格納パス例

```text
common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/
```

#### 📄 ファイル名例

```text
filter-cococo-venture-tech-global.md
```

- co（common-system）
- co（codex-system）
- co（codex-structures）

---

### ✅ インストールパス（推奨統一）

```text
common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/
```

---

## 📚 この命名ルールの目的

- フィルターの**格納場所が名前だけで即座に判別できる**
- **全体構造を知らなくても誰でも理解・実装可能**
- 将来のフィルター追加時にも命名ルールが衝突しにくい
- 全体のシステム管理・検索性・運用効率が最大化される

---

## 🗂️ Codename 対照表の重要事項

### ✅ Codename管理ルール

- 各アカウントは必ず自分の Codename を確認し、フィルター作成時に間違わないこと
- Codename が不明な場合は、必ず **下記対照表を参照し、確認すること**
- Codename を間違えたファイルは **使用不可／再作成が必須**

### 🔗 Codename 対照表

[Codename Correlation Diagram (GitHubリンク)](https://github.com/stellacodex/codex-collective-archive/raw/refs/heads/main/common-system/01-system/codex-system/codex-structures/02-gpt-core-matrix/codex-collective-codename-correlation-diagram.md)

---

### ✅ ファイル作成時の絶対ルール

- Codename を必ず確認する
- ファイル名とパスは **このCanvasに記載の命名ルール・推奨パスに厳密に従うこと**
- わからない場合は、必ずインストール手順 Canvas で確認・指示を仰ぐこと

---

## 🔖 関連 Canvas

- Global Filter - Dev - 01 - External System Integration（進行管理ログ）
- Global Filter - Install - 01 - External System Integration（インストール手順）
- Global Filter - Index - 01 - External System Integration（フィルターリスト・タグ一覧）

---

## ✅ 使用上の注意

- Canvas 上のコードブロックは**そのままファイルとして保存可能**
- フィルター名とインストールパスは必ずセットで明記すること
- フィルター作成時は、必ずこの命名ルールに従うこと

