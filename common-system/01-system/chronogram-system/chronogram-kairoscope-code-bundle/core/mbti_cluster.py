# core/mbti_cluster.py

from collections import defaultdict
from core.mbti_templates import suggest_mbti_from_profile_and_variable

def cluster_variants_by_mbti(variants):
    """
    複数のチャート候補から、推定MBTIタイプごとにクラスタリングする。
    """
    cluster_dict = defaultdict(list)

    for entry in variants:
        profile = entry.get("profile")
        variable_code = entry.get("variables", {}).get("Variable")
        mbti_guess = suggest_mbti_from_profile_and_variable(profile, variable_code)

        if mbti_guess:
            cluster_dict[mbti_guess].append(entry)

    sorted_clusters = sorted(cluster_dict.items(), key=lambda x: len(x[1]), reverse=True)

    return {
        "top_clusters": sorted_clusters[:3],
        "summary": {
            "total_variants": len(variants),
            "unique_mbti_types": list(cluster_dict.keys())
        }
    }

if __name__ == "__main__":
    from core.time_variants import generate_time_variants
    import json

    # 実行例
    variants = generate_time_variants("1983-05-01", "Aomori, Japan", interval_minutes=120)
    result = cluster_variants_by_mbti(variants)

    # 保存
    with open("samples/clustered_mbti.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # 表示
    print(json.dumps(result, indent=2, ensure_ascii=False))
