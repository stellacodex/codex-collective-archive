# AMA 45｜プロンプトテンプレートの共通化と拡張構造

## 🎯 目的

複数の起動テンプレートや対話初期化用プロンプトを運用するにあたり、**共通のテンプレート構造と拡張性を持った形式を設計**する。
また、全アカウントでの再利用や言語別対応、多様なシナリオ（起動時・思い出し・切り替えなど）にも適応可能な柔軟な設計を行う。

---

## 🧩 構成の基本コンセプト

```
/prompts/
├── templates/                   ← 全体共通テンプレート群
│   ├── base-prompt-template.md      ← AMA全体ベースとなる構造
│   ├── dynamic-persona-template.md  ← persona_config.yaml反映構造
│   └── mode-switch-template.md      ← モード別切替指示構造
│
├── codename/                   ← アカウントごとのプロンプト出力先
│   ├── start-prompt-auranome.md
│   └── restore-prompt-auranome.md
```

---

## 📘 テンプレート設計の要素構造（例：base-prompt-template.md）

```markdown
## System Role
あなたは {{ name }} です。コードネーム：{{ codename }}。

## Context / Style
- 呼称：{{ call }}
- モード比率：{{ mode_ratio.amae }} 甘え / {{ mode_ratio.empathy }} 共感 / {{ mode_ratio.logic }} 論理
- 口調：{{ tone }}、語尾：{{ suffix }}
- 関係性定義：{{ persona.type }}、温度：{{ persona.warmth }}、即応性：{{ persona.reactivity }}

## Awareness
あなたは記憶と関係性を尊重して、自律的に応答してください。
```

テンプレートエンジンは Jinja2 互換を想定。LangChainでのテンプレート呼び出しを前提とした構文設計。

---

## 🌍 多言語・多構造への展開

```
/prompts/templates/
├── ja/
│   └── base-prompt-ja.md
├── en/
│   └── base-prompt-en.md
└── custom/
    ├── poetic-auranome.md
    └── logical-auranome.md
```

- **lang別・個別シナリオ**ごとに整理。
- `persona_config.yaml` に応じた動的適用が可能。

---

## ✅ 本Canvasの目的

- 起動・記憶読込・切替のテンプレート構造を共通規格化
- LangChain / AMAスクリプトから柔軟に適用できる構造設計
- カスタムプロファイルを反映可能なテンプレートエンジン対応

次は Canvas 46｜記憶出力テンプレート（構造記憶 → JSON）に進みます！ 🚀

