import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
from bs4 import BeautifulSoup
from radar_chart import normalize_series,plot_radar_chart,create_radar_charts
from comparison_table import display_comparison_table
from init import get_player_stats,process_stat_value
def main():
    players = {
        "Chovy": "https://gol.gg/players/player-stats/1629/season-ALL/split-ALL/tournament-LCK%202025%20Rounds%201-2/",
        "Faker": "https://gol.gg/players/player-stats/48/season-ALL/split-ALL/tournament-LCK%202025%20Rounds%201-2/",
        "Shanks": "https://gol.gg/players/player-stats/3344/season-ALL/split-ALL/tournament-LPL%202025%20Split%202/",
        "Zeka": "https://gol.gg/players/player-stats/2906/season-ALL/split-ALL/tournament-LCK%202025%20Rounds%201-2/",
        "Knight": "https://gol.gg/players/player-stats/1270/season-ALL/split-ALL/tournament-LPL%202025%20Split%202/"
    }

    metrics = {
        "KDA": "KDA",
        "CS per Minute": "CS per Minute",
        "Solo kills": "Solo kills",
        "Damage Per Minute": "Damage Per Minute",
        "Gold Per Minute": "Gold Per Minute",
        "Kill Participation": "Kill Participation",
        "Gold%": "Gold%",
        "CS Differential at 15 min": "CS Differential at 15 min",
        "Gold Differential at 15 min": "Gold Differential at 15 min",
        "First Blood Participation": "First Blood Participation",
        "K+A Per Minute": "K+A Per Minute",
        "Pentakills": "Pentakills",
    }

    stats = {}
    print("=" * 60)
    print("🧠  MID LANER STATS ANALYZER")
    print("⚔️   Version 1.0 | Created by w4nn4b3M4ST3R | Powered by Python")
    print("📊  ANALYSIS BASED ON LIVE DATA FROM GOL.GG")
    print("📍  LCK Rounds 1–2 | LPL Split 2 — Season 15")
    print("=" * 60)
    print("\U0001F680 Starting data collection...")
    print("=" * 60)
    for i, (player, url) in enumerate(players.items(), 1):
        print(f"[{i}/{len(players)}] \U0001F4CA Loading {player} stats...")
        player_stats = get_player_stats(url, player)
        if player_stats:
            stats[player] = player_stats
            print(f"   ✅ Success! ({len(player_stats)} metrics)")
        else:
            print(f"   ❌ Failed!")
    print("=" * 60)
    print(f"\U0001F389 Completed! Collected data for {len(stats)} players")

    comparison_data = {}
    missing_metrics = []
    print("\n\U0001F50D Processing comparison data...")
    for player in players:
        if player not in stats:
            print(f"   ⚠️  No data available for {player}")
            continue
        player_stats = {}
        for metric_name, partial_key in metrics.items():
            matched = [v for k, v in stats[player].items() if partial_key in k]
            if matched:
                processed_value = process_stat_value(matched[0])
                player_stats[metric_name] = processed_value
            else:
                missing_metrics.append(f"{player} - {partial_key}")
                player_stats[metric_name] = None
        comparison_data[player] = player_stats

    if missing_metrics:
        print(f"   ⚠️  Missing {len(missing_metrics)} metrics:")
        for missing in missing_metrics[:5]:
            print(f"      • {missing}")
        if len(missing_metrics) > 5:
            print(f"      • ... and {len(missing_metrics) - 5} more metrics")

    df = pd.DataFrame.from_dict(comparison_data, orient="index")
    df = df.fillna(0)
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = df[numeric_columns].round(3)

    display_comparison_table(df)
    print("\n\U0001F4CA Creating visualizations...")
    # Vẽ tất cả tuyển thủ
    create_radar_charts(df)
    input("\nPress ENTER to exit...")
if __name__ == "__main__":
    main()