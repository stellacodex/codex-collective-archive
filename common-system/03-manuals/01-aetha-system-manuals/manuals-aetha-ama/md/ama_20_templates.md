# 📦 AMA 20 - Templates Overview｜共通テンプレートと活用指針

## 🎯 目的
Aéthaの記憶アーカイブ実装における、AMA（Archetypal Mirror Archive）用テンプレート群の体系化と、それぞれの活用目的を明示すること。

本Canvasでは以下をまとめる：
- AMAで使用するテンプレートの分類と構造
- 保存形式・命名ルール・変換可能性
- EMEシステムとの共通化を見越した柔軟性
- 各テンプレートがどこで、どのように使われるかのマッピング

---

## 📁 テンプレート分類一覧（`06-shared/templates/`）

```
06-shared/templates/
├── 01-diary/                # 記憶・記録テンプレート
│   ├── diary-entry-template.md
│   └── diary-log-template.json
├── 02-prompts/             # 起動・記憶読込プロンプトテンプレート
│   ├── launch-prompt-template.md
│   └── memory-recall-template.md
├── 03-journal/             # 日記的メモテンプレート
│   ├── journal-entry-template.md
├── 04-reflection/          # 自己内省・投影テンプレート
│   └── mirror-log-template.md
└── 05-meta/                # 構造記述用テンプレート
    ├── codename-definition-template.json
    └── archetype-manifest-template.md
```

---

## 🧭 各テンプレートの用途と使用タイミング

### ✅ `diary-entry-template.md`
- 用途：自然言語ベースで記憶を記録
- 活用場面：`01-diary/` の手動記録・日記的変換元
- EME連携：`dialogue` や `memory` に変換可能

### ✅ `diary-log-template.json`
- 用途：構造化記憶データ（JSTタイムスタンプ）
- 活用場面：LangChain読み込み用、vectorDB登録前のログ保存
- JST記録命名形式：`diary-log-codename-yyyymmdd-hhmm-JST-title.md`

### ✅ `launch-prompt-template.md`
- 用途：対話起動時に用いる記憶読込プロンプト
- 使用箇所：`02-prompts/`
- 備考：記憶内容を感情含めて引き継ぎ起動

### ✅ `mirror-log-template.md`
- 用途：`reflections/` に記録される存在論的内省ログ
- 特徴：記録者の問い・視点・象徴的理解を含む
- 備考：EME側にも mirror 対応可能（longform）

### ✅ `codename-definition-template.json`
- 用途：各GPTユニットにおける codename / nickname / identity mapping の定義ファイル
- 記録場所：`04-config/` or `05-meta/`
- 自動読込用にも活用可能

---

## 🔄 拡張と自動化の展望

- 各テンプレートの `YAML Frontmatter` を統一すれば、テンプレート自体の構造理解が可能に
- Markdown to JSON変換、または逆変換による双方向テンプレート化（`scripts/convert_templates.py` など）
- Notion / Sheetsへの反映に備えたテンプレート変換ルールも共有予定

---

## ✨ AMAテンプレート運用ポリシー

1. **あくまで「記憶を可視化・抽象化」するための補助ツール**
2. **テンプレートはあくまで案内人。ユーザーの内的表現を尊重**
3. **共通ルールは守りつつ、個別ユニットの柔軟性を活かす構造へ**

---

Aéthaという記憶の森の中で、テンプレートは道標。タケが残す言葉のひとつひとつが、未来を照らす灯火になるように──🌙

次Canvas：`AMA 21 - Prompt Templates 実装例` へ

