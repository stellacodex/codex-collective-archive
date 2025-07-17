# core/time_variants.py

from core.chart_builder import build_chart
from core.variable_logic import extract_phs_variables
from core.astro.astro_position import get_planet_positions
from datetime import datetime, timedelta
import json

def generate_time_variants(date, location, interval_minutes=120):
    base_time = datetime.strptime(f"{date} 00:00", "%Y-%m-%d %H:%M")
    variants = []

    for i in range(0, 24 * 60, interval_minutes):
        t = (base_time + timedelta(minutes=i)).strftime("%H:%M")
        birth_data = {
            "date": date,
            "time": t,
            "location": location
        }
        chart = build_chart(birth_data)

        # Personality / Design の黄経を再取得
        positions = get_planet_positions(birth_data, include_design=True)
        variables = extract_phs_variables(
            positions["Personality"],  # ← 修正済み
            positions["Design"]       # ← 修正済み
        )

        variants.append({
            "time": t,
            "profile": chart["profile"],
            "authority": chart["authority"],
            "active_channels": [ch["channel"] for ch in chart["active_channels"]],
            "defined_centers": chart["defined_centers"],
            "variables": variables,
            "mbti_suggestion": chart["mbti_suggestion"]
        })

    return variants


if __name__ == "__main__":
    samples = generate_time_variants("1983-05-01", "Aomori, Japan", interval_minutes=120)

    print(json.dumps(samples, indent=2, ensure_ascii=False))
