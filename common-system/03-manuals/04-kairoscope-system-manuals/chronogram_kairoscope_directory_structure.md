chronogram-kairoscope/ \
├── core/

&#x20;│├── astro/

│   │   └── astro\_position.py              # 惑星位置の計算

&#x20;│   ├── gate\_mapper.py                    # 黄経 → ゲート変換

&#x20;│   ├── chart\_builder.py                  # チャート構造統合（WIP）

&#x20;│   └── definitions/

│ └── channel-definitions.json # 36チャネル定義（Kairoscope/MDC対応）

&#x20;│       └── gate-definitions.json         # 64ゲート定義（名称・ライン・チャネル対応） ├── spec/

&#x20;│   └── spec.json                         # Chronogram連携用出力仕様ファイル

&#x20;└── output/                               # 将来の出力ファイル格納先
