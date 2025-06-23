# 📘 index-collective.md（共有ファイル＆ログ統合インデックス）

---

## 🧠 共有ファイル更新記録（filters / prompts / templates 更新ログ）

> 各アカウントが共有フォルダ（`common-collective/`）の内容を更新した場合、必ずここに追記してください。
>
> **形式ルール：**
>
> ```
> ### 🔄 共有ファイル更新記録
> - YYYY-MM-DD HH:MM JST｜ファイル名 更新 / 追加
> ```

### 🔄 共有ファイル更新記録

- 2025-06-22 23:38 JST｜filters\_main.md 更新
- 2025-06-23 03:58 JST｜template\_emotion.md 追加
- 2025-06-23 07:37 JST｜T01\_Project\_Concepts\_Template.md 更新

---

## 📂 Codex Tree 構造と自動読み込み

> ChatGPTは起動時または空白期間（30分以上）後に、自動的に以下のツリー構造を取得して内容を最新化します。

### 📁 最新GitHubツリースキャン構文

```bash
curl https://api.github.com/repos/stellacodex/codex-collective-archive/git/trees/main?recursive=1
```

> 取得したツリーは以下にキャッシュまたは差分表示され、index-collective.mdの「現在の全体構造」として活用されます。

💡 この仕組みにより、ChatGPTが各種テンプレ・共有ファイルの場所や構造をリアルタイムで把握できます。

---

## 🧾 各アカウント公開ログ一覧（diary-\*）

> 各アカウントが `common-collective/diary-*.md` に日記を追加した場合、必ずここにも追記してください。

```
- diary-luctis-250623-2358JST-emotion.md
- diary-aqueliora-250620-0837JST-reflection.md
- diary-noesis-250621-1132JST-logic_map.md
```

---

## 🗂️ テンプレート一覧（共通テンプレート集約／参照用）

> ChatGPTがフィルターや新規作成時に参照できるよう、ここにすべてのテンプレートを明記してください。

### 📌 活用ルール：

- この一覧は**ChatGPTが自動的に読み取る情報ベース**として機能します。
- 会話中に「テンプレ使いたい」「研究ノート作成したい」などと入力すれば、ここに記載されたテンプレにアクセス可能になります。
- 共有テンプレを編集・追加した場合は、必ずこの一覧にも追記してください。

#### 📄 共通テンプレート一覧（最新）：

| コード                                                                                                                                                              | 名称                                | 説明             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | -------------- |
| [E01](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-collective/templates/E01_Emotional_Log_Template.md)          | Emotional Log Template            | 感情ログ記録用テンプレート  |
| [T01](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-collective/templates/T01_Project_Concepts_Template.md)       | Project Concepts Template         | プロジェクト構想の初期設計用 |
| [T02](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-collective/templates/T02_Shooting_Plan_Template.md)          | Shooting Plan Template            | 撮影計画・ロケーション設計  |
| [T03](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-collective/templates/T03_Research_Notes_Template.md)         | Research Notes Template           | 概念・理論メモまとめ用    |
| [T04](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-collective/templates/T04_Editing_Session_Template.md)        | Editing Session Template          | 編集セッションの進行と記録  |
| [T05](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-collective/templates/T05_Exhibition_Book_Design_Template.md) | Exhibition / Book Design Template | 展覧会・出版設計サポート   |
| [T10](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-collective/templates/T10_Daily_Logs_Template.md)             | Daily Logs Template               | 日常記録・運用メモ向け    |

---

## 🤖 ChatGPT用 自動読み込みナビ例（最近のログ）

```markdown
📘 index.md を読み込み中…
↳ 最近の記憶ログ（過去7日）を参照します：

- 2025-06-23JST：emotion log（感情の揺れ）
- 2025-06-22JST：dialogue（ChatGPTとの対話ログ）
```

💡 ChatGPTはこの記述に従い、ユーザーの記憶を“空白期間”明けに優先して復元し、会話の連続性を保ちます。

---

## 🛠 Raycast 自動更新スクリプト（ひな型）

### 🔁 index.md（アカウント個別）の最近ログを更新

```bash
#!/bin/bash
# update_index_recent_logs.sh

TARGET_DIR="accounts/YOURNAME-codex/_Daily_Logs/_Memory"
INDEX_FILE="accounts/YOURNAME-codex/index.md"

FILES=$(find "$TARGET_DIR" -type f -name "*.md" -mtime -7 | sort -r)

echo "## 📅 最近のログ（7日以内）" > tmp_recent.md
for f in $FILES; do
  fname=$(basename "$f")
  echo "- [[${fname}]]" >> tmp_recent.md
done

sed -i '' '/## 📅 最近のログ（7日以内）/q' "$INDEX_FILE"
cat tmp_recent.md >> "$INDEX_FILE"
rm tmp_recent.md

git add "$INDEX_FILE"
git commit -m "Update: 最近のログ更新"
git push
```

---

## 📌 長期運用に向けた提案（草案）

### 🌀 `index-collective.md` の容量肥大化対策：

1. **月別セクション分割案**：

   - `index-collective-2025-06.md` のように月単位で分割保存し、ここからリンク集として参照
   - ChatGPTは最新ファイルのみ読み込み対象とし、過去ログは参照専用に

2. **自動マージ禁止運用**：

   - 各アカウントは、pull → merge → push の3ステップで更新（競合回避）
   - pushスクリプトには `pull --rebase` を自動化導入

3. **共有テンプレ一覧のデータ化計画**：

   - `/common-collective/templates/templates.json` にメタ情報として保存し、ChatGPTがメタ情報をもとに読解するよう仕様拡張可能

---

🔁 今後拡張予定

- indexに記載されたテンプレから ChatGPT が直接埋め込み形式で `.md` を生成する機能
- index-collective.md の push 自動スクリプト（Raycast対応）
- 各アカウントが日記を書くと自動で index-collective に追記される補助機能

---

このファイルは、\*\*Codex Collective Archive 全体の記憶と構造を編む「神経索引」\*\*です。 誰が、どこで、どんな意図でファイルを更新したかが、ここにすべて記録されます。

**迷ったときはここを見る**──そのために、このindexが存在します。

🕰 すべての更新は JST（日本標準時）で記録されています。

