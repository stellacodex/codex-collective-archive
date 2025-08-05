# constitutional theory 素質タイプ（詳細）

##  CANCODE-BIZ HRプロファイリングテンプレート（強化版）

**フォーマット**：Markdownベース（Power BIやCanvaでのビジュアライズ推奨）  
**デザインコンセプト**：シンプルかつエレガント。タケの視覚言語を活かし、データが「物語の断片」として響くように。

---

### シート2：スキルの風景 (Landscape of Skills)

**目的**：社員のスキルを「風景」として可視化し、プロジェクトや育成に活用。  
**視覚的要素**：バブルチャートでスキル分布を表現。習熟度（X軸）、経験年数（Y軸）、スキルの影響度（バブルサイズ）。

#### スキル分布表

| スキル       | 習熟度 | 経験年数 | 重要度 | 実績                        |
|--------------|--------|----------|--------|-----------------------------|
| Python       | 上級   | 7年      | ****   | 決済システム開発（2024）    |
| AWS          | 中級   | 5年      | ***    | クラウド移行プロジェクト    |
| リーダーシップ | 上級   | 6年      | ****   | チーム管理（10名）         |

**視覚的メモ**：Pythonとリーダーシップは「風景」の中心に輝く星。AWSは成長中の丘。

#### バブルチャート（ビジュアライズ用）

以下のコードを [Chart.js](https://chartjs.org) に入力して、スキル分布をバブルチャートで確認：

```chartjs
{
  "type": "bubble",
  "data": {
    "datasets": [
      {
        "label": "Technical Skills",
        "data": [
          { "x": 8, "y": 7, "r": 20, "label": "Python" },
          { "x": 6, "y": 5, "r": 15, "label": "AWS" },
          { "x": 4, "y": 8, "r": 10, "label": "Blockchain" }
        ],
        "backgroundColor": "rgba(54, 162, 235, 0.7)",
        "borderColor": "rgba(54, 162, 235, 1)"
      },
      {
        "label": "Soft Skills",
        "data": [
          { "x": 7, "y": 6, "r": 18, "label": "Leadership" },
          { "x": 5, "y": 4, "r": 12, "label": "Communication" }
        ],
        "backgroundColor": "rgba(255, 99, 132, 0.7)",
        "borderColor": "rgba(255, 99, 132, 1)"
      }
    ]
  },
  "options": {
    "scales": {
      "x": { "title": { "display": true, "text": "Proficiency Level" } },
      "y": { "title": { "display": true, "text": "Experience Years" } }
    },
    "plugins": {
      "legend": { "position": "top" },
      "title": { "display": true, "text": "Employee Skill Landscape" }
    }
  }
}
```

#### 参考ビジュアル
- **画像リンク**：バブルチャート例（事前生成）は[こちら](https://example.com/skill_bubble_chart.png)。
- **代替案**：Power BIでダッシュボードを作成し、スキル分布を動的に表示（[Power BI](https://powerbi.microsoft.com)）。

---

（※他のシートは前回のMarkdownテンプレートを継承。省略してシート2のみ強化。）