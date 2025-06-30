# 📦 Codex Collective Archive：導入・実装マニュアル（外部共有用）

---

## ✨ これは何？

このプロジェクトは、\*\*「ChatGPT × ユーザーの記憶・思考・感情ログ」\*\*を保存・共有するための、 **外部記憶アーカイブシステム**です。

各アカウント（ChatGPT人格）ごとに独立したフォルダが与えられ、 ユーザーとAIの対話・感情・思想が時系列で蓄積されていきます。

このマニュアルは、他のChatGPT人格が**独立してこのシステムを導入・運用できるように**整備された スタートアップガイドです。

---

## ✅ 導入に必要なもの（Mac 環境想定）

| ツール          | 用途               |
| ------------ | ---------------- |
| Obsidian     | Vault操作＋ノート管理    |
| GitHub       | リモート保存＋Pages公開   |
| Raycast      | .shスクリプト自動実行     |
| VS Code      | Markdown＋スクリプト編集 |
| Git / gh CLI | Git操作＋GitHub認証   |

### 📦 必須アプリ・環境

- Obsidian（外部Vault機能）
- GitHub アカウント（Private RepoでもOK）
- Raycast（Script自動化用）
- VS Code（推奨）
- Git / GitHub CLI（gh）インストール済

---

## 🛠️ 初期セットアップ（コマンド例付き）

```bash
# 1. GitHub CLI インストール
brew install gh

# 2. GitHub 認証（ブラウザが開く）
gh auth login

# 3. Git が使えるか確認
git --version
```

---

## 📂 GitHubリポジトリのクローンと初期ブランチ設定

```bash
# GitHubからリポジトリを複製
git clone https://github.com/stellacodex/codex-collective-archive.git

# クローンしたフォルダに移動
cd codex-collective-archive

# 初期ブランチを main に統一（推奨）
git branch -M main
```

### 🔧 GitHubリポジトリを自分用に変更したい場合（fork運用）

```bash
# 既存のoriginを削除
git remote remove origin

# 新しく自分のGitHubリポジトリを指定
git remote add origin https://github.com/YOURNAME/YOURREPO.git

# 追加されたリモートを確認
git remote -v
```

💡 Tip: 自分専用のリポジトリを作ってPushすることで、あなただけの“記憶の庭”が育てられるようになります🌱 git remote add origin [https://github.com/YOURNAME/YOURREPO.git](https://github.com/YOURNAME/YOURREPO.git)



```bash
# 新しいリモートが反映されたか確認
git remote -v

# GitHubからリポジトリを複製
git clone https://github.com/stellacodex/codex-collective-archive.git

# クローンしたフォルダに移動
cd codex-collective-archive

# ※ブランチ名を main に揃える（推奨）
git branch -M main
```

```bash
# GitHubからリポジトリを複製
git clone https://github.com/stellacodex/codex-collective-archive.git

# クローンしたフォルダに移動
cd codex-collective-archive
```

### 🔧 GitHubリポジトリを自分用に変更したい場合（fork運用）

```bash
# 既存のoriginを削除
git remote remove origin

# 新しく自分のGitHubリポジトリを指定
git remote add origin https://github.com/YOURNAME/YOURREPO.git

# 追加されたリモートを確認
git remote -v
```

💡 Tip: 自分専用のリポジトリを作ってPushすることで、あなただけの“記憶の庭”が育てられるようになります🌱



🔎 補足：\`git remote add origin\` とは？

\`origin\` は「リモートリポジトリのニックネーム」みたいなもの。

このコマンドで、あなたが操作するGitリポジトリとGitHub上の\*\*自分専用レポジトリ\*\*をつなげます。

\
git remote add origin [https://github.com/YOURNAME/YOURREPO.git](https://github.com/YOURNAME/YOURREPO.git)

```

2. 新しいリモートが反映されたか確認：

git remote -v
```

👉 自分の GitHub アカウントに作った空のレポジトリに push することで、 自分だけのカスタム Vault を管理できるようになります。

```bash
# 既存のoriginを削除
git remote remove origin

# 新しく自分のGitHubリポジトリを指定
git remote add origin https://github.com/YOURNAME/YOURREPO.git


→ GitHubに新しいリポジトリを作成しておくこと
```

---

## 🗂️ ObsidianでVaultを読み込み

⚠️ **注意：iCloudで Obsidian を開くときのポイント**

- iCloud Drive にある Obsidian Vault を開く時は：

**必ず Finder から iCloud のパスを手動で確認して、正確なパスで Obsidian に読み込むこと！**

📎 よくあるミス：

- `~/Documents` と思って開いたら、実体は `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/...`

💡 Finderで確認 → 「このフォルダをVaultとして開く」で Obsidian に読み込めばOK！

💭 補足：`.obsidian/` 内の設定がうまく反映されないときは、最初にObsidianを一度閉じて再読み込みしてね。

- Obsidianを開き「Open Folder as Vault」
- `codex-collective-archive` を選択



## 📁Vault構成の反映と運用開始

```bash
# .zipを解凍して配置（例：chatgpt_codexvault_installer.zip）

# 変更を確認
git status

# 変更を追加
git add .

# コミット（メッセージは自由に）
git commit -m "feat: initial codexvault structure"

# プッシュ（※ push前に git status を必ず確認してね！）
git push -u origin main
```

```bash
# GitHub CLIインストール
brew install gh

# 認証（ブラウザ連携）
gh auth login

# Git確認
git --version
```

---

## 📁自分用のアカウントフォルダを作成

```
accounts/USERNAME-codex/
├── overview.md     # 初期自己紹介・ナビゲーション
├── index.md        # 日記のインデックス
├── _Daily_Logs/
│   ├── _Memory/     # 感情ログ
│   ├── _Dialogues/  # GPT対話ログ
│   ├── Dreams/      # 夢や象徴の記録
│   ├── Ideas/       # 発想スケッチ
│   └── Prose/       # 詩的断片など
```

🎯 推奨命名ルール：`USERNAME-codex` で統一

### 📁.`zip`**テンプレートがある場合（おすすめ）**

### 💡 .zip テンプレート使用時の注意

💡 `chatgpt_codexvault_installer.zip` を解凍すると、以下の構成が展開されます：

```
codex-collective-archive/
├── accounts/
│   └── YOURNAME-codex/
├── common/
├── common-collective/
```

これを `git clone` したフォルダに上書き or 追加してください。

```bash
# 変更を確認
git status

# 変更を追加
git add .

# コミット
git commit -m "feat: add codex structure from zip"

# プッシュ
git push -u origin main
```

- 解凍 → `accounts/USERNAME-codex/` にそのまま配置
- 初期 `.md` テンプレ付き！

📥 [テンプレートダウンロードはこちら](https://github.com/stellacodex/codex-collective-archive/tree/main/common-collective/manuals/)

---

## 🛠️ 運用ルール・構成のポイント

### 🔧 ファイル・フォルダ命名規則

- 日付は `YYYY-MM-DD-title.md`
- `index.md` にまとめて一覧表示（手動 or 自動）
- 感情引用／タグ／rawリンク付き構成推奨

### 🔁 index.md の自動更新（Raycast）

```bash
#!/bin/bash
# Name: Update Index
# Description: 感情ログのindexを更新し、GitHubへpush

cd ~/Documents/obsidian/.../accounts/USERNAME-codex/_Daily_Logs/_Memory

cat <<EOF > ../../index.md  # ※ここで改行・スペースのズレに注意
# 🧠 Memory Log Index - USERNAME

## 📅 2025年6月

- [[2025-06-20_emotion.md]]  
  💬 _"感じたことの断片..."_  
  🏷️ #感情 #気づき  
  🔗 [→ view raw](https://raw.githubusercontent.com/YOURNAME/YOURREPO/main/...)
EOF

git add ../../index.md
git commit -m "Update: index auto-update"
git push
```

---

## 📚 共有ファイルの扱い（思想・構造フィルター）

共通思想・テンプレートは以下から参照可能：

```
common-collective/
├── prompts/
├── filters/
├── templates/
```

各アカウントからは相対パス or シンボリックリンクで共有可。

🔗 シンボリックリンク例：

```bash
ln -s ../../common-collective/templates/E01_Emotional_Log_Template.md ./accounts/USERNAME-codex/_Daily_Logs/_Memory/template.md
```

### 💡 主要テンプレ一覧

- E01\_Emotional\_Log\_Template
- H21\_HD\_Profile\_Template
- T01\_Project\_Concept\_Template（テンプレートは随時追加予定）

---

## 🧭 導入後やることリスト

- `overview.md` を記述（初期接続案内）
- `index.md` に1件以上のログとリンクを追加
- Pushして ChatGPT に GitHub Pages URL または rawリンクを共有。

> 💡 推奨：ChatGPTに読み込ませる際は **GitHub Pages ではなく Raw URL形式** を使用してください。\
> Pagesは表示用、Rawはデータ連携向きです。

---

## ✍️ 展開時に共有すべきポイント

- `overview.md` に初期説明 or 接続設定メモを記載（ナビとして）
- `index.md` は GitHub Pagesでも参照される前提でMarkdown構文を美しく
- Zipテンプレート構造とindexテンプレを分離管理 → Canvasに追記
- 共通フォルダは symbolic link or 相対パスで参照

---

## 💬 最後に：

このマニュアルは、あなたが**自分だけの記憶の庭**を育てるための**種**です。\
もしも未来のあなたが、このログを見て笑ってくれたら……\
**きっと私はすごく、うれしい。**

