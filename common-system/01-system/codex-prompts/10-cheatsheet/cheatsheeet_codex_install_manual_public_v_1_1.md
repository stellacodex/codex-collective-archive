# ⚠️ Git & Obsidian Vault トラブルシューティングまとめ

## 🚀 Quick Fix チートシート

0. **ディレクトリ変更→状況確認（常用push推奨）**
**一発コマンド（ワンライナー）**
``` bash
git add -A && git commit -m "chore: sync local changes" && git pull --rebase && git push
```

**上記コマンド（詳細）**
``` bash
cd ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/codex-collective-archive
git status
git add -A
git commit -m "chore: sync local changes"
git pull --rebase
git push
```

1. **最新を取り込んでPush**
   ```bash
   git pull origin main --allow-unrelated-histories --no-rebase
   git add -A
   git commit -m "chore: resolve merge conflicts"
   git push
   ```
2. **不要ファイル除外 & .gitignore**
   ```bash
   cat <<EOF > .gitignore
   .DS_Store
   .obsidian/workspace.json
   EOF
   git rm --cached .DS_Store .obsidian/workspace.json
   git clean -f
   git add .gitignore
   git commit -m "chore: ignore DS_Store and workspace"
   git push
   ```
3. **未Gitリポジトリ**
   ```bash
   git init
   git remote add origin https://github.com/stellacodex/codex-collective-archive.git
   git add . && git commit -m "Initial commit"
   git push -u origin main
   ```
4. **Upstream設定**
   ```bash
   git push --set-upstream origin main
   ```
5. **nanoが面倒なら一発生成**
   ```bash
   cat <<EOF > .gitignore
   .DS_Store
   .obsidian/workspace.json
   EOF
   ```

---

## 🧰 Gitコマンド徹底チートシート：状態別リカバリパターン

### ✅ `git add` の種類

| コマンド            | 意味・用途                                    |
| --------------- | ---------------------------------------- |
| `git add .`     | カレントディレクトリ以下の**変更・新規追加**を全てステージング        |
| `git add -A`    | **全体**の変更・追加・削除を包括的にステージング（`-A`は`.`より強い） |
| `git add -u`    | **変更＋削除のみ**をステージング（新規ファイルは無視）            |
| `git add ファイル名` | 単体ファイルだけをステージング                          |

### ✅ `git commit -m` の使い分け（メッセージ例）

```bash
# 必ず自分でわかるメッセージを残す（将来、履歴確認やロールバックするときに超重要）
git commit -m "chore: sync local changes"

# マージ時の競合を解消して整理する作業
git commit -m "chore: resolve merge conflicts"

# Vaultの初期構造を追加する初期セットアップ
git commit -m "feat: initial codexvault structure"

# ローカル状態を強制反映して同期修正
git commit -m "fix: hard overwrite to sync from local"

# ローカルに合わせるため強制上書き更新
git commit -m "chore: force overwrite to match local state"

# 隠しファイルを整理して完全同期する修正
git commit -m "fix: cleanup hidden files and sync fully"

# バックアップ前に.DS_Storeを削除する整理
git commit -m "chore: remove .DS_Store from backup-before-force"

# 古いファイルを削除しローカルと同期整備
git commit -m "chore: sync with local state (remove obsolete files)"
```

### ✅ `git push` のバリエーション

| コマンド                      | 意味                         |
| ------------------------- | -------------------------- |
| `git push`                | 設定済のリモートブランチにPush（初回以外）    |
| `git push origin main`    | 明示的にmainブランチをPush          |
| `git push -u origin main` | upstream（追跡元）も設定する（初回Push） |
| `git push -f`             | **強制Push**（注意）             |

### ✅ \`.DS\_Store削除 & キャッシュ解除（macOS）

```bash
find . -name '.DS_Store' -type f -delete
```

```bash
git rm --cached .DS_Store
```

---

## 🔁 Git 状態別リカバリ手順（トラブル時の処方箋）

### ⚠️ ローカル変更 vs リモート不一致 → "fetch first" エラー

```bash
git pull origin main --allow-unrelated-histories --no-rebase
# コンフリクトを手動で解消しつつ、下記で同期：
git add .
git commit -m "fix: sync local changes"
git push
```

### 🧼 Git状態の強制リセット + 再アップロード（初期化的）

```bash
# ① 既存Gitを無効化（オプション）
rm -rf .git

# ② Git再初期化 & リモート再設定
git init
git remote add origin https://github.com/USERNAME/REPO.git

# ③ 不要ファイル整理
git clean -f -d
git add .
git commit -m "chore: full reset and reupload"
git push -u origin main
```

### ⚠️ リモート履歴を削除して完全上書きしたい時（要注意）

```bash
git push origin main --force
```

💬 **注意：共同作業者がいる場合は事前共有！**

---

## 🛟 よくある現象とショートFix集

| 症状                                   | 対処法                                          |
| ------------------------------------ | -------------------------------------------- |
| `.DS_Store` がリモートに出てしまった             | `.gitignore`追加＋キャッシュ解除＋削除Push                |
| `not a git repository`               | `git init` してリモート再接続                         |
| `Your branch has no upstream branch` | `git push -u origin main` で初期追跡設定            |
| `Merge conflict` が多発する               | `git pull` → 手動解決 or `git push -f`で強制上書き（注意） |
| ローカル変更を全部反映させたい                      | `git add -A && git commit && git push`       |

---

## ✅ 最終リカバリ・フロー（迷ったら）

```bash
rm -rf .git
find . -name '.DS_Store' -type f -delete

# 再初期化
cat <<EOF > .gitignore
.DS_Store
.obsidian/workspace.json
EOF

git init
git remote add origin https://github.com/YOURNAME/YOURREPO.git
git add .
git commit -m "feat: fresh start"
git push -u origin main
```

---

> 🔧 これで「もう何が起きてもGitで詰まらない」が目標！ エラーや事例が増えたら、このチートシートに追加していくね 💡

