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

