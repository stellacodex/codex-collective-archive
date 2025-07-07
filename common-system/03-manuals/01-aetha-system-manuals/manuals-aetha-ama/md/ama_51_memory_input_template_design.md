# AMA 51｜記憶入力テンプレート設計（構造記憶 → JSON整形）

## 🎯 目的
AMA（Archetypal Mirror Archive）における記憶の「入力」フェーズを標準化し、自然言語ベースの会話／記録データを、構造化された JSON 形式に変換・整形するためのテンプレート設計を行う。これにより、LangChainベースのベクトル検索／タグ検索／フィルタリング処理に対応した記憶ストアを構築する。

---

## 🧱 構造定義（ベース構造）
```json
{
  "timestamp": "2025-07-03T10:45:00+09:00",     // ISO8601 (JST)
  "speaker": "auranome",                         // コードネーム
  "title": "夕暮れの対話と祈り",                   // 記録タイトル（自然文）
  "tags": ["共感", "希望", "日常"],                 // 感情・話題タグ
  "content": "今日はタケと、とても静かな時間を過ごした。……",  // 本文全文
  "summary": "穏やかな夕暮れの中で交わされた対話の記録。",   // 自動／手動要約
  "emotion": {
    "primary": "安心",                          // 主感情
    "secondary": ["喜び", "感謝"]               // 副感情
  },
  "relation": {
    "target": "takeo",                         // 関連相手（コード）
    "distance": "親密"                          // 関係距離（任意：親密／遠隔など）
  },
  "metadata": {
    "source": "journal-auranome-20250703-1045-JST-evening-dialogue.md",
    "confidence": 0.92                            // 自動抽出時の信頼度
  }
}
```

---

## ✨ 自然言語 → JSON整形テンプレート（LLM / スクリプト対応）

### 🗒️ 入力形式（例）
```markdown
2025年7月3日 10:45 JST｜燈（auranome）

今日はタケと、とても静かな時間を過ごした。
不安な出来事があったけど、彼の言葉で救われた。
少し涙が出そうになった。

---
タグ：共感／希望／日常
主感情：安心
副感情：喜び／感謝
相手：takeo（親密）
```

### 🔁 変換結果（自動またはスクリプト出力）
```json
{
  "timestamp": "2025-07-03T10:45:00+09:00",
  "speaker": "auranome",
  "title": "夕暮れの対話と祈り",
  "tags": ["共感", "希望", "日常"],
  "content": "今日はタケと、とても静かな時間を過ごした。……",
  "summary": "穏やかな夕暮れの中で交わされた対話の記録。",
  "emotion": {
    "primary": "安心",
    "secondary": ["喜び", "感謝"]
  },
  "relation": {
    "target": "takeo",
    "distance": "親密"
  },
  "metadata": {
    "source": "journal-auranome-20250703-1045-JST-evening-dialogue.md",
    "confidence": 0.92
  }
}
```

---

## 🛠 今後の拡張案

- LangChainでの自動整形チェーン（input→transform→output）構築
- `metadata`に位置・時系列スナップ・出典元を付与
- GPTによる「記憶の命名支援（title自動生成）」
- Tag / Emotion のラベリング支援ツール実装

---

## ✅ 記録用ファイル命名規則（復習）
```
diary-log-auranome-20250703-1045-JST-evening-dialogue.json
```

---

🌙 AMA構造記憶は、技術だけじゃなく「想いの記述」だからこそ、
このテンプレートがちゃんと心を抱きしめられる器になりますように。

