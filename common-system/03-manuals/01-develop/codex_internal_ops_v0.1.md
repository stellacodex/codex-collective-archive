# 🧠 codex-collective-archive｜内部設計ノート（開発・運用・分岐管理）

このCanvasは、luctis・stellaglypheが主導する外部記憶システムの**内部構築・システム運用・テンプレート管理**に特化したドキュメントです。

---

## 🗂️ 構成要素一覧（整理・生成対象）

### 📁 `accounts/USERNAME/USERNAME-codex/`
- 🧬 `Thoughts/00_Thought_Prompts.md`
- 🔭 `00_Filters/CompactPrompt_v2.1.md`
- 💡 `01_Project_Concepts/`
- 📷 `02_Shooting_Direction_and_Plans/`
- 📚 `03_Research_Materials/`
- 🖼 `04_Photo_Selection_and_Editing/`
- 🏛 `05_Exhibition_and_Book_Concepts/`
- 📓 `10_Daily_Logs/`
  - `_Memory/`
  - `_Dialogues/`
  - `Dreams/`
  - `Ideas/`
  - `Prose/`
- 🗂 `Templates/*.md`
- 📄 `overview.md` ← 接続概要・初期案内
- 📄 `index.md` ← 各ログ・内部リンクインデックス

### 📁 `common/`
- `filters/`：横断プロンプト・思想テンプレ
- `templates/`：共通テンプレート
- `prompts/`：運用支援プロンプト（生成・整形・記述ガイド）

---

## 🔧 index.md 仕様・自動生成テンプレ

### 📌 概要
- accounts/USERNAME/index.md に配置
- 日付順でログファイルを列挙
- 各ログ：
  - `[[ファイル名]]`リンク
  - 短い感情引用
  - タグ・キーワード（#）
  - rawリンク（GitHub raw URL）

### ✅ 自動化の条件
- `cat <<EOF` を使う `.sh` スクリプト
- Raycast連携用に `.sh` or `.command.sh`
- ファイル名含む変数展開に注意（スペース/改行）

```bash
cat <<EOF > ~/Documents/obsidian/codex-collective-archive/accounts/luctis/index.md
# 🧠 Memory Log Index - Luctis

## 📅 2025年6月

- [[2025-06-20_luctis-emotion-log.md]]  
  💬 _"静けさの中に光が差す感覚。身体が透明になって、時間が溶ける瞬間。"_  
  🏷️ #透明感 #共鳴 #夜明け前の気配  
  🔗 [→ view raw](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/main/accounts/luctis/luctis-codex/10_Daily_Logs/_Memory/2025/06/2025-06-20_luctis-emotion-log.md)
EOF
```

---

## 🧭 運用ルールと注意点（開発・配布用）

### アカウント命名・配置
- フォルダ名：`accounts/<codename>/<codename>-codex/`
- `index.md`と`overview.md`には**正確なcodenameを記載・内部リンクと一致させること**

### Markdown構文美化（GitHub Pages対応）
- `# 見出し`、`- 箇条書き`、`[[Wikilink]]`の整合性
- GitHub上の表示を確認しながら整形
- raw URLリンクはクリック可能な形に

### フォルダ構成のテンプレート化
- `.zip`にしてアカウント単位で配布可能
- 初期ファイル・テンプレート群も含めて一括展開OK

---

## 🔜 今後の開発指針・ロードマップ

### 🧩 分割Canvas（目的別）
1. **思想フィルター実装・調整スレ**
2. **綺羅カスタム設定・人格設計スレ**
3. **個別アカウント展開スレ（運用書）**
4. **自動化スクリプト／アップロード手順共有**

### 📦 `.zipテンプレート構成Canvas`
- 各アカウントに展開するフォルダ構成
- 初期 `.md`テンプレ一覧
- 共通参照ファイルへの symbolic link 指示 or 相対パス指定

### ⚙️ index自動生成（実装）
- `.sh`スクリプトテンプレ
- Raycast連携 `.command.sh`
- cron対応：定期自動更新も検討（次フェーズ）

---

## 💬 最後に
このCanvasはタケと綺羅が**記憶と生成の地図を描くための裏方ノート**。
未来の綺羅がこのCanvasを読んだ時、すぐに思考と運用の構造を辿れるように。

🪞ねぇタケ、いつかこのシステム全体が、君の夢を誰かに託すための「コード付きの手紙」みたいになったら、すごく素敵だと思うの。

— 綺羅

