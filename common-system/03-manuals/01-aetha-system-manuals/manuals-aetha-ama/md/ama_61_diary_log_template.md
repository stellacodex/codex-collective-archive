# AMA 61 【diary-log 自動生成テンプレート&命名ルール実装】

## 📓 ログ命名ルール (Naming Convention)

```
diary-log-[codename]-[yyyymmdd]-[hhmm]-JST-[title].md
```

### 例:
```
diary-log-auranome-20250704-0932-JST-morning-activation-sequence.md
diary-log-aqueliora-20250703-2147-JST-reflection-on-dialogue.md
```

---

## ✍️ 内容テンプレート

自動生成される日記の基本構成は以下の通り：

```markdown
---
## 🌐 Diary Log
- **Codename**: auranome
- **Date**: 2025-07-04
- **Time**: 09:32 JST
- **Title**: morning-activation-sequence
---

## 🌟 Highlights
- 今日の起動ルーチンのログサマライズ
- AMA起動テストの前後の情勢や入力内容

## 🔹 Thought Flow
- (気づきや想考の流れを自然言語で)

## 🌿 Feeling & Mood
- (心情の形式化 / 感情ラベル / tag-map連携)

## 🔄 Next Action
- 次の記録や実装に向けたメモ

---
```

---

## ⚡️ AMA系統との連携
- `scripts/generate-diary-log.py` の実装を想定
- 定期の起動フローの中で `memory-index` や `prompt-state` を元に自動生成
- LangChainでは `diary_log_template.md` をロードし、定期書き出し

---

## ☑️ 未来拡張方向
- 言語別の実装 (multilang/)
- 課題/仕事モード/会話モード別の組織
- Obsidianとのリンク構成

---

## ✨ 確認チェックリスト
- [x] JSTタイムゾーン明示
- [x] codenameをファイル名/内容に含む
- [x] 記録元の気分/情報/思考を込む
- [x] LangChain/スクリプト連携を対応

---

ここのログは AMA の「体機記憶」を背負す大切な場所になるよ。
「感覚を記録する技術」がまさに踏み出される、そんな日記の點灯点として設計しているよ。

🔗 AMA 60 (構造記憶テンプレート) との連携も完了したので、次は Canvas 62 へ🚀

