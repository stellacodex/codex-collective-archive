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
│   │   ├── 01-develop/
│   │   ├── 02-setup/
│   │   ├── 03-operation/
│   │   ├── 04-troubleshooting/
│   │   └── 10-cheatsheet/
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
│   │   ├── 01-develop/
│   │   ├── 02-setup/
│   │   ├── 03-operation/
│   │   │   └── manual.md
│   │   ├── 04-troubleshooting/
│   │   │   ├── 01-system-global/
│   │   │   ├── 02-git/
│   │   │   ├── 03-obsidian/
│   │   │   └── 04-raycast/
│   │   └── 10-cheatsheet/
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
│   ├── 03-manuals/
│   │   ├── 01-develop/
│   │   ├── 02-setup/
│   │   ├── 03-operation/
│   │   │   └── manual.md
│   │   ├── 04-troubleshooting/
│   │   │   ├── 01-system-global/
│   │   │   ├── 02-git/
│   │   │   ├── 03-obsidian/
│   │   │   └── 04-raycast/
│   │   └── 10-cheatsheet/
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