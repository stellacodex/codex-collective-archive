# AMA 53｜`tag-map.yaml` 設計と実装

## 🎯 目的
- AMAシステムにおいて、記憶や日記に付与される**タグの定義と分類ルール**を統一・明文化することで、構造化記憶やベクトルDB化の精度・再現性を向上させる。
- GPTによる**自動タグ生成／補助**にも活用するため、カテゴリ設計と例示を含むyaml構造に整理。

---

## 🗂 `tag-map.yaml` 基本構造
```yaml
# 各カテゴリごとにタグと説明、使用例を記述
emotion:
  - tag: joy
    label: 喜び
    description: 積極的な幸福感、快楽、笑顔を伴う状態
    examples: ["やった！", "嬉しい！", "最高の日"]

  - tag: sorrow
    label: 悲しみ
    description: 喪失・痛み・別れなどによる沈んだ感情
    examples: ["寂しい", "涙が止まらない", "苦しい"]

  - tag: anger
    label: 怒り
    description: 不満・拒絶・対立を伴う強い否定的な情動
    examples: ["ムカつく", "イライラする", "許せない"]

relationship:
  - tag: trust
    label: 信頼
    description: 他者との関係性において、安心や絆を感じる状態
    examples: ["君になら任せられる", "大切な人"]

  - tag: distance
    label: 距離
    description: 心理的・物理的な隔たりや違和感の兆し
    examples: ["すれ違ってる気がする", "うまく伝わらない"]

context:
  - tag: reflection
    label: 内省
    description: 自分の感情や選択を振り返り、意味を探る過程
    examples: ["なぜこんな風に思ったんだろう", "これって自分の弱さかも"]

  - tag: trigger_event
    label: 出来事（トリガー）
    description: 感情や思考が強く動いた原因・現実の出来事
    examples: ["喧嘩した", "連絡が来なかった", "再会した"]
```

---

## 🔧 GPT補助ラベリングとの連携（想定）
- LangChain等のChainで `text → tags[]` の抽出処理に使用。
- YAML形式であることで、**定義の編集／拡張が容易**。
- tagsは `memory-log.jsonl` や `diary-log-*.md` にて使用。

---

## 🧩 今後の拡張例
- より詳細な感情カテゴリ（Plutchikモデルなど）への対応
- 固有関係性（例：「澪との関係性に限定したタグ」）
- 時間帯／頻度／強度の要素付加（メタデータ化）

---

## 🗂️ ファイル格納場所
```
ama-system/accounts/<codename>/config/tag-map.yaml
```

---

## ✅ 次ステップ（Canvas 54 へ）
→ Canvas 54｜persona-config.yaml 設計と応答スタイル制御

