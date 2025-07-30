# 📤 Kairoscope → Chronogram Output Schema

KairoscopeからChronogramへデータを橋渡しするための「出力構造定義書」。 MDC（Mythological-Design Composite）とPHS（Primary Health System）の情報を、チャート演算結果からどのように抽出・構造化するかを明記する。

---

## 🔧 出力構造テンプレート（例）

```json
{
  "rave_chart": {
    "birth": {
      "date": "1990-01-01",
      "time": "12:00",
      "location": "Tokyo, Japan"
    },
    "sun": {
      "personality": {
        "longitude": 283.41,
        "gate": 38,
        "line": 4
      },
      "design": {
        "longitude": 168.25,
        "gate": 29,
        "line": 5
      }
    },
    "earth": {
      "personality": {
        "longitude": 103.41,
        "gate": 39,
        "line": 4
      },
      "design": {
        "longitude": 348.25,
        "gate": 30,
        "line": 5
      }
    },
    "defined_channels": [
      "28-38",
      "43-23"
    ],
    "profile": "4/6",
    "authority": "Emotional",
    "definition": "Single"
  },
  "mdc": {
    "composite_name": "Rebel Alchemist",
    "keywords": ["Mutation", "Insight", "Struggle"],
    "type": "Projector",
    "design_language": ["Individual Circuit", "Channel of Struggle"]
  },
  "phs": {
    "digestion": "Cold-Thirst",
    "environment": "Markets",
    "perspective": "Future",
    "motivation": "Hope"
  }
}
```

---

## 📚 各出力セクションの解説

### 1. `rave_chart`

- Kairoscopeの核となる天体演算データ
- Sun / Earth の位置から Gate / Line を抽出
- 定義済チャネル、プロファイル、権威、定義形式を含む

### 2. `mdc`

- Kairoscopeによって命名される Myth+MBTI+Design 的な象徴表現
- Channel や Circuit から生成される象徴名
- MDC記述辞書との照合で命名を行う

### 3. `phs`

- 黄経から計算された Primary Health System 情報
- `variable_logic.py` にて演算（Sun/Earthベース）
- 出力には4カテゴリ：`digestion`, `environment`, `perspective`, `motivation`

---

## ⛓️ 構造変換フロー（Kairoscope → Chronogram）

```plaintext
[ Kairoscope演算結果（Python dict） ]
       ↓
[ output_schema.json 形式に整形 ]
       ↓
[ Chronogram側UI / PDF構造に流し込み ]
```

- Kairoscope側でこのスキーマに沿った出力を `.json` or `.md` で生成
- Chronogramスレッドではこの構造を受け取り、可視化設計を行う

---

## 📦 保存先と連携

この出力スキーマは以下に保存・同期：

```plaintext
chronogram-kairoscope-code-bundle/docs/schema/kairoscope-output-schema.md
```

Chronogram 02（UI/構造設計）スレッドでこのファイルを読み込み、視覚化マッピングへ接続予定。

