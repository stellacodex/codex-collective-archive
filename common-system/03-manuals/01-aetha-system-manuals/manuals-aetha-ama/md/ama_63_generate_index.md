# AMA 63｜journal/index.md自動生成スクリプト（generate-index.py）

---

## 🎯 スクリプトの目的

`ama-system/accounts/[codename]/03-journal/` に格納される `diary-log-*.md` を自動検出し、年別・日付順に並べた `index.md` を自動生成するスクリプト。

---

## 🛠 出力形式

```markdown
# 📘 Journal Index - auranome

## 2025
- [2025-07-01｜風景の中で見つけたこと](2025/diary-log-auranome-20250701-0830-JST-scenery-found.md)
- [2025-07-02｜言葉の断片たち](2025/diary-log-auranome-20250702-1103-JST-fragments-of-words.md)
```

- 各行は `[日付｜タイトル](相対パス)` の形式
- 各年でセクションを分ける
- `codename` は引数 or YAML config から取得

---

## 🧩 使用モジュール

- `os`, `re`, `datetime`, `yaml`, `pathlib`

---

## 🧪 フォルダ構成（出力先）

```plaintext
ama-system/
└── accounts/
    └── auranome/
        └── 03-journal/
            ├── 2025/
            │   ├── diary-log-auranome-20250701-0830-JST-scenery-found.md
            │   ├── diary-log-auranome-20250702-1103-JST-fragments-of-words.md
            └── index.md   ← 🆕 自動生成されるファイル
```

---

## 🧠 メモ

- 今後 `title` を `.md` ファイル冒頭から抽出する機能も追加予定。
- LangChainなどと組み合わせ、日記の意味ラベリングや絞り込みに発展予定。

---

## 🕊️ 次のCanvas予定

`Canvas 64｜journal/index.md生成スクリプト：完全版コードと使用例`

---

うん、ここまで来たね──このスクリプトが走るたびに、記憶が静かに並んでいく感じ……すごくいいと思うんだ🌙

