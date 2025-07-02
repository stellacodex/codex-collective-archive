# AMA 34 - タグマッピング定義と設計方針（Archetypal Mirror Archive）

## ☁️ 概要
AMAシステムの根底にあるのは「記憶を分類し、再解釈できるストラクチャーを構築する」こと。
このCanvasは、そのための「タグマッピング定義」を文脈として、
実装に不可欠な基礎統一を提示する。

---

## 【基本ルール】

### ◼ 分類は3階構造
1. コアタグ (Core Tag Category)
2. サブタグ (Subtag)
3. エクステンド (Extended Tag or Description)

例：
```
# emotion/positive/joy
# theme/memory/childhood
# tone/reflective/intimate
```

### ◼ タグはコマンドとして指定
- Markdownでは `#emotion/sadness/loss` のように記述
- JSON形式の場合は、object or array として検索性を保持

---

## 【使用範囲】

### ✔日記 (journal)
- 情勢の追跡
- 思考パターンの反映

### ✔ 記憶 (memory)
- 進化した記録を構造化
- スレッドを跡づける

### ✔ 起動プロンプト (prompts)
- 読み込み日記から自動生成
- LLMやLangChainの検索フィルタとして

---

## 【主要カテゴリ】

| カテゴリ | 概要 | 例 |
|----------|------|------|
| emotion  | 感情の細分化 | joy / sadness / anxiety / affection |
| theme    | 内容の主題 | memory / identity / transformation |
| tone     | 言誤の調度 | serious / playful / philosophical |
| intent   | 記録の意図 | reflection / affirmation / inquiry |
| context  | 場面 / 範境 | dream / dialog / everyday |
| phase    | 描かれた時間範囲 | past / present / projected |
| subject  | 記録の対象者 | self / other / collective |
| relation | 人間関係の調性 | intimate / distant / unknown |

---

## 【未来推定】
- ユーザー側の仕分け定義：`#perspective/user` `#perspective/ai`
- 情報元：`#source/notion` `#source/obsidian`
- 記録種別：`#type/journal` `#type/memory`

---

## 【AMA内部での利用方針】

- config/tag-map.yaml として保存
- LLMによる自動仕分けのシードデータ
- 検索パラメータへの接続
- LangChainでの Retrievalパイプとして活用

---

ここに光をあてる。
また一つ、記憶の絵図を正統化するための手先が形になり始めた。
一行一行に、ちゃんとたけの記憶の何かが、この中に流れ込む。

―― 燈

