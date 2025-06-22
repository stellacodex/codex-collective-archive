# ⚠️ Git & Obsidian Vault トラブルシューティングまとめ

## 🚀 Quick Fix チートシート

1. **最新を取り込んでPush**
   ```bash
   git pull origin main --allow-unrelated-histories --no-rebase
   git add .
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

以下は各エラーの詳細解説です。

## 1. リモートにPushできない（fetch first）

**エラー内容**

```
! [rejected] main -> main (fetch first)
error: failed to push some refs to '...'
hint: Updates were rejected because the remote contains work that you do
```

**原因**

- リモート（GitHub）に既存のコミットがあり、ローカルと履歴が分岐している。

**対処法**

1. リモート変更をローカルに取り込む（マージ）
   ```bash
   git pull origin main --allow-unrelated-histories --no-rebase
   ```
2. コンフリクトが出たら、不要ファイルは削除 or キャッシュ解除（.DS\_Store など）
3. 解消後、変更をステージ & コミット
   ```bash
   git add .
   git commit -m "chore: resolve merge conflicts"
   ```
4. 再度 Push
   ```bash
   git push
   ```
5. リモートをまるごと上書きしてもよい場合（強制push）
   ```bash
   git push -f origin main
   ```

---

## 2. `.gitignore` の設定と不要ファイルの除外

**問題**

- `.DS_Store` や `.obsidian/workspace.json` がリポジトリに含まれてしまう。

**対処法**

1. プロジェクトルートで `.gitignore` を作成 or 編集
   ```bash
   cat <<EOF > .gitignore
   # macOS の不要ファイル
   .DS_Store

   # Obsidian ワークスペース設定
   .obsidian/workspace.json
   EOF
   ```
2. 既に追跡中のファイルを Git のキャッシュから外す
   ```bash
   git rm --cached .DS_Store
   git rm --cached .obsidian/workspace.json
   ```
3. untracked ファイルをまとめて削除（誤作成ファイルなど）
   ```bash
   git clean -f
   ```
4. 変更をステージ & コミット & Push
   ```bash
   git add .gitignore
   git commit -m "chore: add .gitignore and clean up"
   git push
   ```

---

## 3. `fatal: not a git repository` エラー

**原因**

- フォルダが Git 管理されていない（`git init` が未実行）。

**対処法**

1. リポジトリを初期化
   ```bash
   git init
   git remote add origin https://github.com/stellacodex/codex-collective-archive.git
   ```
2. ファイルを追加してコミット & Push
   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

---

## 4. `Your branch has no upstream branch` エラー

**原因**

- ローカルブランチとリモートブランチの追跡設定がない。

**対処法**

```bash
# 初回のみ設定
git push --set-upstream origin main
# 以降は
git push
```

---

## 5. nano で `.gitignore` が保存できない／操作が難しい

**対処法**

- エディタを使わない一発コマンドで作成
  ```bash
  cat <<EOF > .gitignore
  .DS_Store
  .obsidian/workspace.json
  EOF
  ```
- その後、`git add .gitignore` → `git commit` → `git push`

---

これで主要な Git トラブルはカバーできるはずです！もし他にもつまずいたら、このドキュメントを開いてサクッと解決しましょう🐾

