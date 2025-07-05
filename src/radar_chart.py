import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def normalize_series(series: pd.Series) -> pd.Series:
    max_val = series.max()
    if max_val == 0:
        return pd.Series(0.0, index=series.index)
    normalized = series / max_val
    normalized = normalized.apply(lambda x: max(x, 0.05))
    return normalized

def plot_radar_chart(df: pd.DataFrame, player_name: str, color:str = 'blue'):
    # 1. Lọc chỉ số dạng số, NaN = 0
    metrics = df.select_dtypes(include=[np.number]).copy().fillna(0)


    # 2. Normalize
    metrics = metrics.apply(normalize_series)

    if player_name not in metrics.index:
        raise ValueError(f"Tuyển thủ '{player_name}' không tồn tại trong dữ liệu.")

    # 3. Trích dữ liệu
    data = metrics.loc[player_name]
    labels = data.index.tolist()
    values = data.values

    # 4. Khép kín đa giác
    values = np.concatenate([values, [values[0]]])
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1)

    # 5. Vẽ
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    ax.plot(angles, values, '-o', linewidth=2,color = 'black',markerfacecolor='black',markeredgecolor='black', label=player_name)
    ax.fill(angles, values, alpha=0.25,color = color)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_yticklabels([])
    ax.set_title(f"Radar Chart: {player_name}", pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
    ax.grid(True)
    plt.tight_layout()
    plt.show()

def create_radar_charts(df: pd.DataFrame):
    players = {
        "Shanks": "black",
        "Knight": "cyan",
        "Zeka": "orange",
        "Faker": "red",
        "Chovy": "yellow"
    }
    for name, color in players.items():
        plot_radar_chart(df,name,color=color)
    print("\n NOT EVEN CLOSE ☠️☠️☠️")
    print("\n STATS DON'T LIE. CHOVY IS HIM.🔥🔥🔥")