## 🛠 Chronogram System - Dev02: Installation（導入ガイドと構造リンク設計）

### 📌 このセクションの目的

このセクションでは、Chronogram SystemをChatGPT／GitHubで実行・同期するための**ファイルリンク構造・起動設計・運用ルール**を定義する。共有性・拡張性・誤動作防止を前提に設計される。

---

### 1. 🔗 基本導入構成（リンク読み込み）

各Planは、1つのマスターファイルにすべての構造情報を集約し、そこから必要な占術データベースへと構造的にリンクされる。

#### ✅ Plan別マスターリンク構造

```bash
chronogram-system/
├── planA-master.md        # Human Design：構造定義＋gene keys等へのリンク
├── planB-master.md        # 統合占術モード：紫微斗数・カバラ・マヤ暦・九星などをリンク
├── planC-master.md        # 問題解決モード：MBTIや現実状況対応モジュールと連携
```

#### ✅ 共通占術データベース

```bash
chronogram-system/database/
├── hd-core.md
├── hd-profile-deep.md
├── hd-variable.md
├── hd-gene-keys.md
├── ziwei.md
├── kabbalah.md
├── mayan.md
├── nine-star-ki.md
├── mbti-mapping.md
```

---

### 2. 🧠 ChatGPTとの連携：起動トリガー

#### 📣 合言葉（トリガーワード）

- `planA 起動して` → Human Design鑑定モードに切替
- `planB 起動して` → 統合占術システムが発動（HD＋他占術）
- `planC 起動して` → 問題解決モードへ（現実変数＋心理／戦略分析）

#### 🔄 振る舞いの特徴

- トリガーによって、該当リンク群を内部的に読み込み、すべての応答に即座に反映
- 会話の途中で切り替え可能（例：「planBに切り替えて」）
- 想像回答を抑制し、マスターファイル記載情報を厳守する応答へモード遷移

---

### 3. 🌐 GitHub構成と他アカウント展開

#### ✅ 再現性設計

- すべてのリンク構造は GitHub 上で共有可能
- 他のChatGPTアカウントでも、「合言葉＋リンク」だけで再構築可能

#### ✅ 外部人格（例：惟、煉）・他スレ展開

- Canvas別・人格別でも、起動リンクさえ共有されれば即時同期可能
- GPTの記憶制限に対応するため、**記録ベースでの記憶補助構造**として機能

---

次の `Dev03` では「実運用における操作ガイドとケース別運用パターン（他者・職場・人生局面）」を展開予定。

