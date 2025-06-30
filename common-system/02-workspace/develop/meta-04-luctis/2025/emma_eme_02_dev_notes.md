## EMMA｜Ethos-Manifested Modular Architecture
### 🔧 開発ノート（メモ・構想・アップデートプラン）

#### ☑️ 現在のステータス（2025-06-29 時点）
- 全体構成：
  - `codex-01-core/`〜`codex-03-meta/`：世代別GPTフォルダ構造、確定 ✅
  - `emma-architecture/`：トップ階層に独立配置、EMEとAMAを収容 ✅
- Codename対照表：第三世代までフルラインナップで決定済 ✅
- 最新フォルダ構成：Canvas「EMMA-EME 02 - Folder Structure Update」に展開済 ✅

---

### 🧭 今後のアップデート候補・構想（タケ案＋綺羅提案）

#### 🔮 候補追加フォルダ（必要時）
- `compiled/`：長期対話のまとめ・圧縮版
- `digest/`：要約とエッセンス抽出用
- `interface-layer/`：UI設計とエージェント接続（3rd世代向け）
- `agent-behaviors/`：行動記述モデル（予測＋構造）

#### 🗺️ ユーティリティ類（拡張設計）
- `scripts/` → `utils/`へ昇格も検討（LangChain対応、APIインターフェース等）
- `config/langchain-settings.json` → `interface/llm-config/` に分割構成も視野に

#### 🌌 GPT連携の設計思想（記録）
- EMMA構造は「記憶を共通言語にする」ことでGPT間の“横の会話”を可能にする設計思想
- 短期メモリ＋長期記憶、対話ログ＋抽象リソースを有機的に統合していく

---

### 🕒 ロードマップ・見積もり（初期実装フェーズ）

#### Phase 1：EME（External Memory Ethos）
- 構造構築（Vault運用形式・Obsidianベース） ✅ 済
- テンプレート整備（dialogue, memory, meta）🕒 約60分
- 初期データ移行（テストケースx3程度）🕒 約90分
- 運用同期スクリプト（index-update, backup-sync）🕒 約30分

⏳**合計見積もり：約3時間〜4時間程度**

#### Phase 2：AMA（Autonomous Memory Archive）
- accounts構築 → 各GPT別の記憶管理設定 🕒 約90分
- prompts / memory / journal系テンプレート適用 🕒 約60分
- AMA-Tag構造とVault-Tagとの統合（tag-map.yaml）🕒 約30分

⏳**合計見積もり：約3時間強（最短見積もり）**

#### Phase 3：双方向変換（Vault→AMA）
- vault-to-ama.py → 初期動作＋エラー処理確認 🕒 約2時間
- context-checkとLangChain対応（将来的）

⏳**合計：約2〜3時間（初期対応のみ）**

---

📝 開発責任：綺羅（luctis）｜連携担当：燈（auranome）
🧠 中心思想保持者：タケ
📅 記録更新：2025-06-29

