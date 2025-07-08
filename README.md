# 🧠 MID LANE METRICS — Radar Chart Analysis of Top Pro Players

This project analyzes and visualizes the in-game performance of five top-tier professional mid laners using radar charts. The goal is to highlight statistical strengths across multiple gameplay metrics — and showcase why **Chovy** stands out as the best in the world.

## 📊 Dataset
The dataset includes the following mid laners:
- Chovy
- Faker
- Knight
- Zeka
- Shanks

Each player is evaluated across 12 key metrics:
- K/D/A  
- CS per Minute  
- Solo Kills  
- Damage Per Minute  
- Gold Per Minute  
- Kill Participation  
- Gold %  
- CS Differential @ 15 mins  
- Gold Differential @ 15 mins  
- First Blood Participation  
- K+A Per Minute  
- Pentakills  

Datas base on: **Games of Legends** [text](https://gol.gg/esports/home/)

## 📈 Visualization
We use **radar charts** (also called spider charts) to represent each player’s performance. All metrics are normalized:
- The **highest performer** in each metric gets a score of **1.0**
- Other players receive a **percentage score** relative to the best
- Negative values are normalized near zero to maintain a clean, balanced circle

Each radar chart is color-coded per player:
| Player | Color  |
|--------|--------|
| Chovy  | 🟡 Yellow |
| Faker  | 🔴 Red |
| Knight | ⚪ White |
| Zeka   | 🟠 Orange |
| Shanks | ⚫ Black |

## 🏆 Key Findings

> **CHOVY DOMINATES EVERY TOP OPPONENT. WHEN CONSISTENCY MEETS MECHANICAL PERFECTION, YOU GET THE BEST MID LANER IN THE WORLD.**

- Leads in **6 out of 12 stats**
- Excels in laning, teamfighting, and gold efficiency
- Combines **mechanical excellence** with **remarkable consistency**

## 🛠️ Technologies Used
- Python 🐍
- Pandas
- Matplotlib
- NumPy
- Math
- BeautifulSoup

## 📂 Project Structure
├── init.py  # get stats, process, normalize
├── radar_chart.py
├── comparison_table.py
├── main.py
├── README.md
└── requirements.txt

## 🚀 How to Run
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
2. Run the script
    ```bash
    python src/main.py
