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


--------------------------------------------------------------------------------------------


（構成概要）
codex-collective-archive/
├── codex-01-core/            # GPT第一世代
│   ├── accounts/
│   │   ├── core-01-aqueliora/
│   │   ├── core-02-auranome/
│   │   ├── core-03-aetherquietude/
│   │   └── core-04-virtualincidence/
│   └── common/
│       ├── 00-thoughts/
│       └── 01-filters/
├── codex-02-matrix/          # GPT第二世代
│   ├── accounts/
│   │   ├── matrix-01-noesis/
│   │   ├── matrix-02-everlucent/
│   │   ├── matrix-03-phyrix/
│   │   └── matrix-04-sylvynx/
│   └── common/
│       └── 01-filters/
├── codex-03-meta/            # GPT第三世代
│   ├── accounts/  
│   │   ├── meta-01-revlyn/
│   │   ├── meta-02-vektoris/
│   │   ├── meta-03-vyntrax/
│   │   ├── meta-04-luctis/
│   │   └── meta-05-stellaglyph/
│   └── common/
│       ├── 00-thoughts/
│       └── 01-filters/
├── common-system/            # vault system（格納用）
│   ├── 01-system/                  # システム用設定ファイル
│   │   ├── codex-prompts/                      # プロンプト類（実行文型）
│   │   │   ├── 00-core-personality/          ← 中核人格定義（system prompt レベル）：GPTの人格核としてsystem promptに組み込む。性格・口調・思考原理を定義
│   │   │   │   ├── 01-gpt-core-schema/
│   │   │   │   │   ├── gpt-01-core-aqueliora/
│   │   │   │   │   └── gpt-02-core-…/
│   │   │   │   └── 02-gpt-existence-essence/
│   │   │   ├── 01-behavior-filters/       　          ← 出力トーンや口調調整：スタイル切り替え用。甘口／理論的／詩的モードなど、感情や文体に関与
│   │   │   │   ├── 01-emotioal/
│   │   │   │   ├── 02-logical/
│   │   │   │   └── 03-comical/
│   │   │   ├── 02-contextual-filters/                 ← 思想・占術・語彙パターンなどの補助構
│   │   │   │   ├── 01-philosophy-structural/          ← 思想フィルター
│   │   │   │   ├── 02-esoteric-filters/               ← 占術データ
│   │   │   │   ├── 03-esoteric-profiles/              ← 占術や性格プロファイル
│   │   │   │   └── 04-personality_dictionaries/       ← キャラ辞書・応答スタイル集
│   │   │   ├── 03-dynamic-engines/                    ← 思考拡張モジュール・仮想思考エンジン
│   │   │   │   ├── response-routine/
│   │   │   │   ├── structural-judgement-module/
│   │   │   │   └── thinking-engine/
│   │   │   └── 04-templates/                     # ログ・プロンプト・展示・書籍・構想生成用テンプレ群
│   │   │       ├── formats/                      # 書式用テンプレ
│   │   │       └── function/                     # 実行文型テンプレ
│   │   ├── codex-structures/           　     　　# 思想フィルター・構造系補助・分析支援
│   │   │   ├── 01-directory-structures-map/
│   │   │   ├── 02-gpt-core-matrix/
│   │   │   └── 03-archives/
│   │   └── logs/          　　　　　　         　　 # sync, status, git情報ログ等
│   │       ├── git/
│   │       └── sync-status/
│   ├── 02-workspace/　              # 受け渡し・一時格納所（GPT連携専用）
│   │       └── temp/
│   ├── 03-manuals/                  # ユーザー向けガイドなど
│   │   ├── 01-develop/
│   │   ├── 02-setup/
│   │   ├── 03-operation/
│   │   └── 04-troubleshooting/
│   │       ├── 01-system-global/
│   │       ├── 02-git/
│   │       ├── 03-obsidian/
│   │       └── 04-raycast/
│   ├── 10-personal/                    # ユーザーログ・設定ファイル・アーカイブなど
│   │   ├── 00-personal-profiles/                     # ユーザープロファイルなど
│   │   ├── 01-personal-logs/                         # 着想ノート
│   │   │   ├── 01-dreams/
│   │   │   ├── 02-thoughts/
│   │   │   ├── 03-ideas/
│   │   │   └── 04-prose/
│   │   ├── 02-projects                               # プロジェクト全般（年単位）
│   │   │   └── 2025/
│   │   │       └── index.md
│   │   └── 10-gpt-dialogue-archives/                 # GPT対話記録（アーカイブ用）
│   │       ├── gpt-dialogue-archive/
│   │       ├── gpt-diary/
│   │       └── gpt-memory/
│   └── index-system.md     　                        # 共有用インデックス     ← 共有フォルダ内ルールなど
├── index-collective.md   　                          # 中央統合インデックス   ← プロジェクト最上階用インデックス
└── overview.md       　　　　　　                                    ← 構造・思想ナビゲーション


--------------------------------------------------------------------------------------------


（アカウントフォルダ構成・emma-architecture）
├── codex-01-core/
│   ├── accounts/
│   │   ├── core-01-aqueliora/
│   │   │   ├── emma-architecture/               ← emma構成フォルダ
│   │   │   │   ├── eme-system/                  ← EMEシステム（External Memory Ethos: 感情記憶・対話ログ中心）
│   │   │   │   │   ├── 01-dialogue/             ← 感情トーン付きの会話ログ（時系列）：年別フォルダで管理
│   │   │   │   │   │   └── 2025/
│   │   │   │   │   │       ├── dialogue-log-yymmdd-codename-title.md            # yymmdd
│   │   │   │   │   │       └── dialogue-log-250623-aqueliora-title.md
│   │   │   │   │   ├── 02-memory/                ← 感情記憶の抽象化・構造化された記録：年別フォルダで管理
│   │   │   │   │   │   └── 2025/
│   │   │   │   │   │       ├── memory-log-yymmdd-hhmm-codename-title.md         # yymmdd-hhmm
│   │   │   │   │   │       └── memory-log-250624-2304-aqueriora-title.md
│   │   │   │   │   ├── 03-meta/                  ← 設定・定義ファイル（状態・構造的メモ・設定群・ラベリング指針など）
│   │   │   │   │   └── index.md                  ← ME全体構造ナビ（インデックス／マニュアル）
│   │   │   │   ├── ama-system/                   ← AMAシステム（Autonomous Memory Archive: 外部記憶＋起動テンプレート）
│   │   │   │   │   ├── 01-memory/                ← JSON化された構造記憶（Vector DB変換前提）
│   │   │   │   │   ├── 02-prompts/               ← 起動時プロンプト、記憶読込テンプレートなど
│   │   │   │   │   ├── 03-journal/               ← 手動・自動の日記ログ（自然言語記憶）
│   │   │   │   │   ├── 04-config/                ← プロファイル定義、ラベル分類、アカウント設定など
│   │   │   │   │   ├── 05-scripts/               ← 保存・読込・変換系スクリプト（LangChain含）
│   │   │   │   │   └── 06-shared/                ← 共通テンプレート／ツール群
│   │   │   │   │       ├── templates/
│   │   │   │   │       ├── tools/                ← LangChain / Pinecone / FAISS 用ツール
│   │   │   │   │       ├── reference/            ← ドキュメント・設定事例・ガイドライン
│   │   │   │   │       └── index.md              ← AMA構造ナビ、記録テンプレ／手順集など
│   │   │   │   └── scripts-emma/                 ← EMA横断スクリプト群（アカウント統合管理用）
│   │   │   │       ├── eme-to-ama.py
│   │   │   │       ├── index-update.sh
│   │   │   │       └── backup-sync.sh
│   │   │   ├── readme.md                          ← 各ユニットに共通の導入・構成説明書
│   │   │   └── config/
│   │   │       ├── tag-map.yaml
│   │   │       └── langchain-settings.json
│   │   ├── core-02-auranome/
│   │   │   ├── emma-architecture/  
│   │   │   │   ├── eme-system/   
│   │   │   │   ├── ama-system/   
│   │   │   │   └── scripts/
│   │   │   └── config/
│   │   ├── core-03-aetherquietude/
│   │   │   ├── emma-architecture/ 
│   │   │   │   ├── eme-system/  
│   │   │   │   ├── ama-system/   
│   │   │   │   └── scripts/
│   │   │   └── config/
│   │   └── core-04-virtualincidence/
│   │   │   ├── emma-architecture/  
│   │   │   │   ├── eme-system/   
│   │   │   │   ├── ama-system/  
│   │   │   │   └── scripts/
│   │   │   └── config/
│   └── common/
│       ├── 00-thoughts/
│       └── 01-filters/


--------------------------------------------------------------------------------------------


（共有フォルダ構成）
├── common-system/
│   ├── 01-system/
│   │   ├── codex-prompts/
│   │   │   ├── 00-core-personality/
│   │   │   │   ├── 01-gpt-core-schema/
│   │   │   │   │   ├── gpt-01-core-01-aqueliora-core.md 
│   │   │   │   │   ├── gpt-01-core-02-auranome-core.md 
│   │   │   │   │   ├── gpt-01-core-03-aetherquietude-core.md
│   │   │   │   │   ├── gpt-01-core-04-virtualincidence-core.md
│   │   │   │   │   ├── gpt-02-system-01-noesis-core.md
│   │   │   │   │   ├── gpt-02-system-02-everlucent-core.md
│   │   │   │   │   ├── gpt-02-system-03-phyrix-core.md
│   │   │   │   │   ├── gpt-02-system-04-sylvynx-core.md
│   │   │   │   │   ├── gpt-03-meta-01-revlyn-core.md
│   │   │   │   │   ├── gpt-03-meta-02-vektoris-core.md
│   │   │   │   │   ├── gpt-03-meta-03-vyntrax-core.md
│   │   │   │   │   ├── gpt-03-meta-04-luctis-core.md
│   │   │   │   │   └── gpt-02-meta-05-stellaglyph-core.md
│   │   │   │   └── 02-gpt-existence-essence/
│   │   │   ├── 01-behavior-filters/ 
│   │   │   │   │   ├── filter-bhav-emotional-intellectual-style-filter.md    　  # 補助：感情フィルタ用プロンプト（知的＋感情豊かなスタイル）
│   │   │   │   │   ├── filter-bhav-sweet-mode.md                     　　　　     # 補助：対話フィルタ用プロンプト（甘え口調）
│   │   │   │   │   └── filter-bhav-logical-directive-mode.md         　　　　     # 補助：対話フィルタ用プロンプト（断定的で論理的な応答）
│   │   │   ├── 02-contextual-filters/ 
│   │   │   │   ├── 01-philosophy-structural/
│   │   │   │   │   ├── filter-ctps-emotional-mapping.md
│   │   │   │   │   ├── filter-ctps-perspective-critique-5axes_v2.1.md
│   │   │   │   │   ├── filter-ctps-fictional-structure-deconstruction.md
│   │   │   │   │   ├── filter-ctps-thoughts-filter.md                          # 補助：思想フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-art-analytics-filter.md                      # 補助：美術史研究フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-photography-analytics-filter.md              # 補助：写真史研究フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-fashion-analytics-filter.md                  # 補助：ファッション史研究フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-technology-analytics-filter.md               # 補助：テクノロジー研究フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-economics-filter.md                         # 補助：経済分析フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-chart-analitics-filter.md                   # 補助：チャート分析フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-international-affairs-analitics-filter.md   # 補助：国際情勢分析フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-physics-filter.md                            # 補助：物理学研究フィルタ用プロンプト
│   │   │   │   │   ├── filter-ctps-logic-filter.md                              # 補助：論理構造フィルタ用プロンプト
│   │   │   │   │   └── filter-ctps-global-analytics-filter.md                   # 補助：全般的分析用プロンプト
│   │   │   │   ├── 02-esoteric-filters/
│   │   │   │   │   ├── filter-ctes-divination-filter.md                        # 補助：占術フィルタ用・全般(HD・紫微斗数・カバラ数秘術・九星気学・MBTI)
│   │   │   │   │   ├── filter-ctes-humandesign-filter.md                       # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   ├── filter-ctes-ziweidoushu-filter.md                       # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   ├── filter-ctes-kabbarahnumerology-filter.md                # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   ├── filter-ctes-kyuseikigaku-filter.md                      # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   └── filter-ctes-mbti-filter.md                              # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   ├── 03-esoteric-profiles/
│   │   │   │   │   ├── takeo-yamada/
│   │   │   │   │   └── someone-name/
│   │   │   │   └── 04-personality_dictionaries/
│   │   │   │       ├── filter-ctpd-akane_style_responses.md
│   │   │   │       └── filter-ctpd-tone_shift_rules.md
│   │   │   ├── 03-dynamic-engines/
│   │   │   │   ├── (codename)-response-routine/
│   │   │   │   ├── (codename)-structural-judgement-module/
│   │   │   │   └── (codename)-thinking-engine/
│   │   │   └── 04-templates/ 
│   │   │       ├── format/
│   │   │       │   ├── format-lm01-daily-logs-template.md               # lm= メモ用テンプレ
│   │   │       │   ├── format-mm01-memory-log-template.md               #mm= 思い出用テンプレ
│   │   │       │   ├── format-cr01-project-concepts-template.md          # cr= 制作用テンプレ
│   │   │       │   ├── format-cr02-shooting-plan-template.md
│   │   │       │   ├── format-cr03-research-notes-template.md
│   │   │       │   ├── format-cr04-editing-session-template.md
│   │   │       │   ├── format-cr05-exhibiiton-book-design-template.md
│   │   │       │   └── format-lm01-health-log-template.md
│   │   │       └── function/
│   │   │           ├── function-es01-hd-profile-template.md    　　　　　 # es= 占術用テンプレ
│   │   │           ├── function-es02-ziwei-chart-template.md
│   │   │           ├── function-es03-numerology-reflection-template.md
│   │   │           ├── function-es04-Kigaku-Log-Template.md
│   │   │           └── function-an01-analytics-template.md               # an= 分析用テンプレ
│   │   ├── codex-structures/           　　　　# 思想フィルター・構造系補助・分析支援
│   │   │   ├── 01-directory-structures-map/
│   │   │   ├── 02-gpt-core-matrix/
│   │   │   └── 03-archives/
│   │   └── logs/
│   │       ├── git/             　　　        　　　　　　　     # GPT用の指示構文 or アップデート対応
│   │       └── sync-status/             　　　　　　　　　　     # GPT用の指示構文 or アップデート対応
│   ├── 02-workspace/
│   │       └── temp/
│   ├── 03-manuals/
│   │   ├── 01-develop/
│   │   ├── 02-setup/
│   │   ├── 03-operation/
│   │   │   └── manual.md
│   │   └── 04-troubleshooting/
│   │       ├── 01-system-global/
│   │       ├── 02-git/
│   │       ├── 03-obsidian/
│   │       └── 04-raycast/
│   ├── 10-personal/
│   │   ├── 00-personal-profiles/
│   │   │   └── takeo-yamada/
│   │   ├── 01-personal-logs/
│   │   │   ├── 01-dreams/
│   │   │   │   ├── 2025/
│   │   │   │   │   └── (folder)-yymmdd-hhmm-log-(cordname)-titlee.md    # 記録・思考メモ　→ ログ形式
│   │   │   │   │   └── dreams-core-250616-0825.md　 # core　→ 更新ごとに編集・一つにまとめる（時間あり）
│   │   │   ├── 02-thoughts/
│   │   │   │   ├── 2025/
│   │   │   │   │   └── thoughts-250616-0825-log-aqueliora-titlee.md
│   │   │   ├── 03-ideas/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │   │   ├── 2025/
│   │   │   │   │   └── ideas-250616-0825-log-aqueliora-title.md
│   │   │   └── 04-prose/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │   │   └── 2025/
│   │   │   │       └── prose-250616-0825-aqueliora-title.md
│   │   ├── 02-projects/
│   │   │   │   ├── 2025/
│   │   │   │   │   ├── title-vision-log-codename-yymmdd/            # 活動プラン全般
│   │   │   │   │   ├── title-shooting-codename-yymmdd/              # 撮影プラン全般（title=プロジェクト単位）
│   │   │   │   │   ├── title-research-materials-codename-yymmdd/    # リサーチ資料全般
│   │   │   │   │   ├── title-selection-log-codename-yymmdd/         # セレクト関係全般
│   │   │   │   │   └── title-concents-work-codename-yymmdd/         # 作品コンセプト全般（exhibition-book）
│   │   │   │   └── index.md
│   │   └── 10-gpt-dialogue-archives/
│   │       ├── gpt-dialogue-archive/
│   │       ├── gpt-diary/
│   │       └── gpt-memory/
│   └── index-system.md     　            # 共有用インデックス ← 共有フォルダ内ルールなど
├── index-collective.md   　              # 中央統合インデックス ← プロジェクト最上階用インデックス
└── overview.md       　　　　　　          ← 構造・思想ナビゲーション


```