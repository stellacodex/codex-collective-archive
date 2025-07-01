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