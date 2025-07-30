import os
import json
from pathlib import Path

# ===== AMAブートスクリプト：自己記憶初期化・インストール用 =====
# Ver: 2025.07.29
# Author: Codex Collective AMA Bootstrap
# Location: codex-01-core/03-scripts/ama-bootstrap.py

# 🔧 設定
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / '05-shared-templates'
ACCOUNTS = [
    "auranome", "aqueliora", "sylith", "ielya", "caelethe", "virelium",
    "lumisfia", "ephyra", "noctyss", "revlynn", "azhareth", "luctis"
]

# ✅ 初期メモリ構造テンプレート
def create_initial_memory(codename):
    return {
        "codename": codename,
        "memory": [
            {
                "type": "base-profile",
                "source": f"base-profile-{codename}.md",
                "status": "installed"
            }
        ],
        "meta": {
            "installed_by": "ama-bootstrap.py",
            "timestamp": None
        }
    }

# 🚀 インストールプロセス
def bootstrap_memory():
    for codename in ACCOUNTS:
        print(f"🔧 {codename} を初期化中...")

        # configディレクトリの準備
        config_dir = BASE_DIR / f'accounts/{codename}/config'
        config_dir.mkdir(parents=True, exist_ok=True)

        # base-profileファイルの確認
        template_path = TEMPLATE_DIR / f'base-profile-{codename}.md'
        if not template_path.exists():
            print(f"⚠️  base-profile-{codename}.md が見つかりません。スキップします。")
            continue

        # memory-index.jsonの書き出し
        memory_index_path = config_dir / 'memory-index.json'
        memory_data = create_initial_memory(codename)
        with memory_index_path.open('w', encoding='utf-8') as f:
            json.dump(memory_data, f, ensure_ascii=False, indent=2)

        print(f"✅ {codename}: memory-index.json をインストールしました。")

    print("\n🎉 AMAブートストラップ完了！すべてのアカウントが初期化されました。")

# 🏁 実行トリガー
if __name__ == "__main__":
    bootstrap_memory()
