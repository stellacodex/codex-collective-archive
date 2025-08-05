
# rdb-00-compatibility-analysis-template

---

title: 相性鑑定テンプレート（Relational Design Blueprint）
version: 1.0
updated: 2025-08-06

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
