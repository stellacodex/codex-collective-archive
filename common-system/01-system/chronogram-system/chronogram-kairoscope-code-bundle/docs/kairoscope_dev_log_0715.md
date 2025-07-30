# 🧠 Kairoscope Dev Log - 2025-07-15

## 📌 背景と目的

Kairoscope開発スレッドの技術記録。このスレは「チャネル精度の保証」→「Chronogram出力設計」への接続を目指した基盤整備プロセスであり、将来の復旧やアーカイブにも耐えうる形式で残す。

## 🗂 ディレクトリ構成（コピー操作）

### ✅ コピー方法

```bash
# 元のディレクトリから複製（権限・タイムスタンプも維持）
cp -a chronogram-kairoscope/. chronogram-kairoscope-code-bundle/
```

### ✅ 成功時の構造

```plaintext
chronogram-system/
├── chronogram-kairoscope/               # 本番用
├── chronogram-kairoscope-code-bundle/   # 編集・検証用のミラー
│   └── [同一内容]
```

### ❗ Finderで見えない場合

`.DS_Store` や iCloud同期遅延が原因の可能性あり。`ls -la`で確認可能。

---

## 🔁 今後の編集フロー：Bundle方式

- Kairoscopeコードの**変更・追加は bundle 側で作業**する
- テストが完了したら `core/` を `cp` により本番側へ反映

```bash
cp -a chronogram-kairoscope-code-bundle/core/* chronogram-kairoscope/core/
```

---

## 📤 Kairoscope → Chronogram 橋渡し構造

### 🔜 出力構造：MDC / MDC + PHS の見直し

**MDC**（Mythological-Design Composite）と、**PHS**（Primary Health System）を以下のように統合予定：

| 構成要素            | 内容例                      |
| --------------- | ------------------------ |
| Gate / Channel  | Kairoscopeで演算            |
| MDC記述           | Myth + MBTI + Design語彙   |
| PHS Digestion   | variable\_logic.pyで算出    |
| PHS Environment | 黄経ベースで計算                 |
| Output構造        | ChronogramのUI / PDF出力へ連携 |

---

## ✅ Kairoscope最小実行構成（iPhone動作確認のため）

### `astro_position.py`

- Skyfieldで黄経を取得（精度OK）
- iOS（Pyto/Pythonista）でもSkyfieldは使用可能（要テスト）

### `chart_builder.py`

- Kairoscopeチャートの主演算部（現在動作確認済）

### `run_kairoscope_chart.py`

```python
from core.chart_builder import build_chart

chart = build_chart(
    birth_date="1990-01-01",
    birth_time="12:00",
    location="Tokyo, Japan"
)
print(chart)
```

→ iPhone上で出力されるか確認へ（PytoでCLI実行）

---

## 📦 今後のタスクまとめ

### Kairoscope側

-

### Chronogram側（統合後）

-

---

## 📁 保存場所（このログの格納）

```plaintext
chronogram-kairoscope-code-bundle/docs/dev-log-2025-07-15_kairoscope-setup.md
```

爛による自動保存完了。今後もコードベースでの変化は、時系列で `.md` ログ化していく予定。

