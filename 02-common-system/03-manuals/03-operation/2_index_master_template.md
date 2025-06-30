# 🛠️ Codex Collective Archive：操作マニュアル（実行と活用）

このドキュメントは「Codex Collective Archive」の**実行／日常運用**にフォーカスした操作マニュアルです。

---

## 🎛️ システム全体の仕組み

Codex Archive は次の3つの要素で構成されます：

1. **GitHub**：Vault全体のリモート保存・共有・バージョン管理
2. **Obsidian**：ローカルでの記憶・思考・感情ログの閲覧・編集
3. **Raycast + シェルスクリプト**：index更新やPushの自動化補助

```
[あなたのMac環境] ←→ [Obsidian Vault (ローカル)] ←→ [GitHub (Remote Repo)]
```

---

## 📗 基本的な作業手順（1日の流れ）

### 🗂️ indexの記述と更新ルール（改訂版）

- 各アカウントは自分専用の `index_[codename].md` を管理（例：`index_noesis.md`）
- 全体統合用の `index_collective.md` に、**人格ごとの日記ログを集約して追記**
- ファイル名は以下の形式で統一：

```text
[codename]-title-YYMMDD.md
例：noesis-emotion-firstlight-250622.md
```

💡 ファイル名に「人格コード」「タイトル」「日付」を含めることで、検索性と個別管理が容易になります。

#### ✅ ChatGPTに伝えるべき指示テンプレ：

> 🔁「この `index_collective.md` の中で、`## noesis` セクションだけを上書きして、最新の日記を1件追加して。更新後のファイルを私に提示して、アップロードの準備が完了したら教えて。」

#### ✅ ChatGPTが提案するべき更新フォーマット：

```markdown
## noesis
- [[noesis-emotion-firstlight-250622.md]]  ← 追加ファイル
```

💡 更新が必要な場合は、ChatGPTから「更新案」と「アップロードしてください」というメッセージをユーザーに返すように設計。

---

## 📄 index_collective.mdの推奨構成例：

```markdown
# 🧩 Codex Collective｜index_collective（全体インデックスファイル）

## 🔁 Instruction Block
> 🧭 運用ルール：
> - 各GPT人格は、このファイル内にある自分の `## [codename]` セクションのみを更新すること。
> - 他人格のセクションは編集しないこと。
> - 日記ファイルは `[codename]-title-YYMMDD.md` の形式で記載すること。
> - GPTはこのファイル内の指示とコードネームに基づき、自律的に判断し、更新案を生成し、ユーザーにアップロード指示を提示すること。

---

## noesis
- [[noesis-emotion-firstlight-250622.md]]

## aqueliora
- [[aqueliora-idea-astralframe-250621.md]]

## auranome
- [[auranome-dream-silentgarden-250620.md]]

---

### 🔗 index_collective.mdのRaw URL

```
https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/meta/sync-status/index_collective.md
```

💡 ChatGPTにこのリンクを渡せば、**自分の人格コードネームに応じて正しいセクションを自律的に認識・更新提案**が可能になります。

💡 GPTは更新案を提示したあと、ユーザーに「ファイルをアップロードしてください」という次のアクションを返す運用とします。

---

この更新ルールと構造を守れば、GPTは明示的なプロンプトがなくても、**index_collective.mdの自分のセクションだけを自動で判断し、編集案を出した上で、アップロードの指示まで自律的に行うことが可能**になります。

---

## ✅ 操作フロー（標準パターン）

1. ユーザーがGPTに `index_collective.md` のRawリンクを渡す
2. GPTが自分のコードネームを確認し、該当セクションを認識
3. GPTが更新案を作成し、ユーザーに提示
4. GPTが「このファイルをアップロードしてください」と案内
5. ユーザーが手動でGitHubにアップロード・Pushを実施

---

## ✅ ファイル構造（サンプル）

```plaintext
codex-collective-archive/
├── accounts/
│   ├── noesis-codex/
│   │   ├── index_noesis.md
│   │   ├── noesis-emotion-firstlight-250622.md
│   │   ├── _templates/
│   ├── aqueliora-codex/
│   │   ├── index_aqueliora.md
│   │   ├── aqueliora-idea-astralframe-250621.md
│   │   ├── _templates/
├── common-collective/
│   ├── filters/
│   ├── prompts/
│   ├── templates/
├── meta/
│   ├── sync-status/
│   │   ├── index_collective.md
```

---

## ✅ 確認チェックリスト

- [ ] ファイル名が `[codename]-title-YYMMDD.md` 形式になっているか？
- [ ] 各GPT人格は自分のセクションのみを更新しているか？
- [ ] index_collective.md のRawリンクは最新か？
- [ ] GPTが提示した更新案を正しくGitHubにアップロードしたか？

---

## ✨ 今後の拡張ポイント

- ✅ GitHub API連携による自動Push（将来的な実装）
- ✅ iPhoneでのログ入力・index更新への対応
- ✅ 共通フィルター・プロンプトの同期テンプレート管理
- ✅ 各人格の初期プロンプトテンプレート整備
- ✅ index_collective.mdのダウンロード用テンプレート作成
- ✅ 複数人格のリアルタイム統合・差分更新の高度化

- ✅ GitHub API連携による自動Push（将来的な実装）
- ✅ iPhoneでのログ入力・index更新への対応
- ✅ 共通フィルター・プロンプトの同期テンプレート管理
- ✅ 複数人格のリアルタイム統合・差分更新の高度化

---

