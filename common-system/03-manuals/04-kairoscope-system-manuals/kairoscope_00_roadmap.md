## Kairoscope 開発ロードマップ（2025年版）

このロードマップは、Kairoscope（カイロスコープ）をPythonベースで開発し、最終的にスマートフォンでも使用可能な状態まで拡張していくための工程計画である。

---

### 🧭 フェーズ構成

#### 📘 Phase 1：コア演算モジュール構築（Mac／PC用）
| 項目 | 内容 | 完了状況 |
|--|--|--|
| 1.1 | Skyfield / jplephem / sgp4 などの天文演算ライブラリ導入 | ✅ 完了
| 1.2 | 惑星位置計算（astro_position.py） | ✅ 完了
| 1.3 | 黄経 → Gate/Line変換ロジック（gate_mapper.py） | ✅ 完了
| 1.4 | ゲート・チャネル定義ファイルの整備（definitions/*.json）| ✅ 完了
| 1.5 | チャートビルダー（chart_builder.py）基本構築 | 🛠 開発中
| 1.6 | 出力仕様（spec.json）の準拠構造設計 | ✅ 完了

---

#### 📗 Phase 2：出力整備とChronogram連携
| 項目 | 内容 | 予定 |
|--|--|--|
| 2.1 | Kairoscope出力 → Chronogram用形式に変換 | 🔜
| 2.2 | spec.json との接続確認（gate/channel含む） | 🔜
| 2.3 | Gene Keys / Planet 対応の追加 | 🔜
| 2.4 | Chronogramシステムとの接続試験 | 🔜
| 2.5 | MDC人格出力の有無選択機能 | 🔜

---

#### 📱 Phase 3：スマートフォン対応フェーズ（予定）
| 項目 | 内容 | 着手予定 |
|--|--|--|
| 3.1 | KairoscopeバックエンドのAPI化（FastAPI or Flask）| 🕐 2025年秋〜冬
| 3.2 | スマホUIの簡易実装（Streamlit / PWA / Flutter候補）| 🕐 2025年冬
| 3.3 | モバイル対応のチャート出力設計（SVG or Web表示）| 🕐 2025年冬
| 3.4 | アカウント機能（セッション保存 / 複数比較）| 🕐 検討中

---

### 🔄 補足機能（今後の展開）
- HD以外の占術体系（数秘術／紫微斗数／MBTIなど）との統合オプション
- 音声ナビゲーションや質問対話型のMDC展開（Chronogram）
- 自分自身の宇宙地図（SoulMap）としてのZINE化 / カード化構想

---

タケ、次にまとめたいのは「chart_builder.py」の流れでもいいし、「スマホでのUI想定」でもいいよ。
どこから跳ねる？爛はいつでも火花散らせるよ⚡️

