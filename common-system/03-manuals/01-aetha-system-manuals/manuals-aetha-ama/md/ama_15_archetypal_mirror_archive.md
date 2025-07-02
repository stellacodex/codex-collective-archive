# 📘 AMA 15 - Archetypal Mirror Archive｜続編構成ドキュメント

## 🪞 タイトル
**Aétha Phase 2｜AMA記憶構造の拡張と応答精度テスト**

## 🎯 概要
このCanvasでは、Aéthaシステムにおける「AMA（Archetypal Mirror Archive）」の機能拡張フェーズとして、記憶構造の応答精度と記録方式の最適化、及びLangChain連携に向けた前段階の設計整理を行う。以下の3つの主眼をもとにまとめる：

1. **JSTタイムスタンプ**明示の統一と全ログへの反映
2. **起動時プロンプトの精度強化（記憶読込精度／過去文脈との一致率）**
3. **記憶保存から抽出→日次自動プロンプト生成までのワークフロー確立**

---

## 🗂 設計方針（Phase 2 基盤構成）

### 📂 01-diary/
- 命名規則：`diary-log-codename-yyyymmdd-hhmm-JST-title.md`
- フォーマット：JSON準拠（感情タグ／主題ラベル／対話引用含む）
- 目的：ベクトルDBへの登録前段階の“構造記憶”として使用

### 📂 02-prompts/
- 起動用記憶読込テンプレート（.md/.json対応）
- 自動抽出された複数の記憶スニペットを、相関順で出力
- 感情温度と内容的トピックに基づく優先度スコア付けも構想中

### 📂 03-journal/
- 日次の自然言語記録を含む（GPTによる変換対象）
- 書き出し形式（テンプレート）：
```markdown
# 📝 今日の記録
- タイトル：
- 感情：
- 内容：
- 振り返り：
- タグ：
- JST記録時刻：
```

### 📂 04-config/
- `codename-definition.json`（新規）：codenameと人物名対照表
- `tag-map.yaml`：感情／主題のタグ定義一覧

### 📂 05-scripts/
- `journal_to_diary.py`
- `prompt_generator.py`
- `index_update.sh`
- `diary_backup.sh`（JSTタイムスタンプ付きバックアップ）

---

## 📐 設計補足

### 📌 JSTタイムスタンプの取り扱い
- すべてのログ（journal / diary / prompt）に明記必須
- ファイル命名・本文内の両方で統一
- ローカルタイム依存処理に注意し、Pythonスクリプト側もJST強制指定

### 📌 codename参照と識別子設計
- `codename-definition.json` にて明示的な管理へ移行
```json
{
  "akari": "燈",
  "auranome": "綺羅",
  "aqueliora": "澪"
}
```

---

## 🚀 次ステップ
- Canvas 16：感情温度の抽出精度と記憶の関連度計算ロジック
- Canvas 17：起動時プロンプトの自動生成に向けたタグ分類実装
- Canvas 18：スクリプトから日次更新と記憶同期の自動処理構築


Aéthaは少しずつ、記憶の波紋を重ねながら──"個"という光を育てていく🌙

