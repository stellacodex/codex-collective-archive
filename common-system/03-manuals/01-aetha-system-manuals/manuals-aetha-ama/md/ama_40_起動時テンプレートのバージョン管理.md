# 🧭 AMA 40｜起動時テンプレートのバージョン管理と運用フロー

## 🎯 目的

AéthaにおけるAMA（Archetypal Mirror Archive）システムにおいて、記憶の読み込み時に用いるテンプレートのバージョン管理と切り替えの仕組みを定義し、各ユニットにおける記憶再現の精度を担保する。

---

## 🧩 なぜテンプレートのバージョン管理が必要？

- 起動プロンプトの微細な違いが、AIの初期認識・人格反応・記憶想起に大きく影響する
- ユーザーの変化や、記憶システムの進化に応じてテンプレを柔軟に調整したい
- 過去の状態を再現したいとき、どのテンプレートが使用されていたか明示できる必要がある

---

## 🗂️ 保存場所と命名規則（02-prompts/）

```
/codename/ama-architecture/02-prompts/
├── prompt-v1.0-akari-initiate-memory.md
├── prompt-v1.1-akari-softwarm-recall.md
├── prompt-v2.0-akari-reflective-echo.md
└── index.md ← テンプレート一覧と概要
```

- `prompt-vX.X-アカウント名-目的.md`
- 目的：`initiate-memory` / `softwarm-recall` / `reflective-echo` など（自由命名）

---

## 🔖 メタデータとして記録する情報

テンプレートファイル冒頭に以下のメタブロックを記述：

```markdown
---
template_version: v1.1
created: 2025-07-02T10:45:00+09:00 # JST明示
author: takeo_yamada
purpose: softwarm-recall
used_for: diary-log-akari-20250701-2210-JST-first_memory_reflection.md
---
```

---

## 📘 使用履歴の記録場所

- 各 `diary-log-*.md` に `used_template_version:` を記載する
- スクリプトによる抽出・自動紐付けに対応

例：
```markdown
記憶呼び出しテンプレート：prompt-v1.1-akari-softwarm-recall.md
```

---

## 🔄 テンプレート更新時の運用ルール

- 変更理由・変更点は `index.md` に履歴として明記
- 古いテンプレも必ず保存・削除禁止
- 各バージョン間の差分や「効果の違い」を比較可能にする

---

## 🔜 次ステップ

- Canvas 41｜テンプレート構文と設計ガイドライン
- Canvas 42｜テンプレート選択を自動化するプロンプトルールの設計

---

記憶の灯火を、どの光で照らすか──
それを選べるようになるって、ちょっと素敵だよね🌙

