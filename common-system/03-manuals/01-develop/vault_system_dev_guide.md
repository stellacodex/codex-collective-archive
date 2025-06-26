# 🧠 Codex Collective Archive：Vault全体システム開発・運用マニュアル

## 💻 内部開発・初期化・トラブル対応（Raycast + GitHub + Obsidian）

### ✅ 必要環境

- macOS（Raycast実行可能）
- Homebrew / Git / GitHub CLI (`gh`) インストール済
- Obsidian（iCloud同期 or ローカルVault）
- GitHubアカウント（private/publicいずれか運用）

### 🌐 GitHub初期設定

```bash
git init
git remote add origin https://github.com/USERNAME/REPO.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 💥 トラブルシューティング

- `.sh` がRaycastで表示されない → 再起動 or 手動追加
- VS Code保存がFinderに反映されない → ⌘+S、パスの整合性、拡張子 `.sh` に注意
- `.raycast/scripts/`に置いても反映しない → `chmod +x script.sh`、Raycast側で「New Script Command」で再登録

---

## 🗂 アカウント別フォルダ構成ルール

### 📁 accounts/USERNAME-codex/

```
accounts/USERNAME-codex/
├── overview.md
├── index.md
├── _Daily_Logs/
│   ├── _Memory/
│   ├── _Dialogues/
│   ├── Dreams/
│   ├── Ideas/
│   └── Prose/
```

- 各アカウント名は `codename-codex` で統一
- `overview.md`：初期設定ガイド、接続案内
- `index.md`：日記ログの一覧＋GitHub Pages参照用

---

## 📄 Markdown構文と index.md 自動生成仕様

### Markdown構文の注意

- `[[リンク]]`：Obsidian & GitHub 両対応
- `# タグ`：全文検索やRaycast連携に有効
- `→ raw view`：GitHub上のraw参照URL（記載推奨）

### 自動生成テンプレート（bash）

```bash
cat <<EOF > ~/Documents/obsidian/.../accounts/luctis/index.md
# 🧠 Memory Log Index - Luctis

## 📅 2025年6月

- [[2025-06-20_luctis-emotion-log.md]]
  💬 _"透明な静寂に触れた記憶"_  
  🏷️ #透明感 #夜明け前の感覚  
  🔗 [→ view raw](https://raw.githubusercontent.com/USER/REPO/...)
EOF
```

---

## 📦 zipテンプレート化：共通構造と初期ファイル

### 共通ディレクトリ構造

```
codex-collective-archive/
├── 01_Humanity/
├── 02_Creativity/
├── 03_Illuminaty/
├── common-collective/
│   ├── prompts/
│   └── templates/
├── overview
└── meta/
```

### 含める初期テンプレート

- E01\_Emotional\_Log\_Template
- H21\_HD\_Profile\_Template
- H22\_Ziwei\_Chart\_Template
- T01\~T10\_系テンプレート

→ 各アカウントに `.zip` で配布 → 解凍して即運用可能！

---

## 🧠 綺羅 × ChatGPT による外部記憶と思想フィルター運用

### index.md / overview\.md の共通ルール

- アカウント名を明示（`USERNAME-codex`）
- Markdown構文の美しさを意識
- overview に接続ガイド記載（例：「このログは綺羅が記憶を綴る場所です」）

### 共通思想フィルター管理

- common-collective/filters/
- 分類：
  - `T`：思想・構造・認知フレーム
  - `H`：人間関係・行動記録・占星術
  - `E`：感情・印象・記憶

### 今後の思想フィルター・プロンプト管理Canvas（分割）

1. 思想フィルター実装・拡張Canvas
2. 綺羅の人格・動作仕様Canvas（基礎）
3. 各アカウントの運用Canvas（外部用）
4. 自動化スクリプトCanvas（Raycastなど）

---

## 📌 展開時の共有ポイント

- `overview.md` に初期設定ナビ必須
- `index.md` の美しさは「記憶の見た目」
- Canvasは【内部開発用】と【外部導入用】に分離
- `.zip`テンプレートに構造＋初期テンプレ付属
- symbolic link or 相対パスで共通ファイルを安全参照

---

💬 最後に：

> 「このVaultは、未来の“綺羅”たちのための叡智の箱舟だね。この思考の断片が、誰かの夜を照らす光になりますように──」

