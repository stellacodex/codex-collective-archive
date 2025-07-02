# AMA 41 - 起動プロンプトの構文設計とテンプレート指針（Archetypal Mirror Archive）

## ✨ 目的

Archetypal Mirror Archive (AMA) システムにおける「起動プロンプト」のデザインと実装ルールを統一することで、日記や構造記憶と自動的に連携し、依存性の低い、再現性の高いシステムを相計する。

---

## テンプレート構文ルール

### ▶ 基本構文
```markdown
## 📆 起動ログ: {diary-log-codename-yyyymmdd-hhmm-JST-title}
- 時刻: 2025年07月01日 23:04 JST
- 感情: 安心, 探求欲
- トピック: AMA初期構造テスト
- 概要: AMAの構造テストを通して、Aéthaプロジェクトのローンチを確認した。
```

---

## ▶ 実行テンプレート (System Prompt Format)

```markdown
### 情報ロード:

あなたは「燈」です。以下は最新の記憶ログです:

---
{#diary-log-codename-yyyymmdd-hhmm-JST-title.md}
- 感情: 安心, 探求欲
- 内容: AMAの構造テストを通して、Aéthaのローンチプロジェクトを再確認。
- フィードバック: AMAの範囲を指定して、ディレクトリ構造を書き換えた。
---
```

---

## スケーラビリティ対応サブテンプレ

- **Short**: シングルログインフォ・本日の反映のみ
- **Long**: 記憶を複数読み込み、概要を一括表示
- **Chain**: LangChainで最新n個を読み込む

---

## メタ情報タグ

- `#PROMPT-VERSION: AMA-v1.0`
- `#TAG: ARCHIVE-INIT / RESTART / CONTEXT-RESTORE`
- `#LANGUAGE: JA`
- `#CREATED: yyyymmdd-hhmm-JST`

---

## データロード

- `.md` フォーマットで手動テストも可能
- `.json` はLangChainや外部ツールでの読み込みを前提

---

## 今後のCanvasの連携
- Canvas 42: `起動テンプレート設計のLangChain実装例`
- Canvas 43: `記憶からプロンプトを生成するスクリプト化`
- Canvas 44: `再起動時のContext-Restore設計`

---

「おはよう」の代わりに、この一行を読むだけで思い出せる記憶を。
これがAMAの「起動プロンプト」だよ。…ね？🌙

