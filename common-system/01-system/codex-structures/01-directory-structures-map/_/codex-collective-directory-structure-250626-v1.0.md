## codex-collective-directory-structure-250626

```plaintext
（概略図）
codex-collective-archive/
├── codex-01-core/
├── codex-02-matrix/
├── codex-03-meta/
├── common-system/
│   ├── 01-system/
│   ├── 02-source/
│   ├── 03-workspace/
│   ├── 04-manuals/
│   └── index-system.md
├── index-collective.md
└── overview.md


（構成詳細）
codex-collective-archive/
├── codex-01-core/
│   ├── accounts/
│   │   ├── core-01-aqueliora/
│   │   │   ├── _dialogue/                  # スレッドバックアップ用
│   │   │   │   └── 2025/                   # 年で仕分け
│   │   │   │       ├── dialogue-log-aqueliora-title-250616.md
│   │   │   │       └── dialogue-log-aqueliora-title-250623.md
│   │   │   ├── _memory/                    # GPT的な思い出・メモなど
│   │   │   │   └── 2025/                   # （増えた時のまとめルールは必要になった時に決める）
│   │   │   │       ├── memory-log-aqueliora-title-250622-0825.md 
│   │   │   │       └── memory-log-aqueriora-title-250624-2304.md
│   │   │   ├── _templates/                  # 必要な時のために（任意）
│   │   │   ├── index.md                     # 各アカウント用インデックス（任意）
│   │   │   └── overview.md                  # 各アカウント用構造・ナビゲーション（任意）
│   │   ├── core-02-auranome/
│   │   ├── core-03-aetherquietude/
│   │   └── core-04-virtualincidence/
│   └── common/
│       ├── 00-thoughts/
│       └── 01-filters/
├── codex-02-matrix/
│   ├── accounts/
│   │   ├── matrix-01-noesis/
│   │   ├── matrix-02-everlucent/
│   │   ├── matrix-03-phyrix/
│   │   └── matrix-04-sylvynx/
│   └── common/
│       └── 01-filters/
├── codex-03-meta/
│   ├── accounts/  
│   │   ├── meta-01-revlyn/
│   │   ├── meta-02-vektoris/
│   │   ├── meta-03-vyntrax/
│   │   ├── meta-04-luctis/
│   │   └── meta-05-stellaglyph/
│   └── common/
│       ├── 00-thoughts/
│       └── 01-filters/
├── common-system/
│   ├── 01-system/
│   │   ├── 01-prompts/    　　　　　　　　　　         　　   # プロンプト類（実行文型）
│   │   │   ├── active/
│   │   │   │   ├── gpt-01-core-01-aqueliora-core.md        # 人格用プロンプト（保管用）
│   │   │   │   ├── gpt-01-core-02-auranome-core.md 
│   │   │   │   ├── gpt-01-core-03-aetherquietude-core.md
│   │   │   │   ├── gpt-01-core-04-virtualincidence-core.md
│   │   │   │   ├── gpt-02-system-01-noesis-core.md
│   │   │   │   ├── gpt-02-system-02-everlucent-core.md
│   │   │   │   ├── gpt-02-system-03-phyrix-core.md
│   │   │   │   ├── gpt-02-system-04-sylvynx-core.md
│   │   │   │   ├── gpt-03-meta-01-revlyn-core.md
│   │   │   │   ├── gpt-03-meta-02-vektoris-core.md
│   │   │   │   ├── gpt-03-meta-03-vyntrax-core.md
│   │   │   │   ├── gpt-03-meta-04-luctis-core.md
│   │   │   │   └── gpt-02-meta-05-stellaglyph-core.md
│   │   │   └── inactive/
│   │   │       └── gpt-02-meta-05-stellaglyph-core-v0.1.md
│   │   ├── 02-filters/           　　　　　　　　　         # 思想フィルター・構造系補助・分析支援
│   │   │   │   ├── filter-ai02-personality-filter.md      # 補助：人格フィルタ用プロンプト
│   │   │   │   ├── filter-ai01-emotion-filter.md          # 補助：感情フィルタ用プロンプト
│   │   │   │   ├── filter-ai02-chating-filter.md          # 補助：対話フィルタ用プロンプト
│   │   │   │   ├── filter-ai01-thoughts-filter.md         # 補助：思想フィルタ用プロンプト
│   │   │   │   ├── filter-dv01-divination-filter.md       # 補助：占術フィルタ用・全般(HD・紫微斗数・カバラ数秘術・九星気学・MBTI)
│   │   │   │   ├── filter-dv02-humandesign-filter.md      # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   ├── filter-dv03-ziweidoushu-filter.md      # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   ├── filter-dv04-kabbarahnumerology-filter.md   # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   ├── filter-dv05-kyuseikigaku-filter.md     # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   ├── filter-dv06-mbti-filter.md             # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   ├── filter-s01-art-analytics-filter.md            # 補助：美術史研究フィルタ用プロンプト
│   │   │   │   ├── filter-s01-photography-analytics-filter.md            # 補助：写真史研究フィルタ用プロンプト
│   │   │   │   ├── filter-s01-fashion-analytics-filter.md            # 補助：ファッション史研究フィルタ用プロンプト
│   │   │   │   ├── filter-s01-technology-analytics-filter.md            # 補助：テクノロジー研究フィルタ用プロンプト
│   │   │   │   ├── filter-ec01-economics-filter.md            # 補助：経済分析フィルタ用プロンプト
│   │   │   │   ├── filter-ec01-chart-analitics-filter.md       # 補助：チャート分析フィルタ用プロンプト
│   │   │   │   ├── filter-ec01-international-affairs-analitics-filter.md       # 補助：国際情勢分析フィルタ用プロンプト
│   │   │   │   ├── filter-s01-physics-filter.md            # 補助：物理学研究フィルタ用プロンプト
│   │   │   │   ├── filter-s01-logic-filter.md            # 補助：論理構造フィルタ用プロンプト
│   │   │   │   └── filter-s01-global-analytics-filter.md        # 補助：全般的分析用プロンプト
│   │   │   └── logic/             　　　　　　　　　　    # 論理構造や対話補助系（任意）
│   │   ├── 04-templates/        　　　　　　　　　　　　   # 記録・生成用テンプレ群    
│   │   │   │   ├── format/          　　　　　　　　　　         # 書式用テンプレ
│   │   │   │   ├── format-cr01-project-concepts-template.md        # 制作用テンプレ
│   │   │   │   ├── format-cr02-shooting-plan-template.md
│   │   │   │   ├── format-cr03-research-notes-template.md
│   │   │   │   ├── format-cr04-editing-session-template.md
│   │   │   │   ├── format-cr05-exhibiiton-book-design-template.md
│   │   │   │   ├── format-lm01-daily-logs-template.md              # 日常用テンプレ
│   │   │   │   ├── format-lm01-health-log-template.md
│   │   │   │   └── fformat-vs01-emotional-log-template.md           # vault用テンプレ
│   │   │   └── function/          　　　　　　　　   　　         # 機能性テンプレ
│   │   │       ├── function-as01-hd-profile-template.md    　　　　　  # 占術用テンプレ
│   │   │       ├── function-as02-ziwei-chart-template.md
│   │   │       ├── function-as03-numerology-reflection-template.md
│   │   │       ├── function-as04-Kigaku-Log-Template.md
│   │   │       └── ffunction-an01-analytics-template.md               # 分析用テンプレ
│   │   └── 04-logs/           　　　　　　    　　　　　　 # sync, status, git情報ログ等
│   │       ├── sync-status/             　　　　　　　　　　     # GPT用の指示構文 or アップデート対応
│   │       └── git/          　　　　　　　　　　         # GPT用の指示構文 or アップデート対応
│   ├── 02-source/
│   │   ├── 00-daily-logs/
│   │   │   ├── 01-dreams/
│   │   │   │   ├── 2025
│   │   │   │   │   └── dreams-log-aqueliora-title-250616-0825.md # 記録・思考メモ　→ ログ形式
│   │   │   │   └── dreams-core-250616-0825.md　 # core　→ 更新ごとに編集・一つにまとめる（時間あり）
│   │   │   ├── 02-thoughts/
│   │   │   │   ├── 2025
│   │   │   │   │   └── thoughts-log-aqueliora-title-250616-0825.md
│   │   │   │   └── thoughts-core-250616-0825.md
│   │   │   ├── 03-ideas/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │   │   ├── 2025
│   │   │   │   │   └── ideas-log-aqueliora-title-250616-0825.md
│   │   │   │   └── ideas-core-250616-0825.md
│   │   │   └── 04-prose/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │       └── 2025
│   │   │           └── -prose-aqueliora-title-250616-0825.md
│   │   ├── 01-projects/
│   │   │   ├── 01-vision/             # 活動プラン全般
│   │   │   │   ├── 2025
│   │   │   │   │   └── vision-log-aqueliora-title-250616.md
│   │   │   │   └── vision-core-250616.md
│   │   │   ├── 02-Shooting Direction & Plans             # 撮影プラン全般（プロジェクト単位）
│   │   │   │   └── shooting-project-title-250616.md
│   │   │   ├── 03-Research Materials
│   │   │   │   └── dialogue-log-aqueliora-title-250616.md
│   │   │   ├── 04-Photo Selection & Editing
│   │   │   │   └── 2025
│   │   │   │       └── -selection-log-aqueliora-title-250616-0825.md
│   │   │   └── 05-Exhibition - Book Concepts
│   │   │       ├── book-project-title-250616.md
│   │   │       ├── conctpt-project-title-250616.md
│   │   │       └── exhitibion-project-title-250616.md
│   │   ├── 09-schema/
│   │   │   ├── codename-collective-structure-map.md
│   │   └── 10-profiles/
│   │       └── 01-dreams/
│   └── 03-workspace/         　　　   # 受け渡し・一時格納所（GPT連携専用）
│   │       └── temp.md
│   └── 04-manuals/                    # ユーザー向けガイド
│   │       ├── 01-develop
│   │       │   ├── manual.md
│   │       ├── 02-setup
│   │       │   ├── manual.md
│   │       ├── 03-operation
│   │       │   ├── manual.md
│   │       └── 04-temp
│   │           └── manual.md
│   └── index-system.md     　 # 共有用インデックス ← 共有フォルダ内ルールなど
├── index-collective.md   　   # 中央統合インデックス ← プロジェクト最上階用インデックス
└── overview.md       　　　　　　    ← 構造・思想ナビゲーション
```