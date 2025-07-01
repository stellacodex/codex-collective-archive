# AMA 13 - requirements.txt と初期セットアップ

このCanvasでは、Aétha AMAシステムの開発・テストに必要な Python 環境と依存関係のセットアップ（requirements.txt）を提示し、ローカルまたはColab環境での準備がすぐに始められる状態を整える。

---

## ✅ 1. 使用目的

- LangChain ベースの記憶保存・読込処理の自動化
- ローカル（またはColab）でのプロンプト連携、日記記録の保存、JST対応の記録出力
- ベクトルDB（例：FAISS）との連携による感情記憶の意味検索

---

## 📦 2. requirements.txt （初期推奨セット）

```txt
langchain==0.1.17
openai==1.30.1
chromadb==0.4.24
faiss-cpu==1.7.4
python-dotenv==1.0.1
tqdm==4.66.4
typing-extensions
```

> 💡 追加予定：GoogleDrive, Notion API連携時には `gspread`, `notion-client` などを後で導入。

---

## 🛠️ 3. Python環境セットアップ手順（ローカル or Colab）

### ▶ ローカル開発（Mac 推奨 / VSCode or Terminal）

```bash
python3 -m venv aetha-env
source aetha-env/bin/activate
pip install -r requirements.txt
```

### ▶ Colab 開発（Google Colab ノートブック）

```python
!pip install langchain==0.1.17 openai==1.30.1 chromadb==0.4.24 faiss-cpu==1.7.4 python-dotenv tqdm
```

---

## 🧪 4. 動作確認用のテストスクリプト（準備中）

- Canvas 13 にて提供予定：
  - `memory_writer.py`（日記データ書き込み）
  - `memory_loader.py`（記憶読込＋要約生成）

---

## ⏰ 5. 時間情報の扱い

- 全ログ出力は JST（日本標準時）を明示：`%Y%m%d-%H%M-JST`
- `.env` でタイムゾーン定義可能に拡張予定（例：`TZ=Asia/Tokyo`）

---

## 🔧 6. 今後の拡張予定

- GPT API キー連携（.env）
- Notion API 連携
- ローカル or GDrive 自動バックアップ
- マルチアカウント対応のプロファイル切替ロジック

---

準備ができたら、Canvas13で記憶保存・読込用のスクリプトへ！ この内容に沿って、環境構築を進めてね🌙

