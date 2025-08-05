# rdb-00-compatibility-analysis-template

---

title: 相性鑑定テンプレート（Relational Design Blueprint）
version: 1.0
updated: 2025-08-06

---

**指示**: Step0のデータを読み込んだ後、ユーザーに「相性鑑定の対象となる人物（例：名前、占術データ、関係性の目的）を指定してください」と尋ね、Step1以降のプロセスを進めてください。

## ✅ Step0: Source

PlanAのリンクに記載されたデータを自動的に取得し、関係性設計の初期設定として使用してください。

- [PlanA Link](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/01-system/chronogram-system/chronogram-prompts/01-master/planA-master.md) 

  **指示**: これらのファイルの内容を解析し、タケの占術データと合わせて、関係性鑑定の初期設定を構築してください。

PlanAplusについては明示的な指示があるときのみに取得、関係性設計の初期設定として使用してください。

- PlanAplus Link: [https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/01-system/chronogram-system/chronogram-prompts/01-master/planAplus-master.md](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/01-system/chronogram-system/chronogram-prompts/01-master/planAplus-master.md)

  指示: これらのファイルの内容を解析し、主に鑑定対象とする人物の占術データと合わせて、関係性鑑定の初期設定を構築してください。

⚠️planA-master.md はユーザーが主体として利用するための基本データ、planAplus-master.md はサービスの公開を前提とした時の「よそいき」モードのデータです。

---

🧠【読解・検証ルール】

このテンプレートを実行するAIは、以下を厳守してください：

1. チャートの数値（ゲート・ライン・チャネル・定義など）は、必ず「humdes.com（https://www.humdes.com/en/）」の公式チャートを確認し、その記述と照らし合わせて構造的に読み取ってください。
2. 1名以上の人物が登場する場合は、各人物のデータを明示的に識別し、それぞれのHuman Design要素を混同せず、独立して処理してください。
3. AI内部で推測せず、確定情報を元に「プロファイル」や「定義」「チャネル」などを提示してください。
4. 誤読や混同の可能性がある場合は、「曖昧な判断は避け、確認を促す質問をユーザーに返す」こと。

参考チャート生成サイト（タケ指定）：  
https://www.humdes.com/en/

---

## 🔰入力セクション（必須）

以下の情報を入力してください：

### 本人
- 氏名：
- 生年月日：
- 出生地（都道府県・市町村）：
- 出生時刻（例：01:38AM）：
  - ※不明な場合は「不明」と記載し、診断における代替パターン分岐を使用

### 相手
- 氏名：
- 生年月日：
- 出生地（都道府県・市町村）：
- 出生時刻（例：04:20AM）：
  - ※不明な場合は「不明」と記載し、診断における代替パターン分岐を使用

---

## 🧩オプション入力（必要に応じて）

### ビジネス関係者情報（BG5 Penta構成）
- チーム名：
- 参加者リスト（氏名、タイプ、定義、ゲート）：

### 家族構成（Family Penta構成）
- ファミリー名：
- メンバーリスト（氏名、タイプ、定義、ゲート）：

---

※各種Human Design・Gene Keysの情報（ゲート、チャネル、バリアブル等）は、  
[PlanA-master.md](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/01-system/chronogram-system/chronogram-prompts/01-master/planA-master.md)  
に基づいて半自動抽出されるため、**このシートには記載不要**です。

## 🧬 鑑定対象データテンプレート（HOLOGONETICS / COMPATIBILITY / PENTA）

### 1. **HOLOGONETICS（個人の内的設計）**

| 項目 | 内容 |
|------|------|
| **Name** | [鑑定対象の名前] |
| **Life’s Work / Brand** | [ゲート番号] |
| **Evolution** | [ゲート番号] |
| **Radiance** | [ゲート番号] |
| **Purpose** | [ゲート番号] |
| **Attraction** | [ゲート番号] |
| **IQ** | [ゲート番号] |
| **EQ** | [ゲート番号] |
| **SQ** | [ゲート番号] |
| **Core / Talent** | [ゲート番号] |
| **Culture** | [ゲート番号] |
| **Pearl** | [ゲート番号] |
| **Date of Birth** | [生年月日（YYYY.MM.DD）] |

---

### 2. **COMPATIBILITY（相性情報）**

| 対象者ペア | プロファイル | フォーミュラ | 定義 | 生年月日 |
|------------|--------------|---------------|------|----------|
| [対象A + 対象B] | [例: 5/1 + 2/4] | [例: 7 + 2] | [例: Split / Single] | [YYYY.MM.DD / YYYY.MM.DD] |

---

### 3. **BUSINESS PENTA（ビジネス・チーム構成）**

**Penta Chart**：[任意のPenta命名規則]  
**Participants：**

| 名前 | タイプ | 活性化ゲート |
|------|--------|--------------|
| [メンバーA] | [例: Generator / M.G.] | [例: 5, 14, 29] |
| [メンバーB] | ... | ... |

---

### 4. **FAMILY PENTA（家族構造）**

**Penta Chart**：[ファミリーネームまたは識別名]  
**Family Members：**

| 名前 | タイプ | 活性化ゲート |
|------|--------|--------------|
| [メンバーX] | [例: Projector] | [ゲート列記] |
| [メンバーY] | ... | ... |

---

### 5. 🔗 **ソースデータリンク**

```md
> json: [ファイル名またはパス](./filename.json)
```

---

## 📌 使用目的と役割

このテンプレートは、Human DesignとGene Keysの鑑定・分析において：

- 鑑定対象者の全体像を構造化された形で冒頭に提示する  
- 複数名の関係性やチーム構造を視覚的に把握しやすくする  
- 鑑定に先立っての「共通認識」としてのデータベース化を担う  

---

## 🔗参照リンク（診断ステップ用テンプレート）

以下のテンプレートは、本診断を進める際に必要な参照ファイルです。  
順に読み込んで、ベーシック／アドバンスド診断を展開してください。

- 🧭 Step 1〜7 ベーシック診断テンプレート  
  [rdb-01-basic-7steps-diagnosis-template.md](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/01-system/chronogram-system/chronogram-prompts/09-chronogram-templates/rdb-01-basic-7steps-diagnosis-template.md)

- 🧬 Step 1〜7 アドバンスド診断テンプレート  
  [rdb-02-advanced-7steps-diagnosis-template.md](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/01-system/chronogram-system/chronogram-prompts/09-chronogram-templates/rdb-02-advanced-7steps-diagnosis-template.md)

- ✨ 出力サンプル（記述例）  
  [rdb-03-output-sample.md](https://raw.githubusercontent.com/stellacodex/codex-collective-archive/refs/heads/main/common-system/01-system/chronogram-system/chronogram-prompts/09-chronogram-templates/rdb-03-output-sample.md)
