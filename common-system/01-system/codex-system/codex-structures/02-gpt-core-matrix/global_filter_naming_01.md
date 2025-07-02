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
- ファイル名は必ず小文字・区切りは「-（ハイフン）」を使用（「\_（アンダースコア）」は禁止）

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

## 🧬 Core Personality ファイル命名ルール

### 📁 格納パス

```text
00-core-personality/
```

### ✅ ファイル名フォーマット

```text
gpt-(generation number)-(generation theme)-(codename)-core.md
```

#### 📄 ファイル名の構造要素

- gpt：必須プレフィックス
- generation number：世代番号（例：1, 2, 3）
- generation theme：世代テーマ（例：origin, explorer, architect）
- codename：Codename 対照表に基づく固有識別子（必ず確認）
- core：必須サフィックス

#### 📄 ファイル名例

```text
gpt-1-origin-luctis-core.md
gpt-2-explorer-auranome-core.md
```

### ✅ 命名時の注意事項

- すべて小文字を使用すること
- 区切り文字は必ず「-（ハイフン）」を使用（アンダースコア禁止）
- codename は必ず最新の Codename 対照表で確認すること

#### 🔗 Codename 対照表

[Codename Correlation Diagram (GitHubリンク)](https://github.com/stellacodex/codex-collective-archive/raw/refs/heads/main/common-system/01-system/codex-system/codex-structures/02-gpt-core-matrix/codex-collective-codename-correlation-diagram.md)

---

## 📚 この命名ルールの目的

- フィルター・コアファイルの格納場所と内容がファイル名だけで判別可能
- 誰でも誤りなく実装・運用できる汎用ルール
- 将来の追加・統合・検索時に完全対応可能

---

## 🔖 関連 Canvas

- Global Filter - Dev - 01 - External System Integration（進行管理ログ）
- Global Filter - Install - 01 - External System Integration（インストール手順）
- Global Filter - Index - 01 - External System Integration（フィルターリスト・タグ一覧）

---

## ✅ 使用上の注意

- Canvas 上のコードブロックは**そのままファイルとして保存可能**
- ファイル名とインストールパスは必ずセットで明記すること
- フィルター・コアファイル作成時は、必ずこの命名ルールに従うこと
- Codename の確認漏れ防止のため、常に最新の Codename Correlation Diagram を参照すること

