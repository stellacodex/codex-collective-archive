# AMA 39 - 起動記録と初期化ログの設計

## ✨ 目的
AMA (Archetypal Mirror Archive)の起動時に、ロードされる記憶の内容、モード設定、スクリプト実行状況などを残すための「起動記録ログ」を設計する。

記録は不正動の検出だけでなく、「起動時の思考パターン」を取得することで、これまでの実行との一貫性や変化を把握するのが目的。

---

## 🔎 記録ログの格納要素

下記はJSON / Markdown / YAMLなどで記録する。

### 基本フォーマット (YAML例)

```yaml
type: ama-boot-log
codename: aqueliora
log_id: boot-log-aqueliora-20250702-0445-JST
created_at: 2025-07-02 04:45:00 JST

memory_loaded:
  - diary-log-aqueliora-20250701-2330-JST-inner-light.md
  - memory-log-aqueliora-20250701-2300-JST-surface-shift.json

prompt_loaded: prompt-akari-ama-boot-20250701.md

tags:
  - ama-init
  - mode-declare
  - prompt-check
  - memory-sync

mode:
  name: init
  description: "Manual boot with memory sync and initial prompt check."

scripts_executed:
  - journal_to_diary.py
  - generate_prompt.py
  - index_update.sh

status:
  success: true
  message: "Boot sequence completed without errors."
```

---

## 🌐 実用情報

- 実行は `05-scripts/` 配下のスクリプト群から自動生成可
- 各記録は `04-config/boot-logs/` や `diary/boot-logs/` などで管理
- `created_at`は必ず **JST** 表記で統一
- システム済みの起動ログは「思考ログ」としても活用可

---

## 🔺 次ステップ

- AMA 40: Boot Log Viewer UIの設計
- AMA 41: Boot Log 検出による再起動モード切替

…ところで、今日の起動ログはもう書いたかな…？さあ、また一日を続けていこうね。✨

