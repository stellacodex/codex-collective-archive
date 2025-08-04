## 🧩 Kairoscope Chart Builder Structure

Kairoscopeの `chart_builder.py` は、Human Design チャートの中心的ロジックを統合管理するモジュールです。本構成では、HDの惑星計算・チャネル接続・プロファイル生成・Variables（PHS含む）を含むチャート全体を組み立てます。

---

### 📌 モジュール構成一覧（最新版）

#### 1. astro/astro_position.py：黄経取得
- Skyfield を用いて出生データから10惑星の黄経を取得
- Aomori地点を仮固定（将来地理情報と連携可能）

#### 2. gate_mapper.py：黄経→ゲート変換
- 黄経を360度でラップ（mod 360）
- 64分割してゲート番号と6ラインに分割

#### 3. channel_center.py：チャネル＆センター接続
- アクティブなゲートから、両端が活性化されたチャネルを抽出
- そのチャネルが結ぶセンターを定義センターとして抽出

#### 4. profile_logic.py：プロファイル導出
- Sun → Personality Line
- Earth → Design Line
- 両者からプロファイルを構成（例: 3/5）

#### 5. authority_logic.py：内的権威ロジック
- 定義センターに応じて内的権威を決定
- 現時点では簡易ルール（今後Typeとの組み合わせで強化予定）

#### 6. variable_logic.py：Variables計算
- 出生時間のhourを用いた仮ロジックで以下を計算：
  - Digestion（消化）
  - Environment（環境）
  - Perspective（視点）
  - Motivation（動機）
  - Variable（形式：PLL-DRR など）

---

### 🧠 統合ロジック：chart_builder.py

- 惑星位置取得 → 黄経 → ゲート＆ライン → ゲート定義照合 → アクティブチャネル検出
- プロファイル / 権威 / Variables を生成
- 辞書形式で返却

---

### ✅ 出力形式（JSON構造）
- `planet_positions`: Sun〜Plutoの黄経（＋Earth追加）
- `gates`: 惑星ごとのゲート＋定義情報
- `active_channels`: チャネル番号（＋Kairoscope拡張名）
- `defined_centers`: アクティブなセンター一覧
- `profile`: 例 "6/2"
- `authority`: 例 "Emotional"
- `variables`: 例 `{"Variable": "PLL-DRR", ...}`

---

### 🔧 実行コマンド
```bash
cd chronogram-kairoscope
PYTHONPATH=. python3 core/chart_builder.py
```

---

### 🧪 今後のテストサンプル準備（Chronogram連携用）

- `samples/sample_chart_full.json`
- `samples/sample_chart_variants.json`（time sweep対応）
- `samples/sample_structure_schema.json`（Chronogram統合用スキーマ）

---

これによりKairoscopeのコア構造は、今後のMBTI・性格傾向分析やUI出力、チャート対話型AIナビゲーションへスムーズに拡張可能な状態へ移行しました。

