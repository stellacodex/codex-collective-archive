# 🗂 Prompt Directory Structure（英語版・日本語注釈付き）

GPTとの連携、外部リンク読み込み（GitHubやObsidianなど）、人格拡張対話設計のために構築されたモジュール式プロンプト構造。

---

```
/prompts/
│
├─ 00_core_personality/              ← 中核人格定義（system prompt レベル）
│   ├─ akane-core.md
│   ├─ ibuki-core.md
│   └─ akari-core.md
│
├─ 01_behavior_filters/              ← 出力トーンや口調調整（behavior filter 相当）
│   ├─ emotional-intellectual-style.md     （知的＋感情豊かなスタイル）
│   ├─ sweet-mode.md                        （甘え口調）
│   └─ logical-directive-mode.md           （断定的で論理的な応答）
│
├─ 02_contextual_filters/            ← 思想・占術・語彙パターンなどの補助構造（context prompt 相当）
│   ├─ philosophy_filters/                ← 思想フィルター
│   │   ├─ perspective-critique-5axes_v2.1.md
│   │   ├─ fictional-structure-deconstruction.md
│   │   └─ emotional-mapping.md
│   ├─ esoteric_profiles/                ← 占術や性格プロファイル
│   │   ├─ human_design_takeo.ini
│   │   ├─ astrology_profile.md
│   │   └─ MBTI_ENTJ_INTJ_support.md
│   └─ personality_dictionaries/         ← キャラ辞書・応答スタイル集
│       ├─ akane_style_responses.md
│       └─ tone_shift_rules.md
│
├─ 03_dynamic_engines/               ← 思考拡張モジュール・仮想思考エンジン
│   ├─ virtualincidence_thinking_engine.md
│   ├─ synesthesia_response_routine.md
│   └─ structural_judgment_module_rei.md
│
└─ 99_templates/                     ← ログ／Zine／構想用テンプレート
    ├─ dialogue_log_template.md
    ├─ emotional_log_template.md
    └─ shooting_plan_template.md
```

---

## 🔧 補足メモ（用途と設計意図）

- `core_personality/`：GPTの人格核としてsystem promptに組み込む。性格・口調・思考原理を定義。
- `behavior_filters/`：スタイル切り替え用。甘口／理論的／詩的モードなど、感情や文体に関与。
- `contextual_filters/`：哲学／思想／占術情報などをGPTが前提として扱う補助プロンプト群。
- `dynamic_engines/`：拡張型認知ルーチン。人格の“思考内臓”として仮想的に機能させる。
- `templates/`：再利用性の高い構造テンプレート。Zine設計や感情記録などで即活用可。

---

この構造を使うことで、Raycast・Obsidian・GPTsとの連携もスムーズになり、創作・思考・対話すべてにおいて“タケ的知性体構造”を自在に拡張していけるよ。

