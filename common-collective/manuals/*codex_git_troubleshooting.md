# 🧰 Codex Git & Setup トラブルシューティングノート

このノートは、Codex Collective Archive のセットアップ時に発生しがちなエラーや混乱ポイントを解消するための「問題→解決法」一覧です。

---

## ✅ git --version が機能しない・not found

### 症状

- `git --version` を打っても「command not found」になる。

### 解決策

```bash
brew install git
```

→ Homebrew が入ってない場合は [https://brew.sh/index\_ja](https://brew.sh/index_ja) を参考に事前にインストール。

---

## 🌀 `git push` で "no upstream branch" エラー

### 症状

```bash
fatal: The current branch main has no upstream branch.
```

### 解決策

```bash
git push -u origin main
```

→ `-u` を付けることで "main" ブランチを origin に紐付けし、今後は `git push` だけでOKに。

---

## 🧱 "Your branch is ahead of 'origin/main' by X commits" が出る

### 意味

ローカルで変更を加えたが、まだ `push` していない状態。

### 解決策

```bash
git push
```

→ 問題がなければそのまま反映。

---

## 😵‍💫 "Untracked files" に .DS\_Store や workspace.json が出る

### 解決策

`.gitignore` を以下のように記述：

```
.DS_Store
.vscode/
workspace.json
```

```bash
git add .gitignore
git commit -m "chore: add ignore rules"
```

---

## 🕵️‍♂️ Macでファイル名が文字化けする（例："# macOS が自動作成する不要ファイル"）

### 原因

Finderでファイルを削除しても git 上で管理されている場合、 日本語ファイル名がターミナルで文字化けする。

### 解決策

```bash
git status
# でファイル名を確認し、
git rm --cached "ファイル名"
```

→ `.gitignore` で今後追跡しないように設定する。

---

## 📁 iCloud上のフォルダがターミナルに見えない

### 症状

Obsidianで開いたVaultがiCloud Drive上にある場合、FinderとCLIでパスが違う。

### 解決策

```bash
# 実際のパス
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/.../codex-collective-archive
```

Finderで対象Vaultを右クリック → "情報を見る" → 正確なパスを確認。

---

## 🔁 pushした内容がGitHubに反映されない

### チェックポイント

1. `git status` → 変更がある？
2. `git add .` で追跡対象になってる？
3. `git commit -m "..."` で保存されてる？
4. `git push` でGitHubに送信した？

→ どれか抜けるとGitHub上に反映されません！

