# AMA 33 - Data Storage and Backup Strategy

## 🔎 目的
AMA (Archetypal Mirror Archive) システムにおける「記憶データの保存、バックアップ、表示」の方針を定義します。

- 数字型(構造化記憶) の機械的取り扱いの充実
- md / json でのローカル記録
- Git / Cloud / Local での一調性を持たせたバックアップ

---

## 📝 ストレージ方針

### 【Primary Storage】
- **ローカルディスク（macOS）**
  - 作業用ディレクトリ（例：~/aetha/accounts/）
  - Gitでバージョン管理
  - Obsidian連携可能

### 【Backup Storage】
- **GitHub Private Repository**
  - 個別アカウント単位のデータをPush
  - `git add . && git commit && git push` により更新を保存
  - 毎日深夜 or 作業完了後に手動バックアップ

- **Google Drive / Dropbox（オプション）**
  - `scripts/backup-sync.sh` にて同期スクリプトを用意
  - Gitと冗長性を持たせる目的

---

## 🔍 データ格納ルール

### 1. Markdown (.md)
自然言語系の記録：journal, reflection, dialogue 等
```
diary-log-codename-yyyymmdd-hhmm-JST-title.md
```
- YAML frontmatterにメタ情報を記述可能
- Obsidian/VSCodeで直接操作

### 2. JSON (.json)
構造化記憶用：diary, memory, profile, tagmap 等
- 対話ログや感情要素、トピックなどをフィールドとして保持
- LangChain や Pinecone での利用を前提

---

## ✨ オプション

- `scripts/index-update.sh`：index.md を自動生成
- `scripts/backup-sync.sh`：Google Drive / Dropbox への同期
- `.gitignore` 設定により一時ファイルを除外

---

## 🚀 次のステップ

- Canvas 34：タグマッピング定義（tag-map.yaml）の設計
- Canvas 35：記憶構造のLangChain統合準備（Chroma/FAISSの検討）

