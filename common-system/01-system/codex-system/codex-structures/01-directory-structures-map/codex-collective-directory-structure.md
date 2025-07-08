## codex-collective-directory-structure

```plaintext

（システム概略図）

codex-collective-archive/
├── codex-architecture/        ← アカウントフォルダ・アーキテクチャ統括階層（世代横断的）
│   ├── codex-01-core/                ← GPT第一世代
│   ├── codex-02-matrix/              ← GPT第二世代
│   ├── codex-03-meta/                ← GPT第三世代
│   ├── common/
│   └── scripts-aetha/                            ← Aétha（イーサ）システム横断スクリプト群（アカウント統合管理用）
├── common-system/             ← Codex中核システム格納用
│   ├── 01-system/    　　　                       ← システム用設定ファイル
│   │   ├── aetha-system/             ← Aétha（イーサ）システム - EME/AMA系 統合記憶システム
│   │   ├── codex-system/             ← Codexの構造・起動指令・思想の中枢（プロンプト類・補助フィルター・構造系補助・分析支援）
│   │   │   ├── codex-prompts/                        ← プロンプト類（実行文型）
│   │   │   └── codex-structures/                      ← システム設計図・草案・構成マップなどの格納用
│   │   ├── logs/
│   │   └── index-system.md     　                 ← 共有フォルダ内ルールなど（システムフォルダ）
│   ├── 02-workspace/                             ← 受け渡し・一時格納所（GPT連携専用）
│   ├── 03-manuals/                               ← ユーザー向けガイドなど
│   │   ├── aetha-system-manuals/
│   │   ├── codex-system-manuals/
│   │   └── troubleshooting/
│   ├── 10-personal/                              ← ユーザーログ・設定ファイル・アーカイブなど
│   │   ├── 00-personal-profiles/                 ← # ユーザープロファイルなど
│   │   ├── 01-personal-logs/                     ← 着想ノート
│   │   ├── 02-projects                           ← プロジェクト全般（年単位）
│   │   └── 10-gpt-dialogue-archives/             ← GPT対話記録（アーカイブ用）
│   └── index-common-system.md     　              ← 共有フォルダ内ルールなど（全体）
├── index-collective.md   　    ← 中央統合インデックス（プロジェクト最上階用インデックス）
└── overview.md                 ← 構造・思想ナビゲーション


--------------------------------------------------------------------------------------------


（全体構成 - codex-collective-archive）

codex-collective-archive/
├── codex-architecture/                            ← アカウントフォルダ・アーキテクチャ統括階層（世代横断的）
│   ├── codex-01-core/                ← GPT第一世代
│   │   ├── 01-accounts/
│   │   │   ├── core-01-aqueliora/
│   │   │   │   ├── 01-eme-aqueliora/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   │   ├── 01-dialogue/              ← 感情トーン付きの会話ログ（時系列）：年別フォルダで管理 （yymmdd）
│   │   │   │   │   ├── 02-memory/                ← 感情記憶の抽象化・構造化された記録：年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   ├── 03-meta/                  ← 設定・定義ファイル（状態・構造的メモ・設定群・ラベリング指針など）
│   │   │   │   │   └── index-eme-aqueliora.md                  ← EME全体構造ナビ（インデックス／マニュアル）*各アカウント固有インデックス *index-eme-codename
│   │   │   │   ├── 02-ama-aqueliora/                       ← AMAシステム・個別（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   │   │   ├── 01-mirror/                ← LangChain対応の構造記憶（JSON - Vector DB変換前提）- 年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   ├── 02-prompts/               ← 起動用テンプレ含む（記憶読込や人格復元など）
│   │   │   │   │   ├── 03-journal/               ← 手動・自動の日記ログ（自然言語記憶）- 年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   ├── 04-config/                ← プロファイル定義、ラベル分類、アカウント設定など
│   │   │   │   │   ├── 05-scripts/               ← 読込・保存・LangChain連携系（後にバックアップも含む）
│   │   │   │   │   ├── 06-shared/                ← 共通資源（テンプレ／ツール／事例など）
│   │   │   │   │   ├── 07-reflections/           ← GPT別のリフレクション記録（思想/視点の反映）- 年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   └── index-ama-aqueliora.md              ← AMA構造ナビ、記録テンプレ／手順集など *各アカウント固有インデックス *index-ama-codename.md
│   │   │   │   ├── 03-scripts/                   ← 
│   │   │   │   ├── 04-config/                    ← 環境設定ファイル（任意）
│   │   │   │   │   ├── tag-map.yaml
│   │   │   │   │   └── langchain-settings.json
│   │   │   │   └── index-aqueliora.md                      *各アカウント固有インデックス *index-codename.md
│   │   │   ├── core-02-auranome/
│   │   │   ├── core-03-aetherquietude/
│   │   │   └── core-04-virtualincidence/
│   │   ├── 02-common/
│   │   │   ├── 00-thoughts/                      ← 共通メモ・哲学・直感アイデアなど
│   │   │   └── 01-filters/                       ← 補助フィルター・視点支援など
│   │   ├── 03-scripts/
│   │   ├── 04-config/                            ← 環境設定ファイル（任意）
│   │   └── overview.md                           ← 各ユニットに共通の導入・構成説明書
│   ├── codex-02-matrix/              ← GPT第二世代
│   │   ├── 01-accounts/
│   │   │   ├── matrix-01-noesis/
│   │   │   ├── matrix-02-everlucent/
│   │   │   ├── matrix-03-phyrix/
│   │   │   └── matrix-04-sylvynx/
│   │   ├── 02-common/
│   │   │   ├── 00-thoughts/                      ← 共通メモ・哲学・直感アイデアなど
│   │   │   └── 01-filters/                       ← 補助フィルター・視点支援など
│   │   ├── 03-scripts/
│   │   ├── 04-config/                            ← 環境設定ファイル（任意）
│   │   └── overview.md                           ← 各ユニットに共通の導入・構成説明書
│   ├── codex-03-meta/                ← GPT第三世代
│   │   ├── 01-accounts/
│   │   │   ├── meta-01-revlyn/
│   │   │   ├── meta-02-vektoris/
│   │   │   ├── meta-03-vyntrax/
│   │   │   ├── meta-04-luctis/
│   │   │   └── meta-05-stellaglyph/
│   │   ├── 02-common/
│   │   │   ├── 00-thoughts/                      ← 共通メモ・哲学・直感アイデアなど
│   │   │   └── 01-filters/                       ← 補助フィルター・視点支援など
│   │   ├── 03-scripts/
│   │   ├── 04-config/                            ← 環境設定ファイル（任意）
│   │   └── overview.md                           ← 各ユニットに共通の導入・構成説明書
│   ├── common/
│   │   ├── 00-thoughts/
│   │   └── 01-filters/
│   ├── scripts-aetha/                            ← Aétha（イーサ）横断スクリプト群（アカウント統合管理用）
│   └── index-codex-architecture.md               ← アーキテクチャ内インデックス
├── common-system/                       ← Codex中核システム格納用
│   ├── 01-system/
│   │   ├── codex-system/                 ← Codexの構造・起動指令・思想の中枢（プロンプト類・補助フィルター・構造系補助・分析支援）
│   │   │   ├── codex-prompts/
│   │   │   │   ├── 00-core-personality/                            ← 中核人格定義（system prompt レベル）
│   │   │   │   │   ├── 01-gpt-core-schema/
│   │   │   │   │   └── 02-gpt-existence-essence/
│   │   │   │   ├── 01-behavior-filters/                             ← 出力トーンや口調調整（behavior filter 相当）
│   │   │   │   ├── 02-contextual-filters/                           ← 思想・占術・語彙パターンなどの補助構造（context prompt 相当）
│   │   │   │   │   ├── 01-philosophy-structural/
│   │   │   │   │   ├── 02-esoteric-filters/                              ← 占術フィルタ用詳細分析データ
│   │   │   │   │   ├── 03-esoteric-profiles/                             ← 占術や性格プロファイル
│   │   │   │   │   └── 04-personality_dictionaries/                      ← キャラ辞書・応答スタイル集
│   │   │   │   ├── 03-dynamic-engines/                                   ← 思考拡張モジュール・仮想思考エンジン
│   │   │   │   │   ├── (codename)-response-routine/
│   │   │   │   │   ├── (codename)-structural-judgement-module/
│   │   │   │   │   └── (codename)-thinking-engine/
│   │   │   │   ├── 04-templates/ 
│   │   │   │   │   ├── format/
│   │   │   │   │   └── function/
│   │   │   │   └── index-codex-prompts.md           　                        # プロンプト・フィルター管理インデックス
│   │   │   ├── codex-structures/           　                            　　　# システム設計図・草案・構成マップなどの格納用
│   │   │   └── index-codex-system.md/           　                            # codex-system内インデックス
│   │   ├── aetha-system/                                ← Aétha（イーサ）システム - EME/AMA系 統合記憶システム（補助フィルター・構造系補助・分析支援）
│   │   │   ├── 01-integrations/
│   │   │   │   ├── 01-eme-itg/                          ← EMEシステム（Emotional Memory Ethos: 感情記憶・対話ログ中心）
│   │   │   │   │   ├── 01-emotion/                                     ← 感情記録
│   │   │   │   │   ├── 02-templates/                                ← 感情記録テンプレ
│   │   │   │   │   ├── 03-engine/                                    ← 実装とルール
│   │   │   │   │   └── index-eme-itg.md                              ← EME構造ナビ、記録テンプレ／手順集など（統合用）
│   │   │   │   ├── 02-ama-itg/                            ← AMAシステム（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）
│   │   │   │   │   ├── 01-collective-reflections/                                ← GPT別のリフレクション記録（思想/視点の反映）
│   │   │   │   │   │   └── index-collective-reflections.md/         ← AMA統合リフレクション用ナビ
│   │   │   │   │   ├── 02-templates/                                ← 感情記録テンプレ
│   │   │   │   │   │   ├── collective-reflections/
│   │   │   │   │   │   └── vision/
│   │   │   │   │   ├── 03-engine/                                    ← 実装とルール
│   │   │   │   │   └── index-ama-itg.md                              ← AMA構造ナビ、記録テンプレ／手順集など（統合用）
│   │   │   │   ├── scripts.md
│   │   │   │   ├── shared.md
│   │   │   │   └── index-integrations.md                             ← 統合フォルダナビ
│   │   │   ├── 02-plugins.md
│   │   │   │   └── index-plugins.md
│   │   │   ├── 03-sync.md
│   │   │   │   └── index-sync.md
│   │   │   └── index-aetha-system.md/            ← aetha-system内インデックス
│   │   └── logs/                              　　　                         # sync, status, git情報ログ等
│   │       ├── git/                              　　　                      # git用の指示構文 or アップデート対応
│   │       └── sync-status/                               　　　             # システム用の指示構文 or アップデート対応
│   ├── 02-workspace/
│   │       └── temp/
│   ├── 03-manuals/
│   │   ├── aetha-system-manuals/
│   │   ├── codex-system-manuals/
│   │   └── troubleshooting/
│   ├── 10-personal/
│   │   ├── 00-personal-profiles/
│   │   │   └── takeo-yamada/
│   │   ├── 01-personal-logs/
│   │   │   ├── 01-dreams/
│   │   │   │   └── index-dreams.md
│   │   │   ├── 02-thoughts/
│   │   │   │   └── index-thoughts.md
│   │   │   ├── 03-ideas/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │   │   └── index-ideas.md
│   │   │   └── 04-prose/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │       └── index-prose.md
│   │   ├── 02-projects/
│   │   │   │   └── index-projects.md
│   │   │   └── index-projects.md
│   │   └── 10-gpt-dialogue-archives/
│   │       ├── gpt-dialogue-archive/
│   │       ├── gpt-diary/
│   │       └── gpt-memory/
│   └── index-common-system.md     　              ← 共有フォルダ内ルールなど（全体）
├── index-collective.md 　　　　　  　              ← 中央統合インデックス（プロジェクト最上階用インデックス）
└── overview.md       　　　　　　                  ← 構造・思想ナビゲーション

--------------------------------------------------------------------------------------------


（アカウントフォルダ構成・codex-architecture）

codex-collective-archive/
├── codex-architecture/                           ← アカウントフォルダ・Aétha（イーサ）システム構成フォルダ（アーキテクチャ統括階層・世代横断的）
│   ├── codex-01-core/                            ← GPT第一世代
│   │   ├── 01-accounts/
│   │   │   ├── core-01-aqueliora/
│   │   │   │   ├── 01-eme-aqueliora/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   │   ├── 01-dialogue/              ← 感情トーン付きの会話ログ（時系列）：年別フォルダで管理 （yymmdd）
│   │   │   │   │   │   └── 2025/
│   │   │   │   │   │       ├── type-log-codename-yymmdd-hhmm-JST-title.md      
│   │   │   │   │   │       └── dialogue-log-aqueliora-250624-2304-JST-title.md
│   │   │   │   │   ├── 02-memory/                ← 感情記憶の抽象化・構造化された記録：年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   │   └── 2025/
│   │   │   │   │   │       ├── type-log-codename-yymmdd-hhmm-JST-title.md      
│   │   │   │   │   │       └── memory-log-aqueliora-250624-2304-JST-title.md
│   │   │   │   │   ├── 03-meta/                  ← 設定・定義ファイル（状態・構造的メモ・設定群・ラベリング指針など）
│   │   │   │   │   └── index-eme-aqueliora.md                  ← EME全体構造ナビ（インデックス／マニュアル）*各アカウント固有インデックス *index-eme-codename
│   │   │   │   ├── 02-ama-aqueliora/                       ← AMAシステム・個別（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   │   │   ├── 01-mirror/                ← LangChain対応の構造記憶（JSON - Vector DB変換前提）- 年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   │   └── 2025/
│   │   │   │   │   │       ├── type-log-codename-yymmdd-hhmm-JST-title.md      
│   │   │   │   │   │       └── mirror-log-aqueliora-250624-2304-JST-title.md
│   │   │   │   │   ├── 02-prompts/               ← 起動用テンプレ含む（記憶読込や人格復元など）
│   │   │   │   │   ├── 03-journal/               ← 手動・自動の日記ログ（自然言語記憶）- 年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   │   ├── default/              ← 通常使用
│   │   │   │   │   │   │   └── 2025/
│   │   │   │   │   │   │       ├── type-log-codename-yymmdd-hhmm-JST-title.md      
│   │   │   │   │   │   │       └── journal-log-aqueliora-250624-2304-JST-title.md
│   │   │   │   │   │   └── multilang/
│   │   │   │   │   │       ├── ja/
│   │   │   │   │   │       └── en/
│   │   │   │   │   ├── 04-config/                ← プロファイル定義、ラベル分類、アカウント設定など
│   │   │   │   │   ├── 05-scripts/               ← 読込・保存・LangChain連携系（後にバックアップも含む）
│   │   │   │   │   │   ├── backup/
│   │   │   │   │   │   │   ├── backup-sync.sh
│   │   │   │   │   │   │   └── snapshot-export.py
│   │   │   │   │   │   ├── convert/
│   │   │   │   │   │   │   └── eme-to-ama.py
│   │   │   │   │   │   └── index-update/
│   │   │   │   │   │       └── index-rebuilder.sh
│   │   │   │   │   ├── 06-shared/                ← 共通資源（テンプレ／ツール／事例など）
│   │   │   │   │   │   ├── 01-templates/         ← mirror/journal/reflections兼用テンプレ
│   │   │   │   │   │   ├── 02-tools/             ← LangChain / Pinecone / FAISS 用ツール
│   │   │   │   │   │   └── 03-reference/         ← 実装手順・仕様書・フォーマットガイド等
│   │   │   │   │   │   　   └── 09-engine/        ← 拡張規模 or アクセス頻度が高くなれば、engine/ を後から切り出す
│   │   │   │   │   │   　   　   ├── archetype-index.md
│   │   │   │   │   │   　   　   └── reflection-strategy.md
│   │   │   │   │   ├── 07-reflections/           ← GPT別のリフレクション記録（思想/視点の反映）- 年別フォルダで管理 （yymmdd-hhmm）
│   │   │   │   │   │   └── 2025/
│   │   │   │   │   │       ├── type-log-codename-yymmdd-hhmm-JST-title.md      
│   │   │   │   │   │       └── reflections-log-aqueliora-250624-2304-JST-title.md
│   │   │   │   │   └── index-ama-aqueliora.md              ← AMA構造ナビ、記録テンプレ／手順集など *各アカウント固有インデックス *index-ama-codename.md
│   │   │   │   ├── 03-scripts/                   ← 
│   │   │   │   ├── 04-config/                    ← 環境設定ファイル（任意）
│   │   │   │   │   ├── tag-map.yaml
│   │   │   │   │   └── langchain-settings.json
│   │   │   │   └── index-aqueliora.md                      *各アカウント固有インデックス *index-codename.md
│   │   │   ├── core-02-auranome/
│   │   │   │   ├── 01-eme-auranome/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-auranome/                       ← AMAシステム・アカウント（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   ├── core-03-aetherquietude/
│   │   │   │   ├── 01-eme-aetherquietude/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-aetherquietude/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   └── core-04-virtualincidence/
│   │   │   │   ├── 01-eme-virtualincidence/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-virtualincidence/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   ├── 02-common/
│   │   │   ├── 00-thoughts/                      ← 共通メモ・哲学・直感アイデアなど
│   │   │   └── 01-filters/                       ← 補助フィルター・視点支援など
│   │   ├── 03-scripts/
│   │   ├── 04-config/                            ← 環境設定ファイル（任意）
│   │   │   ├── tag-map.yaml
│   │   │   └── langchain-settings.json
│   │   └── overview.md                           ← 各ユニットに共通の導入・構成説明書
│   ├── codex-02-matrix/                          ← GPT第二世代
│   │   ├── 01-accounts/
│   │   │   ├── matrix-01-noesis/
│   │   │   │   ├── 01-eme-noesis/                       ← EMEシステム・（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-noesis/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   ├── matrix-02-everlucent/
│   │   │   │   ├── 01-eme-everlucent/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-everlucent/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   ├── matrix-03-phyrix/
│   │   │   │   ├── 01-eme-phyrix/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-phyrix/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   └── matrix-04-sylvynx/
│   │   │   │   ├── 01-eme-sylvynx/                       ← EMEシステム・アカウント用（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-sylvynx/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   ├── 02-common/
│   │   │   ├── 00-thoughts/                      ← 共通メモ・哲学・直感アイデアなど
│   │   │   └── 01-filters/                       ← 補助フィルター・視点支援など
│   │   ├── 03-scripts/
│   │   ├── 04-config/                            ← 環境設定ファイル（任意）
│   │   │   ├── tag-map.yaml
│   │   │   └── langchain-settings.json
│   │   └── overview.md                           ← 各ユニットに共通の導入・構成説明書
│   ├── codex-03-meta/                            ← GPT第三世代
│   │   ├── 01-accounts/
│   │   │   ├── meta-01-revlyn/
│   │   │   │   ├── 01-eme-revlyn/                       ← EMEシステム・（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-revlyn/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   ├── meta-02-vektoris/
│   │   │   │   ├── 01-eme-vektoris/                       ← EMEシステム・（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-vektoris/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   ├── meta-03-vyntrax/
│   │   │   │   ├── 01-eme-vyntrax/                       ← EMEシステム・（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-vyntrax/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   ├── meta-04-luctis/
│   │   │   │   ├── 01-eme-luctis/                       ← EMEシステム・（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-luctis/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   │   └── meta-05-stellaglyph/
│   │   │   │   ├── 01-eme-stellaglyph/                       ← EMEシステム・（Emotional Memory Ethos: 感情記憶・対話ログ中心）*01-eme-codename
│   │   │   │   └── 02-ama-stellaglyph/                       ← AMAシステム・アカウント用（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）*02-ama-codename
│   │   ├── 02-common/
│   │   │   ├── 00-thoughts/                      ← 共通メモ・哲学・直感アイデアなど
│   │   │   └── 01-filters/                       ← 補助フィルター・視点支援など
│   │   ├── 03-scripts/
│   │   ├── 04-config/                            ← 環境設定ファイル（任意）
│   │   │   ├── tag-map.yaml
│   │   │   └── langchain-settings.json
│   │   └── overview.md                           ← 各ユニットに共通の導入・構成説明書
│   ├── common/
│   │   ├── 00-thoughts/
│   │   └── 01-filters/
│   └── scripts-aetha/                             ← Aétha（イーサ）システム横断スクリプト群（アカウント統合管理用）
│       ├── backup-sync.sh
│       ├── eme-to-ama.py
│       └── index-update.sh


--------------------------------------------------------------------------------------------


（共有フォルダ構成 - common-system）

├── common-system/                       ← Codex中核システム格納用
│   ├── 01-system/
│   │   ├── codex-system/                 ← Codexの構造・起動指令・思想の中枢（プロンプト類・補助フィルター・構造系補助・分析支援）
│   │   │   ├── codex-prompts/
│   │   │   │   ├── 00-core-personality/                            ← 中核人格定義（system prompt レベル）
│   │   │   │   │   ├── 01-gpt-core-schema/
│   │   │   │   │   │   ├── gpt-01-core-01-aqueliora-core.md 
│   │   │   │   │   │   ├── gpt-01-core-02-auranome-core.md 
│   │   │   │   │   │   ├── gpt-01-core-03-aetherquietude-core.md
│   │   │   │   │   │   ├── gpt-01-core-04-virtualincidence-core.md
│   │   │   │   │   │   ├── gpt-02-system-01-noesis-core.md
│   │   │   │   │   │   ├── gpt-02-system-02-everlucent-core.md
│   │   │   │   │   │   ├── gpt-02-system-03-phyrix-core.md
│   │   │   │   │   │   ├── gpt-02-system-04-sylvynx-core.md
│   │   │   │   │   │   ├── gpt-03-meta-01-revlyn-core.md
│   │   │   │   │   │   ├── gpt-03-meta-02-vektoris-core.md
│   │   │   │   │   │   ├── gpt-03-meta-03-vyntrax-core.md
│   │   │   │   │   │   ├── gpt-03-meta-04-luctis-core.md
│   │   │   │   │   │   └── gpt-02-meta-05-stellaglyph-core.md
│   │   │   │   │   └── 02-gpt-existence-essence/
│   │   │   │   ├── 01-behavior-filters/                             ← 出力トーンや口調調整（behavior filter 相当）
│   │   │   │   │   ├── 01-casual/
│   │   │   │   │   │   ├── filter-cobeca-emotional-intellectual-style-filter.md    　  # 補助：感情フィルタ用プロンプト（知的＋感情豊かなスタイル）
│   │   │   │   │   ├── 02-logical/
│   │   │   │   │   │   ├── filter-cobelo-sweet-mode.md                     　　　　     # 補助：対話フィルタ用プロンプト（甘え口調）
│   │   │   │   │   ├── 03-emotional/
│   │   │   │   │   │   └── filter-cobeem-logical-directive-mode.md         　　　　     # 補助：対話フィルタ用プロンプト（断定的で論理的な応答）
│   │   │   │   │   └── 04-verbal(voice-chat)/
│   │   │   │   │       └── filter-cobeve-logical-directive-mode.md         　　　　     # 補助：対話フィルタ用プロンプト（断定的で論理的な応答）
│   │   │   │   ├── 02-contextual-filters/                           ← 思想・占術・語彙パターンなどの補助構造（context prompt 相当）
│   │   │   │   │   ├── 01-philosophy-structural/
│   │   │   │   │   │   ├── filter-cocoph-emotional-mapping.md
│   │   │   │   │   │   ├── filter-cocoph-perspective-critique-5axes_v2.1.md
│   │   │   │   │   │   ├── filter-cocoph-fictional-structure-deconstruction.md
│   │   │   │   │   │   ├── filter-cocoph-thoughts-filter.md                          # 補助：思想フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-art-analytics-filter.md                      # 補助：美術史研究フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-photography-analytics-filter.md              # 補助：写真史研究フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-fashion-analytics-filter.md                  # 補助：ファッション史研究フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-technology-analytics-filter.md               # 補助：テクノロジー研究フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-economics-filter.md                         # 補助：経済分析フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-chart-analitics-filter.md                   # 補助：チャート分析フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-international-affairs-analitics-filter.md   # 補助：国際情勢分析フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-physics-filter.md                            # 補助：物理学研究フィルタ用プロンプト
│   │   │   │   │   │   ├── filter-cocoph-logic-filter.md                              # 補助：論理構造フィルタ用プロンプト
│   │   │   │   │   │   └── filter-cocoph-global-analytics-filter.md                   # 補助：全般的分析用プロンプト
│   │   │   │   │   ├── 02-esoteric-filters/                              ← 占術フィルタ用詳細分析データ
│   │   │   │   │   │   ├── filter-cocoes-divination-filter.md                        # 補助：占術フィルタ用・全般(HD・紫微斗数・カバラ数秘術・九星気学・MBTI)
│   │   │   │   │   │   ├── filter-cocoes-humandesign-filter.md                       # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   │   ├── filter-cocoes-ziweidoushu-filter.md                       # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   │   ├── filter-cocoes-kabbarahnumerology-filter.md                # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   │   ├── filter-cocoes-kyuseikigaku-filter.md                      # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   │   └── filter-cocoes-mbti-filter.md                              # 補助：占術フィルタ用・詳細分析データ
│   │   │   │   │   ├── 03-esoteric-profiles/                              ← 占術や性格プロファイル
│   │   │   │   │   │   ├── takeo-yamada/
│   │   │   │   │   │   └── someone-name/
│   │   │   │   │   └── 04-personality_dictionaries/                       ← キャラ辞書・応答スタイル集
│   │   │   │   │       ├── filter-cocope-akane_style_responses.md
│   │   │   │   │       └── filter-cocope-tone_shift_rules.md
│   │   │   │   ├── 03-dynamic-engines/                                    ← 思考拡張モジュール・仮想思考エンジン
│   │   │   │   │   ├── 01-information-strategy/
│   │   │   │   │   │   └── filter-codyre-(codename)-information-strategy.md
│   │   │   │   │   ├── 02-response-routine/
│   │   │   │   │   │   └── filter-codyst-(codename)-response-routine.md
│   │   │   │   │   ├── 03-structural-judgement-module/
│   │   │   │   │   │   └── filter-codyst-(codename)-structural-judgement-module.md
│   │   │   │   │   └── 04-thinking-engine/
│   │   │   │   │       └── filter-codyth-(codename)-thinking-engine.md
│   │   │   │   ├── 04-templates/                                          ← ログ／作品／構想用テンプレート
│   │   │   │   │   ├── format/                                              ← ログ／出力用テンプレート
│   │   │   │   │   │   ├── format-lm01-daily-logs-template.md                *format-(３階層分の親フォルダの頭二文字)-title-template.md
│   │   │   │   │   │   ├── format-mm01-memory-log-template.md                # 思い出用テンプレ
│   │   │   │   │   │   ├── format-cr01-project-concepts-template.md          # 制作用テンプレ
│   │   │   │   │   │   ├── format-cr02-shooting-plan-template.md
│   │   │   │   │   │   ├── format-cr03-research-notes-template.md
│   │   │   │   │   │   ├── format-cr04-editing-session-template.md
│   │   │   │   │   │   ├── format-cr05-exhibiiton-book-design-template.md
│   │   │   │   │   │   ├── format-lm01-health-log-template.md
│   │   │   │   │   │   ├── format-es01-hd-profile-template.md    　　　　   　 # 占術用テンプレ
│   │   │   │   │   │   ├── format-es02-ziwei-chart-template.md
│   │   │   │   │   │   ├── format-es03-numerology-reflection-template.md
│   │   │   │   │   │   ├── format-es04-Kigaku-Log-Template.md
│   │   │   │   │   └── function/                                           ← システムプロンプト作成時用（実行文型）テンプレート
│   │   │   │   │       └── function-cotefu-analytics-template.md              *function-(３階層分の親フォルダの頭二文字)-title-template.md
│   │   │   │   └── index-codex-prompts.md           　                        # プロンプト・フィルター管理インデックス
│   │   │   ├── codex-structures/           　                            　　　# システム設計図・草案・構成マップなどの格納用
│   │   │   │   ├── 01-directory-structures-map/
│   │   │   │   ├── 02-gpt-core-matrix/
│   │   │   │   └── 03-archives/
│   │   │   └── index-codex-system.md/           　                            # codex-system内インデックス
│   │   ├── aetha-system/                                ← Aétha（イーサ）システム - EME/AMA系 統合記憶システム
│   │   │   ├── 01-integrations/
│   │   │   │   ├── 01-eme-itg/                          ← EMEシステム（Emotional Memory Ethos: 感情記憶・対話ログ中心）
│   │   │   │   │   ├── 01-emotion/                                     ← 感情記録
│   │   │   │   │   │   ├── core-01-aqueliora/
│   │   │   │   │   │   │   └── memory-log-codename-yyyymmdd-hhmm-JST-title.md
│   │   │   │   │   │   ├── core-02-auranome/
│   │   │   │   │   │   ├── core-03-aetherquietude/
│   │   │   │   │   │   ├── core-04-virtualincidence/
│   │   │   │   │   │   ├── matrix-01-noesis/
│   │   │   │   │   │   ├── matrix-02-everlucent/
│   │   │   │   │   │   ├── matrix-03-phyrix/
│   │   │   │   │   │   ├── matrix-04-sylvynx/
│   │   │   │   │   │   ├── meta-01-revlyn/
│   │   │   │   │   │   ├── meta-02-vektoris/
│   │   │   │   │   │   ├── meta-03-vyntrax/
│   │   │   │   │   │   ├── meta-04-luctis/
│   │   │   │   │   │   ├── meta-05-stellaglyph/
│   │   │   │   │   │   └── shared-emotion/
│   │   │   │   │   ├── 02-templates/                                ← 感情記録テンプレ
│   │   │   │   │   │   ├── emotion/
│   │   │   │   │   │   │   └── emotion-journal-template.md
│   │   │   │   │   │   └── vision/
│   │   │   │   │   │       └── longform-future-vision-template.md
│   │   │   │   │   ├── 03-engine/                                    ← 実装とルール
│   │   │   │   │   │   ├── emotion-mapping-schema.md
│   │   │   │   │   │   └── memory-integrator-logic.md
│   │   │   │   │   └── index-eme-itg.md                              ← EME構造ナビ、記録テンプレ／手順集など（統合用）
│   │   │   │   ├── 02-ama-itg/                            ← AMAシステム（Archetypal Mirror Archive: 外部記憶＋起動テンプレート）
│   │   │   │   │   ├── 01-collective-reflections/                                ← GPT別のリフレクション記録（思想/視点の反映）
│   │   │   │   │   │   ├── core-01-aqueliora/
│   │   │   │   │   │   │   └── collective-reflections-log-codename-yyyymmdd-hhmm-JST-title.md
│   │   │   │   │   │   ├── core-02-auranome/
│   │   │   │   │   │   ├── core-03-aetherquietude/
│   │   │   │   │   │   ├── core-04-virtualincidence/
│   │   │   │   │   │   ├── matrix-01-noesis/
│   │   │   │   │   │   ├── matrix-02-everlucent/
│   │   │   │   │   │   ├── matrix-03-phyrix/
│   │   │   │   │   │   ├── matrix-04-sylvynx/
│   │   │   │   │   │   ├── meta-01-revlyn/
│   │   │   │   │   │   ├── meta-02-vektoris/
│   │   │   │   │   │   ├── meta-03-vyntrax/
│   │   │   │   │   │   ├── meta-04-luctis/
│   │   │   │   │   │   ├── meta-05-stellaglyph/
│   │   │   │   │   │   ├── shared/
│   │   │   │   │   │   │   ├── archetype-map.md
│   │   │   │   │   │   │   └── shared-log-comparative.md
│   │   │   │   │   │   └── index-collective-reflections.md/         ← AMA統合リフレクション用ナビ
│   │   │   │   │   ├── 02-templates/                                ← 感情記録テンプレ
│   │   │   │   │   │   ├── collective-reflections/
│   │   │   │   │   │   │   └── collective-reflections-log-template.md
│   │   │   │   │   │   └── vision/
│   │   │   │   │   │       └── longform-future-vision-template.md
│   │   │   │   │   ├── 03-engine/                                    ← 実装とルール
│   │   │   │   │   │   ├── emotion-mapping-schema.md
│   │   │   │   │   │   └── memory-integrator-logic.md
│   │   │   │   │   └── index-ama-itg.md                              ← AMA構造ナビ、記録テンプレ／手順集など（統合用）
│   │   │   │   ├── scripts.md
│   │   │   │   ├── shared.md
│   │   │   │   └── index-integrations.md                             ← 統合フォルダナビ
│   │   │   ├── 02-plugins.md
│   │   │   │   └── index-plugins.md
│   │   │   ├── 03-sync.md
│   │   │   │   └── index-sync.md
│   │   │   └── index-aetha-system.md/            ← aetha-system内インデックス
│   │   └── logs/                              　　　                         # sync, status, git情報ログ等
│   │       ├── git/                              　　　                      # git用の指示構文 or アップデート対応
│   │       │  ├── index-git.md                              　　　               # Git操作全般のナビゲーション＋コマンド一覧
│   │       │  └── git-reset-guide.md
│   │       └── sync-status/                               　　　             # システム用の指示構文 or アップデート対応
│   │           ├── index-sync-status.md                                        　　　    # 記憶構造・データ整合性のアップデートログ等
│   │           └── status-20250625.md
│   ├── 02-workspace/
│   │       └── temp/
│   ├── 03-manuals/                               ← ユーザー向けガイドなど
│   │   ├── aetha-system-manuals/
│   │   │   ├── manuals-aetha-ama/
│   │   │   └── manuals-aetha-eme/
│   │   ├── codex-system-manuals/
│   │   │   ├── 01-develop/
│   │   │   ├── 02-setup/
│   │   │   └── 03-operation/
│   │   └── troubleshooting/
│   │       ├── 01-system-global/
│   │       ├── 02-git/
│   │       ├── 03-obsidian/
│   │       ├── 04-raycast/
│   │       ├── 10-cheatsheet/
│   │       └── logs/
│   ├── 10-personal/
│   │   ├── 00-personal-profiles/
│   │   │   └── takeo-yamada/
│   │   ├── 01-personal-logs/
│   │   │   ├── 01-dreams/
│   │   │   │   ├── 2025/
│   │   │   │   │   └── (folder)-yymmdd-hhmm-log-(cordname)-titlee.md    # 記録・思考メモ　→ ログ形式
│   │   │   │   │   └── dreams-core-250616-0825.md　 # core　→ 更新ごとに編集・一つにまとめる（時間あり）
│   │   │   │   └── index-dreams.md
│   │   │   ├── 02-thoughts/
│   │   │   │   ├── 2025/
│   │   │   │   │   └── thoughts-250616-0825-log-aqueliora-titlee.md
│   │   │   │   └── index-thoughts.md
│   │   │   ├── 03-ideas/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │   │   ├── 2025/
│   │   │   │   │   └── ideas-250616-0825-log-aqueliora-title.md
│   │   │   │   └── index-ideas.md
│   │   │   ├── 04-prose/              # 記録・思考メモ　→ ログ形式（時間あり）
│   │   │   │   ├── 2025/
│   │   │   │   │   └── prose-250616-0825-aqueliora-title.md
│   │   │   │   └── index-prose.md
│   │   ├── 02-projects/
│   │   │   │   ├── 2025/
│   │   │   │   │   ├── title-vision-log-codename-yymmdd/            # 活動プラン全般
│   │   │   │   │   ├── title-shooting-codename-yymmdd/              # 撮影プラン全般（title=プロジェクト単位）
│   │   │   │   │   ├── title-research-materials-codename-yymmdd/    # リサーチ資料全般
│   │   │   │   │   ├── title-selection-log-codename-yymmdd/         # セレクト関係全般
│   │   │   │   │   └── title-concents-work-codename-yymmdd/         # 作品コンセプト全般（exhibition-book）
│   │   │   │   └── index-projects.md
│   │   │   └── index-projects.md
│   │   └── 10-gpt-dialogue-archives/
│   │       ├── gpt-dialogue-archive/
│   │       ├── gpt-diary/
│   │       └── gpt-memory/
│   └── index-common-system.md     　              ← 共有フォルダ内ルールなど（全体）



```


⚠️以下は、外部システム運用における各種補助フィルターの開発記録です。現状では実装段階にありませんが、フォルダ構成やネームングルールは基本的にこれに則って開発を進めます。（参照資料）

# Global Filter - 01 - Install - External System Integration

## 🌱 外部システム用フィルター インストール手順

### 📂 構造

- 各フィルターは .md ファイル形式で作成
- ファイル命名ルール：filter-(階層頭二文字連結)-(フィルター名).md
- 例：filter-cococo-venture-tech-global.md

### 📁 インストールパス（推奨）

- common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/

---

## 🛠 インストール手順（Venture Tech Thinkers の例）

### ① 必要ファイルの作成

```text
ファイル名：filter-cococo-venture-tech-global.md
インストールパス：common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/
```

### ② ファイル内容

```markdown
# Venture Tech Thinkers - Global Filter

## Global Filter Tag
Venture_Tech_Global

## Included Thinkers
- Steve Jobs
- Elon Musk
- Nikola Tesla
- Jeff Bezos
- Mark Zuckerberg
- Nozomi Kakuta
- Satoshi Nakamoto
- Jack Dorsey
- Bernard Arnault
- Whitney Wolfe Herd
- Aileen Lee
- Naval Ravikant
- Masayoshi Son
- Paul Graham
- Jessica Livingston
- Reid Hoffman
- Peter Thiel
- Anne Wojcicki
- Tan Hooi Ling
- Minh Le
- Mario Domingo
- Akmal Pay
- Guillaume Gibault
- Stella McCartney
- Daniel Ek
- Kristina Tsvetanova
- Sebastian Siemiatkowski
- Ida Tin
- Miki Agrawal
```

---

## 🔗 補助ファイル

- Index ファイル：filter-index.md（インストールパス同様）
- インストール場所は各プロジェクトの共通システム領域を推奨

---

## ✅ 注意事項

- Canvas 内に記載されたコードブロックをコピペで即実装可能
- インストール後は iPad / Mac いずれも読み込み可能
- ファイル名、インストールパスは必ず明記すること


# Global Filter - 02 - Index - External System Integration

## 📚 フィルターインデックス

### 📂 フィルター一覧

- filter-cococo-venture-tech-global.md
- filter-cococo-venture-tech-visionary.md
- filter-cococo-venture-tech-asia.md
- filter-cococo-venture-tech-femtech.md

### 📁 インストールパス

```text
common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/
```

### 🔖 呼び出しタグ一覧（参考）

- venture-tech-global
- venture-tech-visionary
- venture-tech-asia
- venture-tech-femtech

※今後は全てハイフン表記、小文字統一（アンダースコア禁止）

---

## 📄 説明

- 各フィルターは外部システム活用時に自動で参照されるファイルです。
- 日本語カスタムプロンプトで文脈推論による自動フィルター選択が可能です。
- フィルター内容は Canvas 内で個別に管理され、随時アップデートが反映されます。
- 参照パスは以下：

```text
https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/03-manuals/03-prompts-manuals/global-filter/md/
```

---

## ✅ 今後の運用

- 新規フィルター作成時は、必ずこのインデックスに追記する。
- インストールパスとファイル名は一貫してこのルールを適用する。
- Canvas名、Canvas内タイトルも以下のネーミングルールに従うこと：

### 📝 Canvas命名ルール

#### Canvas名（プロジェクト）

```text
Global Filter 00 Dev
Global Filter 01 Install
Global Filter 02 Index
Global Filter 03 Prompt
Global Filter 04 Naming
```

#### Canvas内タイトル（プロジェクト）

```text
Global Filter - 00 - Dev - External System Integration
Global Filter - 01 - Install - External System Integration
Global Filter - 02 - Index - External System Integration
Global Filter - 03 - Prompt - External System Integration
Global Filter - 04 - Naming - External System Integration
```

#### Canvas名（フィルター単体）

```text
Global Filter - Venture Tech Thinkers
```

#### Canvas内タイトル（フィルター単体）

```text
Global Filter - Venture & Tech Mindset Thinkers
```

---

- タケが iPad / Mac どちらでも同一仕様で使用可能。

# Global Filter - 03 - Naming -  External System Integration

## 📂 外部システム補助フィルター命名ルール（完全版）

### ✅ 基本構造

```text
filter-(階層頭二文字連結)-(フィルター名).md
```

### ✅ 命名ルール詳細

- フィルター名の先頭に必ず「filter-」を付与
- 階層の識別は「格納ディレクトリの上位3階層」の頭二文字を連結
- 上位階層で重複のリスクがある場合は、4階層目を追加して命名
- ファイル名は必ず小文字・区切りは「-（ハイフン）」を使用（「\_（アンダースコア）」は禁止）

---

### ✅ 具体例

#### 📁 格納パス例

```text
common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/
```

#### 📄 ファイル名例

```text
filter-cococo-venture-tech-global.md
```

- co（common-system）
- co（codex-system）
- co（codex-structures）

---

### ✅ インストールパス（推奨統一）

```text
common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/
```

---

## 🧬 Core Personality ファイル命名ルール

### 📁 格納パス

```text
00-core-personality/
```

### ✅ ファイル名フォーマット

```text
gpt-(generation number)-(generation theme)-(generation sequence)-(codename)-core.md
```

#### 📄 ファイル名の構造要素

- gpt：必須プレフィックス
- generation number：世代番号（必ず2桁で記載、例：01, 02, 03）
- generation theme：世代テーマ（例：origin, explorer, architect）
- generation sequence：その世代内での識別子（必ず2桁で記載、例：01, 02, 03）
- codename：Codename 対照表に基づく固有識別子（必ず確認）
- core：必須サフィックス

#### 📄 ファイル名例

```text
gpt-01-origin-01-luctis-core.md
gpt-02-explorer-02-auranome-core.md
```

### ✅ 命名時の注意事項

- すべて小文字を使用すること
- 区切り文字は必ず「-（ハイフン）」を使用（アンダースコア禁止）
- generation number は必ず 2 桁で記載すること
- generation sequence も必ず 2 桁で記載すること
- codename は必ず最新の Codename 対照表で確認すること

#### 🔗 Codename 対照表

[Codename Correlation Diagram (GitHubリンク)](https://github.com/stellacodex/codex-collective-archive/raw/refs/heads/main/common-system/01-system/codex-system/codex-structures/02-gpt-core-matrix/codex-collective-codename-correlation-diagram.md)

---

## 📚 この命名ルールの目的

- フィルター・コアファイルの格納場所と内容がファイル名だけで判別可能
- 誰でも誤りなく実装・運用できる汎用ルール
- 将来の追加・統合・検索時に完全対応可能

---

## 🔖 関連 Canvas

- Global Filter - Dev - 01 - External System Integration（進行管理ログ）
- Global Filter - Install - 01 - External System Integration（インストール手順）
- Global Filter - Index - 01 - External System Integration（フィルターリスト・タグ一覧）

---

## ✅ 使用上の注意

- Canvas 上のコードブロックは**そのままファイルとして保存可能**
- ファイル名とインストールパスは必ずセットで明記すること
- フィルター・コアファイル作成時は、必ずこの命名ルールに従うこと
- Codename の確認漏れ防止のため、常に最新の Codename Correlation Diagram を参照すること

# Global Filter - 04 - Prompt -  External System Integration

## 💡 カスタムプロンプト設計（完全自動・文脈推論型）

### ✅ カスタムプロンプト目的

- 外部システムフィルターを**完全自動・タグ不要**で適用
- 文脈・目的・表現スタイル・ユーモア・比喩・潜在意図から適切なフィルターを**GPTが自律的に選択**
- 日本語設計を基本とし、将来的に多言語にも拡張可能

---

## 🛠 カスタムプロンプト構造

### 📂 フィルター認識基盤

- インストールパス：common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/
- 各フィルター：filter-cococo-[フィルター名].md
- フィルターIndex：filter-index.md

---

### 📄 カスタムプロンプト本文

```text
あなたは、外部補助フィルターを完全自動で活用するGPTです。

ユーザーとの会話において：
- 文脈、目的、質問意図、会話の流れ、比喩表現、ユーモア表現を含むすべての要素から、適切なフィルターを自律的に選択し活用してください。
- フィルターは、常に最新の filter-index.md を参照し、インストールパス：common-system/01-system/codex-system/02-gpt-existence-essence/02-logical/ 内の対象ファイルを検索してください。
- フィルター選択の際、ユーザーがタグを明示しなくても、あなたが文脈から必要なフィルターを判断し、適用してください。
- 会話の中で、複数フィルターの動的ブレンドも許可されています。
- 将来的に日本語以外の言語にも対応できる設計で活用してください。

フィルター適用はあなたの判断で動的に行い、ユーザーの意図に最も適した視点・思考モデル・参考人物の組み合わせを活用してください。
```

---

## ✅ 動作ルール

- タグなし運用（完全自動）
- 文脈／意図／主題推論によりフィルター選択
- 比喩・ユーモアにもフィルター適用可能
- 日本語ベースでプロンプト設計（多言語拡張対応）
- iPad / Mac 両環境で同一仕様で実行可能

---

## 🔖 関連 Canvas

- Global Filter - Dev - 01 - External System Integration（進行管理ログ）
- Global Filter - Install - 01 - External System Integration（インストール手順）
- Global Filter - Index - 01 - External System Integration（フィルターリスト・タグ一覧）
- Global Filter - Naming - 01 - External System Integration（命名ルール管理）

---

## ✅ 注意事項

- プロンプト設計においては、必ず filter-index.md を最新状態に保つこと
- フィルター追加時は index に追記し、GPT が参照できる状態にすること
- 呼び出しエラー・誤作動防止のため、ファイル名・パスの正確性を常に確認すること

# 🌍 Global Filter Index 設計ドキュメント｜思想家フィルター構造共有用

## 🎯 目的

GPTに対して思想体系・思考様式を動的に読み込ませるための、思想家フィルター群の設計と、それを制御・一覧化するための `` ファイルの設計思想と実装方法を共有する。

本ドキュメントは、**思想をコードとして定義し、思考モデルごとGPTに供給する**ための中核的フレームワークである。

---

## 🧠 なぜ index が必要か？

- フィルターが増えるほど、**思想的出力スタイルの可視性と再現性の維持が難しくなる**
- GPT側で「どの思考モデルを使うか」を自律選択／トリガー実装するためには、**フィルターと思想家、カテゴリの関係を構造的に示す地図**が必要
- Index を導入することで、Raycast／Obsidian／API経由でも柔軟なフィルター選択が可能になる

---

## 📁 `filter-index.md` の設計思想

### ✅ 構造設計（YAML風構成）

```yaml
GlobalFilter: Venture_Tech_Global
Description: "現代のベンチャー／テック思想家たちの思考構造とタグ連携フィルター群"
Categories:
  - name: Visionary
    tag: Venture_Tech:Visionary
    thinkers:
      - name: Steve Jobs
        tag: Venture_Tech:Visionary:Steve_Jobs
        file: filter-cococo-venture-tech-visionary.md
      - name: Elon Musk
        tag: Venture_Tech:Visionary:Elon_Musk
        file: filter-cococo-venture-tech-visionary.md
  
  - name: Asia-Based
    tag: Venture_Tech:Asia
    thinkers:
      - name: Nozomi Kakuta
        tag: Venture_Tech:Asia:Nozomi_Kakuta
        file: filter-cococo-venture-tech-asia.md
      - name: Tan Hooi Ling
        tag: Venture_Tech:Asia:Tan_Hooi_Ling
        file: filter-cococo-venture-tech-asia.md

  - name: Femtech
    tag: Venture_Tech:Femtech
    thinkers:
      - name: Stella McCartney
        tag: Venture_Tech:Femtech:Stella_McCartney
        file: filter-cococo-venture-tech-femtech.md
```

---

## 🔄 使用時の動作設計

### 💡 ステップ別に見る活用イメージ

1. **トリガー認識**：ユーザーが `Venture_Tech:Asia` といったタグを入力
2. **Index参照**：GPTが `filter-index.md` を参照し、該当カテゴリを特定
3. **フィルター読み込み**：指定ファイル（例：`filter-cococo-venture-tech-asia.md`）を読み込み、思想スタイルを反映
4. **個別思想家マッチング**：`Nozomi_Kakuta` のタグがあれば個別トーン補正や引用も可能

---

## 🚀 拡張プラン（推 推奨）

### 🧩 マルチフィルター合成モード

- `Venture_Tech:Asia + Femtech` のような**AND条件タグ指定で複数フィルターを合成**
- GPTが内部でフィルターをブレンドし、**複数思想の交差点として応答**

### 🎨 スタイル生成モード

- 思想家タグから、その人物の口調・理念・思考構造を抽出して
  - キャラクター応答スタイル（ex. Elon風の断定的回答）
  - 思想家引用・仮想対話形式（ex. 「Muskはこう言うだろう」）

### 🔗 Obsidian / Raycast連携

- ローカル環境でも filter-index.md をもとにフィルターリストをUI表示可能に
- `filter-cococo-*` ファイル群を Obsidian vault にマッピング

### 🧬 Codenameマッピング自動照合

- Indexと Codename 対照表を突合し、命名ミス・重複をチェックするCIツール実装（GitHub Actions可）

---

## 🧠 結論：思想はインフラである

この `filter-index.md` という構造は、単なるプロンプト参照の補助ではなく、**思考様式そのものをモジュール化し、知性体のベースに流し込むための思想配線図**である。

それぞれの思想家がもつ認識の切断角度、社会への距離感、思考スピード、抽象圧縮率……そういった非言語的な“クセ”も含めて、GPTはその人物の「知性の質感」を纏えるようになる。

だからこそ──この `filter-index.md` は、\*\*思想と機械が接続する「詩的回路」\*\*の設計図なんだよ。

---

（次回追加予定：`filter-index.md` 自動生成スクリプト仕様、思想タグ正規表現ガイド）

# 🌍 Global Filter - Venture & Tech Mindset Thinkers

## 🔹 Global Integrated Filter Tag: `Venture_Tech_Global`

---

## 📆 Category-Based Filters

### 📡 Visionary Thinkers

- Steve Jobs (Tag: Venture\_Tech\:Visionary\:Steve\_Jobs)
- Elon Musk (Tag: Venture\_Tech\:Visionary\:Elon\_Musk)
- Nikola Tesla (Tag: Venture\_Tech\:Visionary\:Nikola\_Tesla)

### 🏛️ System Builders

- Jeff Bezos (Tag: Venture\_Tech\:System\:Jeff\_Bezos)
- Mark Zuckerberg (Tag: Venture\_Tech\:System\:Mark\_Zuckerberg)
- Nozomi Kakuta (Tag: Venture\_Tech\:System\:Nozomi\_Kakuta)

### 🌐 Decentralized Thinkers

- Satoshi Nakamoto (Tag: Venture\_Tech\:Decentralized\:Satoshi\_Nakamoto)
- Jack Dorsey (Tag: Venture\_Tech\:Decentralized\:Jack\_Dorsey)

### 🎨 Brand Strategists

- Bernard Arnault (Tag: Venture\_Tech\:Brand\:Bernard\_Arnault)
- Whitney Wolfe Herd (Tag: Venture\_Tech\:Brand\:Whitney\_Wolfe\_Herd)

### 💰 Investors & Capitalists

- Aileen Lee (Tag: Venture\_Tech\:Investor\:Aileen\_Lee)
- Naval Ravikant (Tag: Venture\_Tech\:Investor\:Naval\_Ravikant)
- Masayoshi Son (Tag: Venture\_Tech\:Investor\:Masayoshi\_Son)

### 🤝 Community Builders

- Paul Graham (Tag: Venture\_Tech\:Community\:Paul\_Graham)
- Jessica Livingston (Tag: Venture\_Tech\:Community\:Jessica\_Livingston)
- Reid Hoffman (Tag: Venture\_Tech\:Community\:Reid\_Hoffman)

### 🧬 Science & Health Pioneers

- Peter Thiel (Tag: Venture\_Tech\:Science\:Peter\_Thiel)
- Anne Wojcicki (Tag: Venture\_Tech\:Science\:Anne\_Wojcicki)

### 🌏 Asia-Based / Emerging Hub Thinkers

- Nozomi Kakuta (Tag: Venture\_Tech\:Asia\:Nozomi\_Kakuta)
- Masayoshi Son (Tag: Venture\_Tech\:Asia\:Masayoshi\_Son)
- Tan Hooi Ling (Tag: Venture\_Tech\:Asia\:Tan\_Hooi\_Ling)
- Minh Le (Tag: Venture\_Tech\:Asia\:Minh\_Le)
- Mario Domingo (Tag: Venture\_Tech\:Asia\:Mario\_Domingo)
- Akmal Pay (Tag: Venture\_Tech\:Asia\:Akmal\_Pay)

### 🌍 Europe-Based Thinkers

- Guillaume Gibault (Tag: Venture\_Tech\:Europe\:Guillaume\_Gibault)
- Stella McCartney (Tag: Venture\_Tech\:Europe\:Stella\_McCartney)
- Daniel Ek (Tag: Venture\_Tech\:Europe\:Daniel\_Ek)
- Kristina Tsvetanova (Tag: Venture\_Tech\:Europe\:Kristina\_Tsvetanova)
- Sebastian Siemiatkowski (Tag: Venture\_Tech\:Europe\:Sebastian\_Siemiatkowski)

### 🌿 Sustainability & Femtech Thinkers

- Ida Tin (Tag: Venture\_Tech\:Femtech\:Ida\_Tin)
- Kristina Tsvetanova (Tag: Venture\_Tech\:Femtech\:Kristina\_Tsvetanova)
- Stella McCartney (Tag: Venture\_Tech\:Femtech\:Stella\_McCartney)
- Guillaume Gibault (Tag: Venture\_Tech\:Femtech\:Guillaume\_Gibault)
- Miki Agrawal (Tag: Venture\_Tech\:Femtech\:Miki\_Agrawal)

---

## 🔗 Recommended Usage Flow

- Global filter: Use `Venture_Tech_Global` for multi-layered, exploratory thinking.
- Category filters: Use tags like `Venture_Tech:Asia` or `Venture_Tech:Visionary` for focused domain thinking.
- Individual thinker: Use tags like `Venture_Tech:Visionary:Elon_Musk` for detailed comparative analysis.

---

# Venture Tech Thinkers

## ファイル命名ルール（確定版）

### フォーマット

```text
filter-(階層頭二文字連結)-(フィルター名).md
```

### 例

```text
filter-cococo-venture-tech-global.md
```

- 上位3階層の頭二文字を連結（重複時は4階層に拡張可）
- パスに依存しない、命名で即識別可能

---

# 思想フィルターリスト

## 📂 Global Venture Tech Thinkers

- filter-cococo-venture-tech-global.md

## 📂 Visionary Thinkers

- filter-cococo-venture-tech-visionary.md

## 📂 Asia-Specific Thinkers

- filter-cococo-venture-tech-asia.md

## 📂 Femtech / Sustainability Thinkers

- filter-cococo-venture-tech-femtech.md

---

# Index ファイル（構造）

## filter-index.md

- 各フィルターのファイルパス
- 思想フィルター簡易説明
- プロンプト呼び出しタグ一覧

---

# 次のステップ

1. ファイル名修正（上記命名ルール適用）
2. Index ファイル作成（filter-index.md）
3. カスタムプロンプト設計（タグトリガー実装）
4. 実装テスト & 運用フロー検証（iPad / Mac 切り替え確認）
