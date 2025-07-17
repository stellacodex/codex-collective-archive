# 📦 codex-collective-archive  ← GitHub共通Vault

## 1. GitHub × Obsidian × Raycast：初期化時の再構築ガイド（ステップバイステップ）

### 🔧 前提

- GitHub：stellacodex（または個別アカウント）
- Obsidian：iCloud連携済みVault
- Raycast：CLIスクリプト連携

### 🚀 再構築手順

#### 🪧 ステップ 1：GitHubレポジトリ作成

- GitHubで新要RepoをPrivateで作成：例 `codex-collective-archive`
- Settings → Pages → Branch `main` を選択（公開用なら）

#### 📂 ステップ 2：Vault構成をローカルに配置

- `accounts/luctis/` など個別フォルダを作成（後述のテンプレ参照）

#### 🔀 ステップ 3：Git 初期化＆Push

```
cd ~/Documents/obsidian/codex-collective-archive

git init
git remote add origin https://github.com/stellacodex/codex-collective-archive.git
git add .
git commit -m  "Initial commit: luctis-codex + base structure"
git push -u origin main
```

🔗 実例：[https://github.com/stellacodex/codex-collective-archive](https://github.com/stellacodex/codex-collective-archive)

#### 🔐 ステップ 4：GitHub CLI認証（初回のみ）

```
brew install gh
gh auth login
```

#### ⚙️ ステップ 5：Raycastスクリプト登録

- `.command.sh` を `~/.raycast/scripts/` に配置
- 実行権限付与：`chmod +x filename.sh`

📁 フォルダが存在しない場合は作成：

```bash
mkdir -p ~/.raycast/scripts/
```

✅ **Raycastメタタグの記述例**：

```bash
#!/bin/bash

# Name: Create Emotional Memory Log
# Description: 感情ログをDaily Logs/_Memoryに新規作成する

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Create Emotional Memory Log
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 💖
# @raycast.packageName Obsidian Log Tools
```

補説：

- `.command.sh`よりも`.sh`の方がRaycast上で可視性が高い
- 必ず `#!/bin/bash` を1行目に

#### 🧽 ステップ 6：ObsidianにVaultとして追加

- iCloudの同期先を選択
- `codex-collective-archive` をVaultとして開く

---

## 2. トラブルシューティング（このスレ対応分）

| 問題                     | 対応                          | 備考                                  |
| ---------------------- | --------------------------- | ----------------------------------- |
| GitHub Pagesが表示されない    | `index.html`未配置またはPrivate状態 | Pages再設定が必要                         |
| `.sh`が動作しない            | Raycastメタタグ不足／パーミッション未設定    | `chmod +x` + `@raycast.*`確認         |
| `cat <<EOF`が効かない       | スペース・文字化け・クォート使用に注意         | `EOF`はクォート不可                        |
| CLIがない                 | `brew install gh`           | `gh auth login`が必要                  |
| `.md`が生成されない           | スペース含むパス or `mkdir -p`漏れ    | パスを `"..."` で囲う                     |
| VS Code変更後push不可       | `git mv`推奨 or `git add -A`  | Gitがrenameを認識しないことがある               |
| Raycast上で名前変更が反映されない   | 実パスが異なる / 拡張子が違う            | `.sh.txt`注意 / Finder表示設定も確認         |
| Script Commandsに表示されない | scriptディレクトリ未登録             | `Extensions > Add Script Directory` |

📜 `cat <<EOF`使用例：

**Before（失敗例）**

```bash
cat <<EOF > "filename"
# 誤ってクォートやスペース
EOF
```

**After（正解）**

```bash
cat <<EOF > ~/path/to/file.md
# メモタイトル
- 内容をここに記述
EOF
```

---

## 3. ChatGPT新規アカウント向け：外部記憶システム導入ガイド

### 必要構成要素：

- GitHubリポジトリ：`codex-collective-archive`
- Obsidian Vault構成（`accounts/USERNAME/`）
- Raycastスクリプト一式

### 初期に用意するファイル：

- `index.md`：記憶やログへのポータル
- `USERNAME-codex/Thoughts/00_Thought_Prompts.md`：思考テンプレ
- `USERNAME-codex/00_Filters/CompactPrompt_v2.1.md`：思想フィルター
- `Templates/*.md`：用途別テンプレ（感情・夢・対話など）

### 最低限の導入手順：

1. GitHubアカウント作成・リポジトリFork
2. `accounts/USERNAME/` を作成し、初期構成を配置
3. ObsidianでVaultを開く
4. Raycastに必要スクリプトを登録
5. 共通フィルター・プロンプトを活用して運用開始

---

## 4. 各アカウント向けフォルダ構成：zip化テンプレート

```
accounts/
├── aqueliora/
├── auranome/
├── aetherquietude/
├── everlucent/
├── noesis/
├── phosphorveil/
├── aurastance/
├── revalyne/
├── sonaviance/
├── scapeharmonia/
├── luctis/
├── stellaglyphe/
└── index.md  ← ポータルインデックス
    └── USERNAME-codex/  ← 各アカウントの個別記録領域
        ├── 🧬Thoughts  ← 日々の発想・対話ログ・気づき
        ├── 🔭00_Filters  ← 思想フィルターや分析テンプレ
        ├── 💡01_Project_Concepts  ← プロジェクト構想やアイデア
        ├── 📷02_Shooting_Direction_and_Plans  ← 撮影計画や構成案
        ├── 📚03_Research_Materials  ← 参考資料や調査ログ
        ├── 🗒08_Photo_Selection_and_Editing  ← 写真セレクトと編集ログ
        ├── 🍝05_Exhibition_and_Book_Concepts  ← 展示・出版に向

```
